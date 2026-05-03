/**
 * PostListPage.tsx — 게시글 목록 페이지
 *
 * 앱 최초 진입 페이지(/)에서 /posts로 리다이렉트되어 표시됩니다.
 *
 * 동작 흐름:
 *  1. 컴포넌트 마운트 시 useEffect로 서버에서 게시글 목록을 불러옵니다.
 *  2. 로딩 중에는 아무것도 표시하지 않고, 에러 시 에러 메시지를 표시합니다.
 *  3. 게시글이 없으면 빈 상태(empty state) UI를 보여줍니다.
 *  4. 게시글이 있으면 PostCard 컴포넌트 목록을 렌더링합니다.
 */
import { useState, useEffect } from 'react'
import { postApi } from '../api/postApi'
import { Post } from '../types/post'
import PostCard from '../components/PostCard'
import styles from './PostListPage.module.css'

export default function PostListPage() {
  // 서버에서 불러온 게시글 목록
  const [posts, setPosts] = useState<Post[]>([])
  // API 호출 실패 시 에러 메시지
  const [error, setError] = useState('')

  // 컴포넌트가 화면에 나타날 때 한 번만 실행 (의존성 배열이 빈 배열)
  useEffect(() => {
    postApi.getAll()
      .then(setPosts)
      .catch(e => setError(e.message))
  }, [])

  return (
    <div>
      {/* 페이지 헤더 — 제목과 게시글 수 */}
      <div className={styles.pageHeader}>
        <h1 className={styles.pageTitle}>전체 게시글</h1>
        {posts.length > 0 && (
          <p className={styles.count}>총 {posts.length}개</p>
        )}
      </div>

      {/* 에러 메시지 */}
      {error && <p className="alert-error">{error}</p>}

      {/* 게시글이 없을 때 빈 상태 UI */}
      {!error && posts.length === 0 && (
        <div className={styles.empty}>
          <div className={styles.emptyIcon}>📭</div>
          <p className={styles.emptyText}>
            아직 게시글이 없습니다.<br />
            상단의 <strong>+ 글쓰기</strong> 버튼으로 첫 글을 작성해보세요!
          </p>
        </div>
      )}

      {/* 게시글 카드 목록 */}
      {posts.map(post => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  )
}
