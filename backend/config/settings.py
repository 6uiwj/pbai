"""
config/settings.py — Django 프로젝트 설정

환경변수(.env 파일)에서 민감한 값을 읽어옵니다.
os.environ.get('KEY', '기본값') 형식으로 읽으며,
기본값은 로컬 개발 환경에서만 사용합니다. 운영 서버에서는 반드시 환경변수를 설정하세요.
"""
from pathlib import Path
import os

# 프로젝트 루트 경로 (manage.py 가 있는 디렉터리)
BASE_DIR = Path(__file__).resolve().parent.parent

# ─────────────────────────────────────────────
# 보안 설정
# ─────────────────────────────────────────────

# Django 암호화에 사용되는 비밀 키 — 절대 코드에 직접 작성하지 마세요
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-in-production')

# DEBUG=True 이면 에러 상세 정보가 브라우저에 노출됨 → 운영 서버에서는 반드시 False
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Django가 응답할 허용 호스트 목록 (쉼표 구분)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ─────────────────────────────────────────────
# 설치된 앱 목록
# ─────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.contenttypes',  # 콘텐츠 타입 프레임워크 (DRF가 필요)
    'django.contrib.auth',          # 인증 프레임워크 (contenttypes 의존성)
    'rest_framework',               # Django REST Framework
    'corsheaders',                  # 프론트엔드(다른 origin)의 API 호출 허용
    'apps.board',                   # 우리가 만든 게시판 앱
]

# ─────────────────────────────────────────────
# 미들웨어 — 요청이 View에 닿기 전 처리 레이어
# ─────────────────────────────────────────────
MIDDLEWARE = [
    # CORS 헤더 추가 — 반드시 제일 위에 위치해야 OPTIONS 요청을 올바르게 처리
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# URL 라우팅 설정 파일 위치
ROOT_URLCONF = 'config.urls'

# ─────────────────────────────────────────────
# 데이터베이스 — PostgreSQL (docker-compose의 db 서비스)
# ─────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'boarddb'),
        'USER': os.environ.get('POSTGRES_USER', 'boarduser'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'boardpass'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),   # docker-compose 서비스명
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# ─────────────────────────────────────────────
# CORS (Cross-Origin Resource Sharing)
# 프론트엔드(localhost:5173)가 백엔드(localhost:8000)에 API 요청할 수 있도록 허용
# ─────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = os.environ.get(
    'CORS_ALLOWED_ORIGINS', 'http://localhost:5173'
).split(',')

# ─────────────────────────────────────────────
# DRF (Django REST Framework) 기본 설정
# ─────────────────────────────────────────────
REST_FRAMEWORK = {
    # 응답을 항상 JSON으로 렌더링 (BrowsableAPI 제거로 불필요한 HTML 렌더러 비활성화)
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# ─────────────────────────────────────────────
# 기타 설정
# ─────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # PK 기본 타입: BigInt

USE_TZ = True               # 시간대를 인식하는 datetime 사용
TIME_ZONE = 'Asia/Seoul'    # 서버 기본 시간대
LANGUAGE_CODE = 'ko-kr'     # 언어 설정
