/**
 * main.tsx — 앱 진입점 (Entry Point)
 *
 * React 앱을 HTML의 <div id="root"> 에 마운트합니다.
 * global.css를 여기서 임포트해 전체 페이지에 기본 스타일을 적용합니다.
 * StrictMode: 개발 중에만 활성화되며 잠재적 문제를 감지해 콘솔에 경고를 출력합니다.
 */
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './styles/global.css' // 전역 CSS 변수·리셋·공통 클래스
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
