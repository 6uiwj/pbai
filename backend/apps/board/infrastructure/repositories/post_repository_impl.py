"""
infrastructure/repositories/post_repository_impl.py — PostRepository 구현체

[DDD 인프라 계층]
도메인 계층에서 정의한 PostRepository 인터페이스를 Django ORM으로 구현합니다.

핵심 역할:
  - ORM 모델(PostModel) ↔ 도메인 엔티티(Post) 변환
  - Django ORM 쿼리 실행 (SELECT, INSERT, UPDATE, DELETE)

이 파일만 수정하면 DB 종류를 바꿀 수 있습니다 (PostgreSQL → MongoDB 등).
"""
from typing import List, Optional

from ...domain.entities.post import Post
from ...domain.repositories.post_repository import PostRepository
from ..models import PostModel


class DjangoPostRepository(PostRepository):
    """
    Django ORM을 사용한 PostRepository 구현체.
    PostgreSQL에 게시글 데이터를 저장·조회합니다.
    """

    def _to_entity(self, model: PostModel) -> Post:
        """
        ORM 모델 → 도메인 엔티티 변환.
        DB에서 읽어온 PostModel을 비즈니스 로직에서 사용하는 Post로 변환합니다.
        """
        return Post(
            id=model.id,
            title=model.title,
            content=model.content,
            author=model.author,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    def find_by_id(self, post_id: int) -> Optional[Post]:
        """
        ID로 게시글 단건 조회.
        DoesNotExist 예외를 잡아 None으로 변환합니다 (상위 계층에서 예외 처리 불필요).
        """
        try:
            return self._to_entity(PostModel.objects.get(pk=post_id))
        except PostModel.DoesNotExist:
            return None  # 없는 게시글 → 404 처리는 View에서

    def find_all(self) -> List[Post]:
        """
        전체 게시글 목록 조회.
        정렬은 PostModel.Meta.ordering = ['-created_at'] 에 의해 최신순으로 처리됩니다.
        """
        return [self._to_entity(m) for m in PostModel.objects.all()]

    def save(self, post: Post) -> Post:
        """
        게시글 저장 (생성 또는 수정).

        post.id가 None이면 새 레코드를 INSERT합니다.
        post.id가 있으면 해당 레코드를 UPDATE합니다.

        updated_at은 auto_now=True로 설정되어 있어 자동 갱신됩니다.
        """
        if post.id is not None:
            # 기존 게시글 수정 — filter+update로 불필요한 SELECT 없이 UPDATE
            PostModel.objects.filter(pk=post.id).update(
                title=post.title,
                content=post.content,
                author=post.author,
            )
            # updated_at 등 DB가 갱신한 값을 반영하기 위해 다시 조회
            model = PostModel.objects.get(pk=post.id)
        else:
            # 새 게시글 생성 — INSERT
            model = PostModel.objects.create(
                title=post.title,
                content=post.content,
                author=post.author,
            )
        return self._to_entity(model)

    def delete(self, post_id: int) -> None:
        """
        게시글 삭제.
        존재하지 않아도 오류가 발생하지 않습니다 (filter는 매칭 없어도 에러 없음).
        """
        PostModel.objects.filter(pk=post_id).delete()
