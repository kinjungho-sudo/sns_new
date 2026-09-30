# 채널별 자료 전달 근거

공통 공개 자료 링크:

`https://uncovered-crate-996.notion.site/AI-3eb147a5e90f80bcbc73c5a9107e5060`

## 운영 방식

| 채널 | 자료 전달 |
|---|---|
| Instagram | 댓글 `자료`를 CreatorFlow가 감지해 DM으로 공개 링크 전송 |
| LinkedIn | 본문에 공개 링크 직접 제공 |
| 네이버 블로그 | 본문에 공개 링크 직접 제공 |
| 티스토리 | 본문에 공개 링크 직접 제공 |

## 공식 근거

- LinkedIn Comments API는 댓글 읽기·작성 기능을 제공한다: https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/comments-api
- LinkedIn Messages API는 승인 파트너 전용이고, 메시지는 구체적인 회원 동작과 명시적 전송 동의가 필요하며 자동·예약 이벤트는 회원 동작으로 인정하지 않는다: https://learn.microsoft.com/en-us/linkedin/shared/integrations/communications/messages
- NAVER 로그인 Open API가 안내하는 사용자 권한 API는 프로필, 카페 가입·글쓰기, 캘린더 일정 생성이며 블로그 댓글·쪽지 자동 발송은 포함하지 않는다: https://developers.naver.com/docs/login/api/api.md
- Tistory Open API는 댓글 관련 기능을 포함해 2024년 2월까지 순차 종료됐다: https://tistory.github.io/document-tistory-apis/

## 검수

1. Instagram 본문은 댓글 키워드 `자료`를 포함해야 한다.
2. LinkedIn·네이버 블로그·티스토리 본문은 공통 공개 Notion URL을 포함해야 한다.
3. 나머지 세 채널은 댓글을 달면 비공개 메시지를 보낸다고 약속하지 않는다.
4. 2일 주기 게시 때 네 채널을 모두 게시하고 네 개 공개 URL을 기록한다.
