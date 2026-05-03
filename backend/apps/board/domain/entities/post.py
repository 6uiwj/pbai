"""
domain/entities/post.py — Post 도메인 엔티티

[DDD 도메인 계층]
엔티티(Entity)는 고유 ID를 가지는 핵심 비즈니스 객체입니다.
이 파일은 "게시글이란 무엇인가"를 순수 Python으로 정의합니다.

중요: Django ORM, DRF 등 어떤 프레임워크도 import하지 않습니다.
      도메인은 인프라에 의존해서는 안 됩니다 (DDD 원칙).
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Post:
    """
    게시글 엔티티.

    dataclass를 사용해 boilerplate(__init__, __repr__ 등)를 자동 생성합니다.

    Attributes:
        title: 게시글 제목
        content: 게시글 본문 내용
        author: 작성자 이름
        id: 게시글 고유 번호 (DB 저장 전에는 None)
        created_at: 작성 일시 (DB 저장 후 설정됨)
        updated_at: 최종 수정 일시 (DB 저장 후 설정됨)
    """
    title: str
    content: str
    author: str
    id: Optional[int] = None          # 생성 전에는 ID가 없으므로 Optional
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
