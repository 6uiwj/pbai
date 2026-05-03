/**
 * PostDetailPage.tsx — 게시글 상세 페이지
 *
 * URL 파라미터(:id)로 게시글 번호를 받아 단일 게시글을 표시합니다.
 *
 * 동작 흐름:
 *  1. URL에서 id를 추출해 서버에서 게시글 데이터를 불러옵니다.
 *  2. 삭제 버튼 클릭 시 confirm으로 사용자에게 확인을 받습니다.
 *  3. 삭제 성공 시 목록 페이지로 이동합니다.
 */
import { useState, useEffect } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { postApi } from '../api/postApi'
import { Post } from '../types/post'
import styles from './PostDetailPage.module.css'

export default function PostDetailPage() {
  // URL의 :id 파라미터 추출 (예: /posts/3 → id = "3")
  const { id } = useParams<{ id: string }>()
  // 페이지 이동을 프로그래밍 방식으로 수행하는 함수
  const navigate = useNavigate()

  const [post, setPost] = useState<Post | null>(null)
  const [error, setError] = useState('')

  // id가 변경될 때마다 해당 게시글을 다시 불러옴
  useEffect(() => {
    if (!id) return
    postApi.getById(Number(id))
      .then(setPost)
      .catch(e => setError(e.message))
  }, [id])

  /** 삭제 처리 — 확인 다이얼로그 → API 호출 → 목록으로 이동 */
  const handleDelete = async () => {
    // 실수로 삭제하지 않도록 브라우저 confirm 창 표시
    if (!id || !window.confirm('정말 삭제하시겠습니까?\n이 작업은 되돌릴 수 없습니다.')) return
    try {
      await postApi.delete(Number(id))
      navigate('/posts') // 삭제 성공 → 목록 페이지로 이동
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : '삭제에 실패했습니다.')
    }
  }

  // 에러 상태: 에러 메시지 + 목록으로 돌아가기 링크
  if (error) {
    return (
      <div>
        <Link to="/posts" className="back-link">← 목록으로</Link>
        <p className="alert-error">{error}</p>
      </div>
    )
  }

  // 데이터 로딩 중
  if (!post) return <p className="loading">불러오는 중...</p>

  return (
    <div>
      {/* 목록으로 돌아가기 링크 */}
      <Link to="/posts" className="back-link">← 목록으로</Link>

      {/* 게시글 카드 */}
      <article className={styles.article}>

        {/* 제목 + 메타 정보 헤더 */}
        <div className={styles.articleHeader}>
          <h1 className={styles.title}>{post.title}</h1>
          <div className={styles.meta}>
            <span className={styles.author}>{post.author}</span>
            <span className={styles.dot} />
            <span>
              {new Date(post.created_at).toLocaleDateString('ko-KR', {
                year: 'numeric', month: 'long', day: 'numeric',
              })}
            </span>
            {/* 수정된 경우 수정 일시도 표시 */}
            {post.created_at !== post.updated_at && (
              <>
                <span className={styles.dot} />
                <span style={{ fontStyle: 'italic' }}>수정됨</span>
              </>
            )}
          </div>
        </div>

        {/* 본문 내용 — pre-wrap으로 줄바꿈 보존 */}
        <div className={styles.content}>{post.content}</div>

        {/* 수정·삭제 액션 버튼 */}
        <div className={styles.actions}>
          <Link to={`/posts/${post.id}/edit`}>
            <button className="btn btn-secondary btn-sm">수정</button>
          </Link>
          <button
            className="btn btn-danger btn-sm"
            onClick={handleDelete}
          >
            삭제
          </button>
        </div>

      </article>
    </div>
  )
}
