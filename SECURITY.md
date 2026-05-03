# SECURITY.md — 비상 매뉴얼

> **이 파일은 키 노출 등 보안 사고 발생 시 즉시 꺼내보는 매뉴얼입니다.**
> 평소에는 건드리지 않습니다.

---

## 🚨 키 노출 의심 — 즉시 대응 순서

> Claude가 **"🚨 키 노출 의심"** 경고를 띄우면 아래 순서대로 진행합니다.

```
1. 침착하게 — 지금 당장 할 수 있는 게 있습니다.
2. 노출된 키가 어떤 서비스인지 확인합니다.
3. 아래 해당 서비스 섹션으로 이동합니다.
4. 폐기 → 재발급 → 환경변수 교체 순서로 진행합니다.
5. 사용 이력을 확인합니다.
```

---

## 🔑 서비스별 긴급 대응

### OpenRouter API 키 (`sk-or-v1-...`)

| 단계 | 행동 | 주소 |
|------|------|------|
| 1. 폐기 | 대시보드 → API Keys → 해당 키 삭제 | https://openrouter.ai/keys |
| 2. 재발급 | 같은 페이지에서 새 키 생성 | — |
| 3. 교체 | `.env` 파일의 `OPENROUTER_API_KEY=` 값 교체 | 로컬 `.env` |
| 4. 이력 확인 | Usage 탭에서 비정상 호출 확인 | https://openrouter.ai/activity |

### Oracle Cloud SSH 키 (`~/.ssh/oracle-server.key`)

| 단계 | 행동 |
|------|------|
| 1. 서버 접근 차단 | Oracle 콘솔 → Compute → Instance → 해당 인스턴스 → Security List에서 내 IP 외 차단 |
| 2. 키 교체 | 새 키 쌍 생성: `ssh-keygen -t ed25519 -f ~/.ssh/oracle-server-new.key` |
| 3. 공개키 등록 | Oracle 콘솔 → Instance → Add SSH Key → 새 공개키 붙여넣기 |
| 4. 구키 삭제 | Oracle 콘솔에서 구 공개키 제거, 로컬 `~/.ssh/oracle-server.key` 삭제 |
| 5. SSH config 수정 | `~/.ssh/config`의 IdentityFile 경로를 새 키로 교체 |
| 6. 접속 로그 확인 | 서버: `sudo journalctl -u sshd --since "1 hour ago"` |

### WordPress / DB 비밀번호

| 단계 | 행동 |
|------|------|
| 1. DB 비밀번호 변경 | phpMyAdmin 또는 `mysql -u root -p` → `ALTER USER '유저'@'localhost' IDENTIFIED BY '새비번';` |
| 2. wp-config 교체 | `wp-config.php`의 `DB_PASSWORD` 값 교체 |
| 3. 관리자 비밀번호 변경 | WP 대시보드 → 사용자 → 프로필 → 비밀번호 재설정 |
| 4. 세션 무효화 | WP 대시보드 → 사용자 → 모든 기기에서 로그아웃 |
| 5. 접속 로그 확인 | 호스팅 패널 → 접속 로그 or `access.log` 확인 |

---

## 📋 키 노출 체크리스트

노출 사고 처리 후 아래를 모두 확인합니다:

- [ ] 노출된 키가 완전히 폐기되었는가?
- [ ] 새 키가 정상 동작하는가?
- [ ] `.env` 파일만 키를 갖고 있는가? (코드에 하드코딩 없음)
- [ ] `.env`가 `.gitignore`에 등록되어 있는가?
- [ ] git 히스토리에 키가 남아있지 않은가? (`git log -S "노출된키"`)
- [ ] 비정상 사용 이력이 없는가?
- [ ] 필요 시 관련 인원에게 공유했는가?

---

## 🛡️ 평소 예방 수칙

```bash
# .gitignore 필수 항목 확인
.env
*.key
*.pem
id_rsa
credentials.json
```

```bash
# 커밋 전 키 포함 여부 검색
git diff --cached | grep -E "(sk-|password|secret|key)" 
```

- 키는 항상 환경변수로만 참조 (`os.environ.get("KEY_NAME")`)
- 키를 터미널에 직접 출력하지 않기
- 로그 파일에 키가 찍히지 않도록 주의

---

_마지막 검토: 2026-05-03 | 다음 검토 예정: 분기 1회_
