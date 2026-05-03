/**
 * App.tsx — 앱 루트 컴포넌트
 *
 * 역할:
 *  1. BrowserRouter로 클라이언트 사이드 라우팅 활성화
 *  2. 상단 고정 헤더(로고 + 글쓰기 버튼) 렌더링
 *  3. Routes로 URL 경로별 페이지 컴포넌트 매핑
 *
 * 라우팅 구조:
 *  /            → /posts 로 자동 리다이렉트
 *  /posts       → 게시글 목록
 *  /posts/new   → 게시글 작성
 *  /posts/:id   → 게시글 상세
 *  /posts/:id/edit → 게시글 수정
 */
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom'
import styles from './App.module.css'
import PostListPage from './pages/PostListPage'
import PostDetailPage from './pages/PostDetailPage'
import CreatePostPage from './pages/CreatePostPage'
import EditPostPage from './pages/EditPostPage'

function App() {
  return (
    <BrowserRouter>
      <div className={styles.layout}>

        {/* ── 상단 고정 네비게이션 바 ── */}
        <header className={styles.header}>
          <div className={styles.headerInner}>
            {/* 로고 — 클릭 시 목록 페이지로 이동 */}
            <Link to="/posts" className={styles.logo}>
              📋 게시판
            </Link>

            {/* 글쓰기 버튼 — 헤더에 항상 표시 */}
            <Link to="/posts/new">
              <button className="btn btn-primary btn-sm">+ 글쓰기</button>
            </Link>
          </div>
        </header>

        {/* ── 페이지 콘텐츠 영역 ── */}
        <main className={styles.main}>
          <Routes>
            {/* 루트 경로는 목록으로 리다이렉트 */}
            <Route path="/" element={<Navigate to="/posts" replace />} />
            <Route path="/posts" element={<PostListPage />} />
            <Route path="/posts/new" element={<CreatePostPage />} />
            <Route path="/posts/:id" element={<PostDetailPage />} />
            <Route path="/posts/:id/edit" element={<EditPostPage />} />
          </Routes>
        </main>

      </div>
    </BrowserRouter>
  )
}

export default App
