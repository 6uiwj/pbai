/**
 * PostForm.tsx — 게시글 작성/수정 공용 폼 컴포넌트
 *
 * mode prop으로 '작성(create)' 과 '수정(edit)' 두 가지 모드를 지원합니다.
 *
 * - create 모드: 제목·작성자·내용 입력. 작성자 필드 포함.
 * - edit 모드: 제목·내용만 수정 가능. initialTitle/initialContent로 초기값 설정.
 *
 * 제출 시 상위 컴포넌트의 onSubmit 콜백을 호출합니다.
 * 서버 통신은 이 컴포넌트의 책임이 아니며, 페이지 컴포넌트가 처리합니다.
 */
import { useState } from 'react'
import { CreatePostInput, UpdatePostInput } from '../types/post'
import styles from './PostForm.module.css'

/** create 모드용 props */
type CreateProps = {
  mode: 'create'
  onSubmit: (data: CreatePostInput) => void
  loading?: boolean // 서버 요청 중 버튼 비활성화 여부
}

/** edit 모드용 props */
type EditProps = {
  mode: 'edit'
  initialTitle: string   // 수정 전 기존 제목
  initialContent: string // 수정 전 기존 내용
  onSubmit: (data: UpdatePostInput) => void
  loading?: boolean
}

type Props = CreateProps | EditProps

export default function PostForm(props: Props) {
  // 입력 상태 초기값: edit 모드면 기존 값, create 모드면 빈 문자열
  const [title, setTitle] = useState(props.mode === 'edit' ? props.initialTitle : '')
  const [content, setContent] = useState(props.mode === 'edit' ? props.initialContent : '')
  const [author, setAuthor] = useState('')

  /** 폼 제출 처리 — 브라우저 기본 동작을 막고 상위 콜백 호출 */
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault() // 페이지 새로고침 방지
    if (props.mode === 'create') {
      props.onSubmit({ title, content, author })
    } else {
      props.onSubmit({ title, content })
    }
  }

  return (
    <form onSubmit={handleSubmit} className={styles.form}>

      {/* 제목 입력 */}
      <div className="form-group">
        <label htmlFor="title" className="form-label">제목</label>
        <input
          id="title"
          type="text"
          className="form-input"
          value={title}
          onChange={e => setTitle(e.target.value)}
          placeholder="제목을 입력하세요"
          required
        />
      </div>

      {/* 작성자 입력 — create 모드에서만 표시 */}
      {props.mode === 'create' && (
        <div className="form-group">
          <label htmlFor="author" className="form-label">작성자</label>
          <input
            id="author"
            type="text"
            className="form-input"
            value={author}
            onChange={e => setAuthor(e.target.value)}
            placeholder="이름을 입력하세요"
            required
          />
        </div>
      )}

      {/* 내용 입력 */}
      <div className="form-group">
        <label htmlFor="content" className="form-label">내용</label>
        <textarea
          id="content"
          className="form-textarea"
          value={content}
          onChange={e => setContent(e.target.value)}
          placeholder="내용을 입력하세요"
          rows={10}
          required
        />
      </div>

      {/* 제출 버튼 — 요청 중에는 비활성화 */}
      <div className={styles.submitRow}>
        <button
          type="submit"
          className="btn btn-primary"
          disabled={props.loading}
        >
          {props.loading
            ? '처리 중...'
            : props.mode === 'create' ? '등록하기' : '수정 완료'
          }
        </button>
      </div>

    </form>
  )
}
