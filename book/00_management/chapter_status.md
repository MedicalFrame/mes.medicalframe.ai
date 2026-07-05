# 원고 상태표

기준일: 2026-06-07

이 문서는 현재 `book_manuscript/` 실파일과 `00_management/scripts/build_book.py`를 기준으로 작성했다.
이제 상태표의 기준은 과거 원본 폴더가 아니라 현재 책 원고 구조다.

## 상태 기준

| 상태 | 의미 |
|---|---|
| 본문 | 현재 책 본문에 포함되는 장 |
| frontmatter | 프롤로그/에필로그 같은 앞뒤글 |
| appendix | 부록 원고 |
| 관리문서 | 원고 본문이 아닌 운영/설명 문서 |

## 현재 책 구조 요약

| 구분 | 장 수 | 비고 |
|---|---:|---|
| 프롤로그 | 1 | `00_frontmatter` |
| Part 1. 왜 자꾸 모델을 만드는가 | 4 | |
| Part 2. 구조로 공부하다 | 8 | |
| Part 3. 사고를 구현하다 | 9 | |
| Part 4. 기록은 곧바로 데이터가 되지 않는다 | 5 | |
| Part 5. 약물은 점이 아니라 곡선이다 | 3 | |
| Part 6. AI 시대에 살아남는 것 | 4 | |
| 에필로그 | 1 | `00_frontmatter` |
| 부록 | 6 | 제작 노트 포함 |

## frontmatter

| 구분 | 파일 | 상태 | 메모 |
|---|---|---|---|
| 프롤로그 | `book_manuscript/00_frontmatter/00_프롤로그_의세계에_전생했다는_것_축약판.md` | frontmatter | 빌드용 축약판, 원본 파일 별도 보존 |
| 에필로그 | `book_manuscript/00_frontmatter/99_에필로그_두_세계를_오가는_마법진.md` | frontmatter | 책 마무리 |

## 본문

