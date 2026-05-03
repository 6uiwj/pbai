/**
 * CreatePostPage.tsx — 게시글 작성 페이지
 *
 * PostForm 컴포넌트(create 모드)를 사용해 새 게시글을 등록합니다.
 *
 * 동작 흐름:
 *  1. 사용자가 폼을 작성하고 제출하면 handleSubmit이 호출됩니다.
 *  2. postApi.create()로 서버에 데이터를 전송합니다.
 *  3. 성공 시 생성된 게시글의 상세 페이지로 이동합니다.
 *  4. 실패 시 에러 메시지를 표시하고 폼을 다시 활성화합니다.
 */
import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { postApi } from '../api/postApi'
import { CreatePostInput } from '../types/post'
import PostForm from '../components/PostForm'
import styles from './CreatePostPage.module.css'

export default function CreatePostPage() {
  const navigate = useNavigate()
  // 서버 요청 중 폼 비활성화 여부
  const [loading, setLoading] = useState(false)
  // 에러 메시지
  const [error, setError] = useState('')

  /**
   * 폼 제출 처리
   * PostForm 컴포넌트로부터 입력값을 받아 API를 호출합니다.
   */
  const handleSubmit = async (data: CreatePostInput) => {
    setLoading(true)
    setError('')
    try {
      const post = await postApi.create(data)
      // 생성 성공 → 새 게시글 상세 페이지로 이동
      navigate(`/posts/${post.id}`)
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : '등록에 실패했습니다.')
      setLoading(false) // 실패 시에만 로딩 해제 (성공 시 페이지 이동으로 자동 해제)
    }
  }

  return (
    <div>
      <Link to="/posts" className="back-link">← 목록으로</Link>

      <h1 className={styles.pageTitle}>새 글 작성</h1>

      {/* 에러 메시지 */}
      {error && <p className="alert-error" style={{ marginBottom: '16px' }}>{error}</p>}

      {/* 폼을 카드 안에 감싸서 시각적으로 구분 */}
      <div className={styles.card}>
        <PostForm
          mode="create"
          onSubmit={handleSubmit}
          loading={loading}
        />
      </div>
    </div>
  )
}
