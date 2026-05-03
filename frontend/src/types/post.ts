/**
 * post.ts — 게시글 관련 TypeScript 타입 정의
 *
 * 백엔드 API 응답과 프론트엔드 요청 데이터의 구조를 타입으로 명시합니다.
 * 타입을 한 곳에서 관리하면 API 변경 시 수정이 용이합니다.
 */

/**
 * 서버에서 받아오는 게시글 전체 데이터 구조.
 * GET /api/posts/, GET /api/posts/:id/ 응답에 사용됩니다.
 */
export interface Post {
  id: number
  title: string
  content: string
  author: string
  created_at: string  // ISO 8601 형식 (예: "2026-05-03T17:00:00+09:00")
  updated_at: string
}

/**
 * 게시글 작성 시 서버로 전송하는 데이터.
 * POST /api/posts/ 요청 바디에 사용됩니다.
 */
export interface CreatePostInput {
  title: string
  content: string
  author: string
}

/**
 * 게시글 수정 시 서버로 전송하는 데이터.
 * PUT /api/posts/:id/ 요청 바디에 사용됩니다.
 * 작성자(author)는 수정 불가이므로 포함하지 않습니다.
 */
export interface UpdatePostInput {
  title: string
  content: string
}
