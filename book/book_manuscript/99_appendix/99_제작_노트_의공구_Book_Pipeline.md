## 제작 노트: 의공구 Book Pipeline

| 항목 | 내용 |
|---|---|
| 프로젝트명 | 의공구 Book Pipeline |
| 개발 기간 | 2026.06.04 – 2026.06.06 |
| 원고 형식 | Markdown |
| 이미지 자산 | PNG / JPG assets |
| 메타데이터 | YAML |
| 언어 | Python / Bash |
| 빌드 엔진 | Pandoc |
| 작업 환경 | Codex / Antigravity IDE |
| 출력 형식 | DOCX / PDF / EPUB |
| 파이프라인 | Markdown + assets → Python build script → Pandoc → EPUB/PDF/DOCX |

이 책은 Markdown 원고와 이미지 assets를 기반으로 관리되었고, Pandoc을 통해 EPUB/PDF/DOCX 형식으로 빌드되었습니다. 일부 원고 정리와 빌드 파이프라인 구성에는 Codex의 도움을 받았습니다.

**게으른 방지송 쉑기는 결국 책마저 Codex로 빌드하였습니다.**
