# Case-Mismatch Handoff Plan

기준일: 2026-06-07

## 대상

현재 source manuscript는 아래 3개 이미지를 소문자 `.png`로 참조하지만, 실제 디스크 파일은 대문자 `.PNG`다.

| source ref | actual file |
|---|---|
| `assets/images/cleanemr_04.png` | `assets/images/cleanemr_04.PNG` |
| `assets/images/clinical_digital_twin_02.png` | `assets/images/clinical_digital_twin_02.PNG` |
| `assets/images/diaframe_02.png` | `assets/images/diaframe_02.PNG` |

## 현재 영향

- macOS 기본 환경에서는 대개 문제 없이 보일 수 있다.
- case-sensitive filesystem, 외부 패키징, 일부 자동 링크 재연결 환경에서는 깨질 수 있다.
- InDesign handoff 관점에서는 **실제 존재 파일은 있지만 링크 안정성이 부족한 상태**다.

## 권장 처리 순서

### 1안. handoff package 기준으로만 실제 파일명 사용

권장도: 높음

방법:

- source manuscript는 당장 수정하지 않는다.
- `output/indesign_handoff/image_manifest.csv` 기준으로 실제 디스크 파일명을 사용한다.
- InDesign 반입자는 `image_manifest.csv`의 `current_path`를 기준으로 링크한다.

장점:

- 원고 파일을 건드리지 않는다.
- 현재 규칙의 “source manuscript 파일명 보존”에 부합한다.
- handoff 직전 운영 위험을 가장 적게 늘린다.

단점:

- source manuscript와 actual disk path가 계속 어긋난다.
- 이후 자동화 단계에서 다시 같은 이슈가 반복될 수 있다.

### 2안. source manuscript 참조를 실제 `.PNG`에 맞춘다

권장도: 중간

방법:

- 해당 3개 이미지 ref만 원고에서 `.PNG`로 수정한다.

장점:

- source manuscript와 disk state가 일치한다.
- case-sensitive 환경에서도 안정적이다.

단점:

- source manuscript를 직접 수정한다.
- 현재는 handoff 준비 단계이므로, 변경 범위를 더 늘리게 된다.

### 3안. 실제 파일명을 모두 소문자 `.png`로 통일한다

권장도: 중간 이하

방법:

- asset 파일명을 rename하고 참조를 같이 갱신한다.

장점:

- 장기적으로 가장 깔끔하다.

단점:

- 링크 영향 범위가 커진다.
- 지금 단계에서는 불필요하게 리스크가 커진다.

## 현재 권장 결론

현 시점 handoff 준비 기준으로는 **1안**이 가장 적절하다.

- 즉, source manuscript는 유지
- handoff package와 InDesign 링크 작업에서는 `image_manifest.csv`의 실제 파일명 기준 사용

## handoff 담당자에게 전달할 문구

- `cleanemr_04`, `clinical_digital_twin_02`, `diaframe_02`는 source manuscript ref와 actual file extension case가 다릅니다.
- InDesign 링크는 `output/indesign_handoff/image_manifest.csv`의 `current_path`를 기준으로 연결하십시오.
