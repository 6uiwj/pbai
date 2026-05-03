"""
presentation/views.py — DRF APIView (HTTP 요청 처리)

[DDD 표현 계층]
View는 HTTP 요청을 받아 Application 계층(Service)에 위임하고
결과를 HTTP 응답으로 변환하는 역할만 담당합니다.

처리 흐름:
  HTTP 요청 → Serializer(입력 검증) → DTO 생성 → Service 호출 → Response 반환

각 클래스:
  PostListView   — 목록 조회(GET) + 생성(POST)   : /api/posts/
  PostDetailView — 상세 조회(GET) + 수정(PUT) + 삭제(DELETE) : /api/posts/:id/

asdict()를 사용해 ResponseDTO → dict 변환 시
DRF의 JSONRenderer가 datetime을 ISO 8601 문자열로 자동 직렬화합니다.
"""
from dataclasses import asdict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..application.post_service import PostService
from ..application.dto.post_dto import CreatePostDTO, UpdatePostDTO
from ..infrastructure.repositories.post_repository_impl import DjangoPostRepository
from .serializers import CreatePostSerializer, UpdatePostSerializer


def _service() -> PostService:
    """
    PostService 인스턴스를 생성해 반환합니다.
    DjangoPostRepository를 의존성으로 주입합니다.
    요청마다 새 인스턴스를 생성하는 단순한 방식 (향후 DI 컨테이너로 개선 가능).
    """
    return PostService(DjangoPostRepository())


class PostListView(APIView):
    """
    /api/posts/ 엔드포인트
    GET: 전체 게시글 목록 반환
    POST: 새 게시글 생성
    """

    def get(self, request):
        """
        전체 게시글 목록을 반환합니다.
        200 OK + Post 배열 JSON
        """
        posts = _service().get_all_posts()
        # ResponseDTO 리스트를 dict 리스트로 변환해 JSON 응답
        return Response([asdict(p) for p in posts])

    def post(self, request):
        """
        새 게시글을 생성합니다.
        요청 바디: { title, content, author }
        201 Created + 생성된 Post JSON
        400 Bad Request: 입력 검증 실패 시
        """
        serializer = CreatePostSerializer(data=request.data)
        if not serializer.is_valid():
            # 검증 실패: 어떤 필드가 왜 잘못됐는지 상세 에러 반환
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 검증된 데이터로 DTO 생성 후 서비스 호출
        dto = CreatePostDTO(**serializer.validated_data)
        post = _service().create_post(dto)
        return Response(asdict(post), status=status.HTTP_201_CREATED)


class PostDetailView(APIView):
    """
    /api/posts/<id>/ 엔드포인트
    GET: 단일 게시글 조회
    PUT: 게시글 수정
    DELETE: 게시글 삭제
    """

    def get(self, request, post_id: int):
        """
        단일 게시글을 반환합니다.
        200 OK + Post JSON
        404 Not Found: 존재하지 않는 게시글
        """
        post = _service().get_post(post_id)
        if not post:
            return Response(
                {'detail': '게시글을 찾을 수 없습니다.'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(asdict(post))

    def put(self, request, post_id: int):
        """
        게시글을 수정합니다.
        요청 바디: { title, content }
        200 OK + 수정된 Post JSON
        404 Not Found: 존재하지 않는 게시글
        """
        serializer = UpdatePostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dto = UpdatePostDTO(**serializer.validated_data)
        post = _service().update_post(post_id, dto)
        if not post:
            return Response(
                {'detail': '게시글을 찾을 수 없습니다.'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(asdict(post))

    def delete(self, request, post_id: int):
        """
        게시글을 삭제합니다.
        204 No Content: 삭제 성공 (응답 바디 없음)
        404 Not Found: 존재하지 않는 게시글
        """
        if not _service().delete_post(post_id):
            return Response(
                {'detail': '게시글을 찾을 수 없습니다.'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
