# MES MedicalFrame Site

Static distribution site for **의세계에 전생한 공학자는 자꾸 모델을 만든다**.

이 저장소는 이제 배포 사이트와 책 제작 소스를 함께 관리합니다.

## Repository layout

- `index.html`, `styles.css`: 공개 배포 사이트
- `assets/`: 사이트 표지 이미지
- `downloads/MESbook.pdf`: 사이트에서 내려받는 최신 PDF
- `book/`: MESbook 원천 원고, 이미지 자산, 빌드 스크립트, 출력물

`book/`은 기존 `MESbook` 저장소의 살아있는 제작 소스를 흡수한 영역입니다. 오래된 `legacy/`, Git 기록 캐시, 사용하지 않는 font 묶음은 포함하지 않습니다.

## Book pipeline

```bash
cd book
python3 00_management/scripts/build_book.py
bash 00_management/scripts/build_all.sh
```

`build_all.sh`는 Pandoc과 Microsoft Word PDF 내보내기에 의존합니다. 빌드 후 공개 PDF를 갱신하려면 `book/output/MESbook.pdf`를 `downloads/MESbook.pdf`로 복사합니다.

## Local preview

```bash
python3 -m http.server 4173
```

## Deployment

- Target domain: `mes.medicalframe.ai`
- GitHub Pages custom domain file: `CNAME`
- PDF asset: `downloads/MESbook.pdf`
- Book source and generated manuscript: `book/`

See `DEPLOYMENT.md` for DNS instructions.
