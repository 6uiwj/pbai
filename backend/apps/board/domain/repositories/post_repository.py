"""
domain/repositories/post_repository.py — PostRepository 추상 인터페이스

[DDD 도메인 계층]
Repository 인터페이스는 "데이터를 어떻게 가져올 수 있는가"의 계약(contract)입니다.
구체적인 구현(SQLite, PostgreSQL, MongoDB 등)은 Infrastructure 계층이 담당합니다.

도메인 계층은 이 인터페이스만 알고, 실제 DB가 무엇인지는 모릅니다.
덕분에 DB를 바꿔도 도메인·애플리케이션 코드는 수정할 필요가 없습니다.

ABC(Abstract Base Class): Python에서 인터페이스를 구현하는 방식입니다.
@abstractmethod로 표시된 메서드는 반드시 자식 클래스에서 구현해야 합니다.
"""
from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.post import Post


class PostRepository(ABC):
    """
    게시글 저장소 추상 인터페이스.
    인프라 계층의 DjangoPostRepository가 이를 구현합니다.
    """

    @abstractmethod
    def find_by_id(self, post_id: int) -> Optional[Post]:
        """
        ID로 단일 게시글을 조회합니다.
        존재하지 않으면 None을 반환합니다.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[Post]:
        """
        모든 게시글 목록을 반환합니다.
        정렬은 구현체(Infrastructure)가 결정합니다.
        """
        pass

    @abstractmethod
    def save(self, post: Post) -> Post:
        """
        게시글을 저장합니다.
        - post.id가 None이면 새 레코드 INSERT
        - post.id가 있으면 기존 레코드 UPDATE
        저장 후 DB가 생성한 id·created_at·updated_at이 채워진 엔티티를 반환합니다.
        """
        pass

    @abstractmethod
    def delete(self, post_id: int) -> None:
        """ID에 해당하는 게시글을 삭제합니다."""
        pass
