"""
config/urls.py — URL 라우팅 설정 (진입점)

모든 HTTP 요청은 여기서 어떤 View가 처리할지 결정됩니다.

URL 구조:
  /api/posts/          → PostListView  (목록 조회 + 생성)
  /api/posts/<id>/     → PostDetailView (상세 조회 + 수정 + 삭제)

<int:post_id>: URL 파라미터를 정수(int)로 자동 변환해 View 함수에 전달합니다.
               예: /api/posts/3/ → post_id=3
"""
from django.urls import path
from apps.board.presentation.views import PostListView, PostDetailView

urlpatterns = [
    # 게시글 목록 + 생성
    path('api/posts/', PostListView.as_view()),

    # 게시글 상세 + 수정 + 삭제
    # <int:post_id>: URL의 숫자 부분을 post_id 변수로 View에 전달
    path('api/posts/<int:post_id>/', PostDetailView.as_view()),
]
