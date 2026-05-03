"""
application/dto/post_dto.py — 애플리케이션 계층 DTO (Data Transfer Object)

[DDD 애플리케이션 계층]
DTO는 계층 간 데이터를 주고받을 때 사용하는 단순 데이터 컨테이너입니다.

왜 DTO를 사용하나요?
  - Presentation(View) → Application(Service): 무엇을 요청하는지 명확히 전달
  - Application(Service) → Presentation(View): 서비스 결과를 일관된 형태로 반환
  - 도메인 엔티티를 외부에 직접 노출하지 않아 내부 구현을 숨깁니다

구조:
  - CreatePostDTO: 게시글 생성 요청 데이터
  - UpdatePostDTO: 게시글 수정 요청 데이터 (작성자는 수정 불가)
  - PostResponseDTO: 서비스가 View에 반환하는 게시글 데이터
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class CreatePostDTO:
    """
    게시글 생성 요청 DTO.
    Presentation 계층(View)이 Application 계층(Service)에 전달합니다.
    """
    title: str
    content: str
    author: str


@dataclass
class UpdatePostDTO:
    """
    게시글 수정 요청 DTO.
    작성자(author)는 생성 후 변경 불가이므로 포함하지 않습니다.
    """
    title: str
    content: str


@dataclass
class PostResponseDTO:
    """
    게시글 응답 DTO.
    Service가 처리 결과를 View에 반환할 때 사용합니다.
    View는 이 DTO를 JSON으로 직렬화해 클라이언트에 응답합니다.
    """
    id: int
    title: str
    content: str
    author: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