| 번호 | 제목 | 파일 | 상태 | 메모 |
|---:|---|---|---|
| 1 | 의대생이 공학을 놓지 않는 이유 | `book_manuscript/01_왜_자꾸_모델을_만드는가/01_의대생이_공학을_놓지_않는_이유.md` | 본문 |  |
| 2 | 공학적 사고란 무엇인가 | `book_manuscript/01_왜_자꾸_모델을_만드는가/02_공학적_사고란_무엇인가.md` | 본문 |  |
| 3 | 나는 왜 모델을 좋아하는가 | `book_manuscript/01_왜_자꾸_모델을_만드는가/03_나는_왜_모델을_좋아하는가.md` | 본문 |  |
| 4 | 의료를 구조화한다는 것 | `book_manuscript/01_왜_자꾸_모델을_만드는가/04_의료를_구조화한다는_것.md` | 본문 |  |
| 5 | 공부를 구조로 바라본다는 것 | `book_manuscript/02_구조로_공부하다/01_공부를_구조로_바라본다는_것.md` | 본문 | 브리지 장 유지 권장 |
| 6 | 암기와 이해는 다른 층위 | `book_manuscript/02_구조로_공부하다/02_암기와_이해는_다른_층위.md` | 본문 |  |
| 7 | 실습은 사고의 전환점 | `book_manuscript/02_구조로_공부하다/03_실습은_사고의_전환점.md` | 본문 | 현행 유지 권장, 추후 보강은 선택 |
| 8 | 구조화의 힘 | `book_manuscript/02_구조로_공부하다/04_구조화의_힘.md` | 본문 |  |
| 9 | Anki는 구조 관리 도구 | `book_manuscript/02_구조로_공부하다/05_Anki는_구조_관리_도구.md` | 본문 |  |
| 10 | AI를 도구로 쓰는 공부 | `book_manuscript/02_구조로_공부하다/06_AI를_도구로_쓰는_공부.md` | 본문 |  |
| 11 | 좋은 질문은 무엇일까 | `book_manuscript/02_구조로_공부하다/07_좋은_질문은_무엇일까.md` | 본문 |  |
| 12 | 가르친다는 것은 구조를 다시 짓는 일이다 | `book_manuscript/02_구조로_공부하다/08_가르친다는_것은_구조를_다시_짓는_일이다.md` | 본문 |  |
| 13 | 사고를 구현한다는 것 | `book_manuscript/03_사고를_구현하다/01_사고를_구현한다는_것.md` | 본문 | 파트 도입 장으로 유지 권장 |
| 14 | 구체화와 자동화 | `book_manuscript/03_사고를_구현하다/02_구체화와_자동화.md` | 본문 |  |
| 15 | 집이 살아있다, HAOS | `book_manuscript/03_사고를_구현하다/03_집이_살아있다_HAOS.md` | 본문 |  |
| 16 | 작업용 개인 클라우드, Jisong Cloud 6.0 | `book_manuscript/03_사고를_구현하다/04_작업용_개인_클라우드_Jisong_Cloud_6_0.md` | 본문 |  |
| 17 | OpenClaw, 그리고 춘식이 | `book_manuscript/03_사고를_구현하다/05_OpenClaw_그리고_춘식이.md` | 본문 |  |
| 18 | 모델링과 확률적 판단 | `book_manuscript/03_사고를_구현하다/06_모델링과_확률적_판단.md` | 본문 |  |
| 19 | 감각의 객관화, VoiceGrape | `book_manuscript/03_사고를_구현하다/07_감각의_객관화_VoiceGrape.md` | 본문 |  |
| 20 | 상태를 모델로, NeuroFrame | `book_manuscript/03_사고를_구현하다/08_상태를_모델로_NeuroFrame.md` | 본문 |  |
| 21 | CDSS prototype, EstroFrame | `book_manuscript/03_사고를_구현하다/09_CDSS_prototype_EstroFrame.md` | 본문 |  |
| 22 | 감각에서 수치로, 수치에서 예측으로 | `book_manuscript/04_기록은_곧바로_데이터가_되지_않는다/01_감각에서_수치로_수치에서_예측으로.md` | 본문 |  |
| 23 | 의료 텍스트는 왜 바로 데이터가 되지 않는가 | `book_manuscript/04_기록은_곧바로_데이터가_되지_않는다/02_의료_텍스트는_왜_바로_데이터가_되지_않는가.md` | 본문 |  |
| 24 | 로컬 기반 EMR 파싱, CleanText | `book_manuscript/04_기록은_곧바로_데이터가_되지_않는다/03_로컬_기반_EMR_파싱_CleanText.md` | 본문 |  |
| 25 | EMR 연구용 파싱, CleanEMR | `book_manuscript/04_기록은_곧바로_데이터가_되지_않는다/04_EMR_연구용_파싱_CleanEMR.md` | 본문 |  |
| 26 | 머신러닝 기반 당뇨 약물 추천, DiaFrame | `book_manuscript/04_기록은_곧바로_데이터가_되지_않는다/05_머신러닝_기반_당뇨_약물_추천_DiaFrame.md` | 본문 |  |
| 27 | 다학제 약제 PK 분석, PharmaFrame | `book_manuscript/05_약물은_점이_아니라_곡선이다/01_다학제_약제_PK_분석_PharmaFrame.md` | 본문 |  |
| 28 | 수술 전 약을 끊는다는 것 | `book_manuscript/05_약물은_점이_아니라_곡선이다/02_수술_전_약을_끊는다는_것.md` | 본문 |  |
| 29 | 모델은 처음부터 맞지 않는다 | `book_manuscript/05_약물은_점이_아니라_곡선이다/03_모델은_처음부터_맞지_않는다.md` | 본문 |  |
| 30 | AI에게 일을 맡긴다는 건, 좋은 상사가 되는 일이다 | `book_manuscript/06_AI_시대에도_남는_것/01_AI에게 일을 맡긴다는 건, 좋은 상사가 되는 일이다.md` | 본문 |  |
| 31 | 판단은 설명될 때 완성된다 | `book_manuscript/06_AI_시대에도_남는_것/02_판단은_설명될_때_완성된다.md` | 본문 | 브리지 장 유지 권장, 대주제 앵커 역할 |
| 32 | 어떤 의사가 될 것인가 | `book_manuscript/06_AI_시대에도_남는_것/03_어떤_의사가_될_것인가.md` | 본문 |  |
| 33 | 임상 디지털 트윈 설계자 | `book_manuscript/06_AI_시대에도_남는_것/04_임상_디지털_트윈_설계자.md` | 본문 |  |

## 부록

| 구분 | 파일 | 상태 | 메모 |
|---|---|---|---|
| 부록 1 | `book_manuscript/99_appendix/01_하루_30분_1년_반_JLPT_N1까지.md` | appendix | 학습 구조화 사례 |
| 부록 2 | `book_manuscript/99_appendix/02_Obsidian_PKM_연결을_관리하기.md` | appendix | PKM/연결 관리 |
| 부록 3 | `book_manuscript/99_appendix/03_도메인을_산다는_것.md` | appendix | 개인 인프라 외전 |
| 부록 4 | `book_manuscript/99_appendix/04_사고_보조_장치_Antigravity_IDE.md` | appendix | 작업 도구 외전 |
| 부록 5 | `book_manuscript/99_appendix/05_사진도_구조를_보는_일이다.md` | appendix | 사진/구조화 외전 |
| 제작 노트 | `book_manuscript/99_appendix/99_제작_노트_의공구_Book_Pipeline.md` | appendix | 책 제작 메모 |

## 관리 메모

- 현재 합본 원고는 `book_manuscript/book.md`다.
- 합본 생성 기준은 `00_management/scripts/build_book.py`다.
- 현재 구조 기준으로는 과거 상태표에 있던 “30장 누락” 이슈는 더 이상 유효하지 않다.
