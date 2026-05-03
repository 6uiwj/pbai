"""
presentation/serializers.py — DRF 입력 Serializer

[DDD 표현 계층]
Serializer는 클라이언트로부터 받은 JSON 데이터를 검증(validate)합니다.

역할:
  - 필수 필드 누락 여부 확인
  - 데이터 타입 및 길이 검증
  - 검증 통과 시 validated_data 딕셔너리 제공

주의: 여기서는 "입력 검증"만 담당합니다.
      응답(출력) 직렬화는 View에서 dataclasses.asdict()로 처리합니다.
      (ResponseDTO → dict 변환은 DRF JSONRenderer가 datetime을 자동 처리)
"""
from rest_framework import serializers


class CreatePostSerializer(serializers.Serializer):
    """
    게시글 생성 요청 검증.
    POST /api/posts/ 요청 바디를 검증합니다.
    """
    title = serializers.CharField(
        max_length=200,
        error_messages={'blank': '제목을 입력해주세요.', 'max_length': '제목은 200자 이하여야 합니다.'}
    )
    content = serializers.CharField(
        error_messages={'blank': '내용을 입력해주세요.'}
    )
    author = serializers.CharField(
        max_length=100,
        error_messages={'blank': '작성자를 입력해주세요.', 'max_length': '작성자 이름은 100자 이하여야 합니다.'}
    )


class UpdatePostSerializer(serializers.Serializer):
    """
    게시글 수정 요청 검증.
    PUT /api/posts/:id/ 요청 바디를 검증합니다.
    작성자(author)는 수정 불가이므로 포함하지 않습니다.
    """
    title = serializers.CharField(
        max_length=200,
        error_messages={'blank': '제목을 입력해주세요.'}
    )
    content = serializers.CharField(
        error_messages={'blank': '내용을 입력해주세요.'}
    )
