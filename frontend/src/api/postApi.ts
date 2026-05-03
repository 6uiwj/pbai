/**
 * postApi.ts — 게시글 API 호출 모듈
 *
 * 백엔드 REST API와 통신하는 함수들을 모아둔 파일입니다.
 * fetch API를 사용하며, 에러 발생 시 Error 객체를 throw 합니다.
 *
 * BASE URL은 환경변수 VITE_API_URL에서 읽습니다.
 * 환경변수가 없으면 로컬 개발 주소(localhost:8000)를 기본값으로 사용합니다.
 */
import { Post, CreatePostInput, UpdatePostInput } from '../types/post'

/** 백엔드 서버 주소 (예: http://localhost:8000) */
const BASE = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

export const postApi = {
  /**
   * 모든 게시글 목록을 가져옵니다.
   * GET /api/posts/
   * @returns Post 배열 (최신순 정렬은 백엔드에서 처리)
   */
  getAll: async (): Promise<Post[]> => {
    const res = await fetch(`${BASE}/api/posts/`)
    if (!res.ok) throw new Error('목록을 불러오지 못했습니다.')
    return res.json()
  },

  /**
   * 특정 게시글 하나를 가져옵니다.
   * GET /api/posts/:id/
   * @param id 게시글 고유 번호
   */
  getById: async (id: number): Promise<Post> => {
    const res = await fetch(`${BASE}/api/posts/${id}/`)
    if (!res.ok) throw new Error('게시글을 찾을 수 없습니다.')
    return res.json()
  },

  /**
   * 새 게시글을 작성합니다.
   * POST /api/posts/
   * @param data 제목·내용·작성자
   * @returns 서버에서 생성된 게시글 (id, created_at 포함)
   */
  create: async (data: CreatePostInput): Promise<Post> => {
    const res = await fetch(`${BASE}/api/posts/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error('게시글 등록에 실패했습니다.')
    return res.json()
  },

  /**
   * 기존 게시글을 수정합니다.
   * PUT /api/posts/:id/
   * @param id 수정할 게시글 번호
   * @param data 새 제목·내용
   */
  update: async (id: number, data: UpdatePostInput): Promise<Post> => {
    const res = await fetch(`${BASE}/api/posts/${id}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error('게시글 수정에 실패했습니다.')
    return res.json()
  },

  /**
   * 게시글을 삭제합니다.
   * DELETE /api/posts/:id/
   * 성공 시 서버는 204 No Content를 반환하므로 반환값이 없습니다.
   */
  delete: async (id: number): Promise<void> => {
    const res = await fetch(`${BASE}/api/posts/${id}/`, { method: 'DELETE' })
    if (!res.ok) throw new Error('게시글 삭제에 실패했습니다.')
  },
}
