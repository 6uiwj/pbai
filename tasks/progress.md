# 작업 기록 (progress.md)

> 작업 종료 시 아래에 **추가**만 합니다. 기존 항목은 수정하지 않습니다.
> 형식: `[날짜] 작업 내용 — 결과/메모`

---

## 기록 로그

### 2026-05-03
- [2026-05-03] 작업 환경 초기 구축 — `tasks/`, `SECURITY.md`, `README.md` 생성 완료
- [2026-05-03] 게시판 CRUD 구현 완료
  - 백엔드: Django 5 + DRF + DDD 4-Layered (domain/application/infrastructure/presentation)
  - 인프라: PostgreSQL + docker-compose (db healthcheck 포함)
  - 프론트엔드: React 18 + TypeScript + Vite + react-router-dom
  - API: GET/POST /api/posts/, GET/PUT/DELETE /api/posts/:id/
  - 주의: docker-compose up --build 로 실행, .env 파일 필요

---

_이 파일은 append-only입니다. 위쪽 항목을 절대 지우거나 수정하지 마세요._
