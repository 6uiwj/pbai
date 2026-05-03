/**
 * PostCard.tsx — 게시글 목록 카드 컴포넌트
 *
 * 게시글 하나를 카드 형태로 표시합니다.
 * 카드 전체가 링크로 감싸져 있어 어디를 클릭해도 상세 페이지로 이동합니다.
 * 호버 시 카드가 살짝 떠오르는 애니메이션이 적용됩니다.
 */
import { Link } from 'react-router-dom'
import { Post } from '../types/post'
import styles from './PostCard.module.css'

interface Props {
  post: Post // 표시할 게시글 데이터
}

export default function PostCard({ post }: Props) {
  // 날짜를 "2026. 5. 3." 형식으로 변환
  const formattedDate = new Date(post.created_at).toLocaleDateString('ko-KR')

  return (
    // 카드 전체를 Link로 감싸 클릭 영역 최대화
    <Link to={`/posts/${post.id}`} className={styles.link}>
      <article className={styles.card}>

        {/* 제목 + 메타 정보 */}
        <div className={styles.body}>
          <h3 className={styles.title}>{post.title}</h3>
          <div className={styles.meta}>
            <span>{post.author}</span>
            {/* 구분점 (·) */}
            <span className={styles.dot} />
            <span>{formattedDate}</span>
          </div>
        </div>

        {/* 우측 화살표 — 호버 시 오른쪽으로 이동 */}
        <span className={styles.arrow}>→</span>

      </article>
    </Link>
  )
}
