# pythonBoardEx

Django + React/TypeScript 게시판 예제 프로젝트.
DDD + 4 Layered Architecture로 구성된 백엔드와 Vite 기반 프론트엔드를 Docker Compose로 실행합니다.

---

## ⚡ 실행 방법

```bash
# .env 파일 준비 (.env.example 복사)
cp .env.example .env

# 전체 스택 실행
docker-compose up --build

# 백그라운드 실행
docker-compose up -d --build
```

| 서비스 | 주소 |
|--------|------|
| 프론트엔드 | http://localhost:5173 |
| 백엔드 API | http://localhost:8000/api/posts/ |
| PostgreSQL | localhost:5432 |

---

## 📁 폴더 구조

```
pythonBoardEx/
├── docker-compose.yml
├── .env                    # 환경변수 (git 제외)
├── .env.example            # 환경변수 템플릿
├── CLAUDE.md               # Claude Code 행동 지침
├── SECURITY.md             # 🚨 보안 사고 비상 매뉴얼
│
├── backend/                # Django 백엔드
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/             # Django 프로젝트 설정
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── apps/
│       └── board/          # 게시판 앱 (DDD 4-Layered)
│           ├── domain/             # ① 도메인 계층
│           │   ├── entities/post.py          # Post 엔티티
│           │   └── repositories/             # Repository 인터페이스 (ABC)
│           ├── application/        # ② 애플리케이션 계층
│           │   ├── dto/post_dto.py           # 요청/응답 DTO
│           │   └── post_service.py           # CRUD 유스케이스
│           ├── infrastructure/     # ③ 인프라 계층
│           │   ├── models.py                 # Django ORM 모델
│           │   ├── repositories/             # Repository 구현체
│           │   └── migrations/               # DB 마이그레이션
│           └── presentation/       # ④ 표현 계층
│               ├── serializers.py            # DRF 입력 검증
│               └── views.py                  # APIView (CRUD)
│
├── frontend/               # React + TypeScript 프론트엔드
│   ├── Dockerfile
│   ├── src/
│   │   ├── types/post.ts           # 타입 정의
│   │   ├── api/postApi.ts          # API 호출 함수
│   │   ├── components/
│   │   │   ├── PostCard.tsx        # 목록 카드
│   │   │   └── PostForm.tsx        # 작성/수정 폼
│   │   └── pages/
│   │       ├── PostListPage.tsx    # GET /posts
│   │       ├── PostDetailPage.tsx  # GET /posts/:id
│   │       ├── CreatePostPage.tsx  # POST /posts
│   │       └── EditPostPage.tsx    # PUT /posts/:id
│   └── App.tsx                     # 라우팅
│
└── tasks/                  # 작업 관리
    ├── todo.md             # 할 일 체크리스트
    └── progress.md         # 완료 기록 로그
```

---

## 🔌 API 엔드포인트

| Method | URL | 설명 |
|--------|-----|------|
| GET | `/api/posts/` | 목록 조회 |
| POST | `/api/posts/` | 게시글 작성 |
| GET | `/api/posts/:id/` | 상세 조회 |
| PUT | `/api/posts/:id/` | 수정 |
| DELETE | `/api/posts/:id/` | 삭제 |

---

## 🛠 개발 환경 (Docker 없이)

```bash
# 백엔드
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# 프론트엔드
cd frontend
npm install
npm run dev
```

> 백엔드만 단독 실행 시 PostgreSQL이 필요합니다. `.env`의 DB 설정을 로컬 DB에 맞게 수정하세요.

---

## 🚨 보안 사고 발생 시

`SECURITY.md` 파일을 즉시 열어 해당 서비스 섹션을 따릅니다.
