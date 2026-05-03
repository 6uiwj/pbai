/**
 * EditPostPage.tsx — 게시글 수정 페이지
 *
 * URL 파라미터(:id)로 기존 게시글을 불러와 수정합니다.
 * PostForm 컴포넌트(edit 모드)에 기존 값을 초기값으로 전달합니다.
 *
 * 동작 흐름:
 *  1. 마운트 시 현재 게시글 데이터를 서버에서 불러옵니다.
 *  2. 로딩 완료 후 PostForm에 기존 제목·내용을 초기값으로 설정합니다.
 *  3. 폼 제출 시 수정된 데이터를 서버에 전송합니다.
 *  4. 성공 시 상세 페이지로 이동합니다.
 */
import { useState, useEffect } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { postApi } from '../api/postApi'
import { Post, UpdatePostInput } from '../types/post'
import PostForm from '../components/PostForm'
import styles from './EditPostPage.module.css'

export default function EditPostPage() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()

  // 수정 전 원본 게시글 데이터 (초기값 설정에 사용)
  const [post, setPost] = useState<Post | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // 페이지 진입 시 기존 게시글 데이터 불러오기
  useEffect(() => {
    if (!id) return
    postApi.getById(Number(id))
      .then(setPost)
      .catch(e => setError(e.message))
  }, [id])

  /**
   * 폼 제출 처리 — 수정된 제목·내용을 서버에 전송
   */
  const handleSubmit = async (data: UpdatePostInput) => {
    if (!id) return
    setLoading(true)
    setError('')
    try {
      await postApi.update(Number(id), data)
      navigate(`/posts/${id}`) // 수정 성공 → 상세 페이지로 이동
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : '수정에 실패했습니다.')
      setLoading(false)
    }
  }

  // 에러 상태
  if (error) {
    return (
      <div>
        <Link to="/posts" className="back-link">← 목록으로</Link>
        <p className="alert-error">{error}</p>
      </div>
    )
  }

  // 원본 데이터 로딩 중
  if (!post) return <p className="loading">불러오는 중...</p>

  return (
    <div>
      <Link to={`/posts/${post.id}`} className="back-link">← 상세로</Link>

      <h1 className={styles.pageTitle}>글 수정</h1>

      {/* 폼을 카드 안에 감싸서 시각적으로 구분 */}
      <div className={styles.card}>
        <PostForm
          mode="edit"
          initialTitle={post.title}    // 기존 제목을 초기값으로 전달
          initialContent={post.content} // 기존 내용을 초기값으로 전달
          onSubmit={handleSubmit}
          loading={loading}
        />
      </div>
    </div>
  )
}
