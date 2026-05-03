# 할 일 목록 (todo.md)

> 작업 시작 시 이 파일을 확인합니다.
> 완료된 항목은 `[ ]` → `[x]`로 바꾸고, `progress.md`에 기록합니다.

---

## 🔥 현재 작업: 게시판 CRUD (Django + React/TS + Docker)

### Phase 1 — 백엔드 (Django + DRF + DDD 4-Layered)
- [ ] 1-1. docker-compose.yml + .env + Dockerfile 구성
- [ ] 1-2. Django 프로젝트 config (settings, urls, wsgi)
- [ ] 1-3. Domain Layer: Post 엔티티 + Repository 인터페이스
- [ ] 1-4. Infrastructure Layer: ORM 모델 + Repository 구현체 + 초기 마이그레이션
- [ ] 1-5. Application Layer: DTO + PostService (CRUD 유스케이스)
- [ ] 1-6. Presentation Layer: DRF Serializer + APIView + URL 라우팅

### Phase 2 — 프론트엔드 (React + TypeScript + Vite)
- [ ] 2-1. Vite 프로젝트 설정 (package.json, tsconfig, vite.config)
- [ ] 2-2. 타입 정의 + API 클라이언트
- [ ] 2-3. 공통 컴포넌트 (PostCard, PostForm)
- [ ] 2-4. 페이지 (목록 / 상세 / 작성 / 수정) + 라우팅

### Phase 3 — 통합 확인
- [ ] 3-1. docker-compose up 실행 확인
- [ ] 3-2. CRUD 전체 동작 확인

---

## 📋 백로그

- [ ] 로그인/인증 기능
- [ ] 댓글 기능
- [ ] 페이지네이션

---

## ✅ 완료됨

- [x] 작업 환경 초기 구축 (tasks/, SECURITY.md, README.md)

---

_마지막 업데이트: 2026-05-03_
