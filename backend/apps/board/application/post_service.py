"""
application/post_service.py — PostService (유스케이스 집합)

[DDD 애플리케이션 계층]
Service는 "사용자가 할 수 있는 일"을 메서드로 나열한 클래스입니다.
각 메서드 = 하나의 유스케이스(Use Case).

역할:
  - Presentation 계층(View)으로부터 DTO를 받아 처리
  - Domain 계층(Repository 인터페이스)을 통해 데이터를 읽고 씀
  - 처리 결과를 ResponseDTO로 변환해 View에 반환

중요: Service는 HTTP, ORM 등을 직접 다루지 않습니다.
      덕분에 웹 프레임워크 없이도 테스트할 수 있습니다.
"""
from typing import List, Optional

from ..domain.entities.post import Post
from ..domain.repositories.post_repository import PostRepository
from .dto.post_dto import CreatePostDTO, UpdatePostDTO, PostResponseDTO


class PostService:
    """
    게시글 비즈니스 로직 서비스.

    생성자에서 Repository 인터페이스를 주입받습니다(의존성 주입).
    테스트 시 FakeRepository를 주입하면 DB 없이도 테스트할 수 있습니다.
    """

    def __init__(self, repository: PostRepository):
        # Repository 인터페이스만 알고 구체 구현(DjangoPostRepository)은 모름
        self._repository = repository

    def _to_response(self, post: Post) -> PostResponseDTO:
        """
        도메인 엔티티 → 응답 DTO 변환.
        View에 필요한 데이터만 포함시켜 내부 도메인 구조를 숨깁니다.
        """
        return PostResponseDTO(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.author,
            created_at=post.created_at,
            updated_at=post.updated_at,
        )

    def get_all_posts(self) -> List[PostResponseDTO]:
        """전체 게시글 목록 조회 유스케이스."""
        return [self._to_response(p) for p in self._repository.find_all()]

    def get_post(self, post_id: int) -> Optional[PostResponseDTO]:
        """
        단일 게시글 조회 유스케이스.
        존재하지 않으면 None을 반환하며, View에서 404 처리합니다.
        """
        post = self._repository.find_by_id(post_id)
        return self._to_response(post) if post else None

    def create_post(self, dto: CreatePostDTO) -> PostResponseDTO:
        """
        게시글 생성 유스케이스.
        DTO → 도메인 엔티티 생성 → Repository 저장 → ResponseDTO 반환
        """
        post = Post(title=dto.title, content=dto.content, author=dto.author)
        return self._to_response(self._repository.save(post))

    def update_post(self, post_id: int, dto: UpdatePostDTO) -> Optional[PostResponseDTO]:
        """
        게시글 수정 유스케이스.
        먼저 존재 여부를 확인한 뒤 수정합니다.
        존재하지 않으면 None을 반환합니다.
        """
        post = self._repository.find_by_id(post_id)
        if not post:
            return None  # View에서 404 처리
        # 엔티티 필드를 직접 수정 후 저장 (작성자는 불변)
        post.title = dto.title
        post.content = dto.content
        return self._to_response(self._repository.save(post))

    def delete_post(self, post_id: int) -> bool:
        """
        게시글 삭제 유스케이스.
        성공 여부를 bool로 반환합니다.
        존재하지 않으면 False, 삭제 성공이면 True.
        """
        if not self._repository.find_by_id(post_id):
            return False
        self._repository.delete(post_id)
        return True
