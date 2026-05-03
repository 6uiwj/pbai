"""
infrastructure/models.py — Django ORM 모델 (DB 테이블 정의)

[DDD 인프라 계층]
ORM 모델은 DB 테이블 구조를 Python 클래스로 표현한 것입니다.
Django가 이 클래스를 읽어 SQL 테이블을 생성하고 쿼리를 실행합니다.

주의: 이 모델은 DB 접근용 전용 객체입니다.
      비즈니스 로직은 domain/entities/post.py의 Post 엔티티에서 처리합니다.
      ORM 모델과 도메인 엔티티를 분리함으로써 DB 변경 시 도메인이 영향받지 않습니다.
"""
from django.db import models


class PostModel(models.Model):
    """
    게시글 DB 테이블 (posts).

    Django ORM 모델 — DB 스키마를 정의합니다.
    실제 비즈니스 로직은 Post 엔티티(domain/entities/post.py)에 있습니다.
    """
    title = models.CharField(max_length=200)       # 제목 (최대 200자)
    content = models.TextField()                    # 본문 (길이 제한 없음)
    author = models.CharField(max_length=100)       # 작성자 (최대 100자)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시 자동 기록
    updated_at = models.DateTimeField(auto_now=True)      # 저장할 때마다 자동 갱신

    class Meta:
        app_label = 'board'         # Django가 이 모델이 속한 앱을 인식하는 레이블
        db_table = 'posts'          # 실제 DB 테이블 이름
        ordering = ['-created_at']  # 기본 정렬: 최신 글 먼저

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
