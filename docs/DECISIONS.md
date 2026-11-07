# 결정 이력(Decision Log)

표기·구조·범위에 관한 결정을 시간순으로 기록한다. 기존 항목은 고치지 않는다.
결정을 바꿀 때는 새 번호를 추가하고, 바뀐 항목에 "→ D-000으로 대체"라고 표시한다.

- 결정 주체: **편저자** = 박지민의 직접 지시, **검증** = 출처 확인 결과 반영, **AI 제안·편저자 승인**
- 날짜는 한국 시간 기준

## 1. 범위와 구조

| 번호 | 날짜 | 결정 | 주체 · 근거 |
|---|---|---|---|
| D-001 | 2026-11-07 | 영→한 방향 용어집으로 시작한다. 각국 연맹(NSO)의 고유 명칭은 제외한다 | 편저자 |
| D-002 | 2026-11-07 | 원자료는 BP미디어 용어집(bpmedia.net/glossary) 공개 API에서 추출한다 | 편저자 |
| D-003 | 2026-11-07 | 종교계 국제 스카우트 기구(IUMS 등)는 모두 제외한다 | 편저자 |
| D-004 | 2026-11-07 | 한국스카우트연맹에는 공식 용어 표준이 없다. 이 데이터셋은 "제안 기준"으로 둔다. 다만 연맹 규정이 정한 명칭은 공식 명칭으로 따른다 | 편저자 · 검증(지도자·포상·진보과정·제복장구·Youth Hero상 규정) |
| D-005 | 2026-11-07 | `editorial_choice`는 "편저자 판단, 주로 가장 일반적인 용례"를 뜻한다 | 편저자 |
| D-006 | 2026-11-07 | 원자료 추출 시 정의에 "회원국"이 있는 항목을 지우는 필터가 핵심 개념 23개를 잘못 제외했다. 이를 복원했다 | 검증(AI 오류 정정) |
| D-007 | 2026-11-07 | `term_id`는 첫 공개판(v1.0.0)에서 영문 알파벳순으로 매기고, 이후에는 영구 번호로 고정한다 | 편저자 |
| D-008 | 2026-11-07 | 영문 이형 표기 열 `term_en_variant`를 둔다. 약어·옛 영문 명칭은 여기에 쓰고 표제어 괄호에 두지 않는다 | 편저자 |
| D-009 | 2026-11-07 | 표제어 앞의 정관사 "The"를 뺀다(예: Scout Method). 원래 표기는 영문 이형 표기에 둔다 | 편저자 지적 |
| D-010 | 2026-11-07 | 국내에서 영문 그대로 쓰는 용어는 `term_ko`에 영문을 그대로 쓴다 | 편저자 |
| D-011 | 2026-11-07 | `source_status`를 cited · not_required · compiler 세 가지로 둔다 | AI 제안·편저자 승인 |
| D-012 | 2026-11-07 | Zenodo DOI 발급: 대표 10.5281/zenodo.24032806, v1.0.0 10.5281/zenodo.24032807. 라이선스 CC BY 4.0 | 검증 |
| D-013 | 2026-11-07 | v1.0.1 발행(버전 DOI 10.5281/zenodo.24032958). AI 작업 규칙(AGENTS.md)·결정 이력·검증 스크립트 추가 | 편저자 |

## 2. 국문 표기

| 번호 | 영문 | 국문(결정) | 이형·참고 | 주체 · 근거 |
|---|---|---|---|---|
| D-101 | World Association of Girl Guides and Girl Scouts | 세계걸스카우트연맹 | "세계걸가이드·걸스카우트" 표현 사용 안 함 | 편저자 |
| D-102 | Personal Progression | 진보과정 | 진보 제도(이형) | 편저자 · 진보과정 규정 제1조 |
| D-103 | World Scout Committee Member | 세계스카우트이사 | 세계이사 | 편저자 · 온라인 용례(데일리안 2021) |
| D-104 | Chairperson of the World Scout Committee | 세계스카우트이사회 의장 | 이사회 대표 직위는 "의장" | 편저자 |
| D-105 | Korea National Jamboree | 한국잼버리 | 스카우트 내부·보도자료의 일반 용례 | 편저자 · 검증 |
| D-106 | Regional Director | 지역 사무처장 | 지역사무국장(초안, 이형) | 편저자 |
| D-107 | Regional Support Centre | 지역사무처 | 옛 영문 Regional Office | 편저자(사무처장과 짝) |
| D-108 | World Scout Bureau | 세계사무국 | 세계스카우트사무국(이형) | 편저자(사무총장과 짝) · 연맹 보도자료 "세계사무국"(2005) |
| D-109 | Global Support Centre | 세계사무국 본부 | 옛 영문 Central Office | AI 제안·편저자 승인(WSB 전체와 구분) |
| D-110 | Youth Advisor to the World Scout Committee | 세계청년이사 | "청소년자문위원"은 실제 용례 없음 → 삭제 | 편저자 |
| D-111 | Youth Advisor to the Regional Scout Committee | 지역청년이사 | | AI 제안(세계청년이사와 형식 통일) |
| D-112 | World Scout Foundation | 세계스카우트지원재단 | 세계스카우트재단(이형) | 편저자 · 연맹 연혁 "세계스카우트지원재단회의"(2008) |
| D-113 | Safe from Harm | 위해로부터안전 | 연맹 국내 정책명은 안전보호정책(별도 항목) | 편저자 |
| D-114 | Non-formal Education | 비정형학습 | 비형식교육(이형, 교육학 일반 번역) | 편저자 |
| D-115 | World Scout Education Congress | 세계스카우트교육총회 | 약어 WSEC | 편저자 |
| D-116 | GSAT | GSAT | 국내에서 약어 그대로 부름 | 편저자 |
| D-117 | Baden-Powell Fellowship | Baden-Powell Fellowship | BP 펠로우십 | 편저자 |
| D-118 | Better World Framework, Earth Tribe | 영문 그대로 | | 편저자 |
| D-119 | Korea Scout Parliamentary Union | 국회스카우트의원연맹 | 약어 KSPA. 정식 명칭 | 편저자 |
| D-120 | Asia-Pacific Regional Scout Foundation | 아시아-태평양 스카우트 지원재단 | 아시아태평양지역 스카우트지원재단(이형) | 편저자 |
| D-121 | Team System | (기존 국문 유지) | 옛 영문 Patrol System | 편저자 |
| D-122 | Badge / Pin | 패치 / 핀뱃지 | "패치"는 콩글리시가 아님. 영어 문맥에서는 badge로 옮김 | 편저자 · AI 정정 |
| D-123 | National Training Center | 중앙훈련원 | 옛 이름 중앙훈련소(1993년 승격) | 편저자 · 연맹 연혁 |
| D-124 | Korea Scout Foundation | 한국스카우트지원재단 | 옛 이름 한국보이스카우트지원재단(1983) | 편저자 · 연맹 연혁 |
| D-125 | Boy Scouts of Korea | 한국보이스카우트연맹 | BSK. 2001.12.29 한국스카우트연맹으로 명칭 변경 승인 | 편저자 · 연맹 연혁 |
| D-126 | National Board / Member | 중앙이사회 / 중앙이사 | | 편저자 · 연맹 안전보호정책 |
| D-127 | Council Commissioner / Chief Commissioner / Board Member | 지방커미셔너 / 지방치프커미셔너 / 지방이사 | | 편저자 |
| D-128 | KSA 지방·특수연맹 | ○○연맹 | "한국스카우트", "Korea Scout Association" 접두·접미 삭제 | 편저자 |
| D-129 | Chungnam Council | 충남세종연맹 | 옛 국문 충남연맹. 영문은 옛 용어집 표기 유지(확인 필요) | 검증(연맹 홈페이지) |
| D-130 | Member Organization / NSO / NSA | 회원기구 / 회원국 / 회원국협회 | 세 개념을 정의에서 서로 구분 | 편저자 승인 · 연맹 자료 "회원기구" 용례 |
| D-131 | Constitution of WOSM | 세계연맹헌장 | | 편저자 |
| D-132 | World Triennial Plan | 세계 3개년 계획 | | 편저자 |
| D-133 | Conference Resolution / Resolutions Committee | 총회 결의 / 총회 결의문 작성위원회 | | 편저자 |
| D-134 | Act on the Promotion of Scouting Activities | 스카우트활동 육성에 관한 법률 | 영문 법률명은 공식 번역 미확인 | 편저자(보수적 법률 문체) · 법률 원문 |
| D-135 | Asia-Pacific Region Award for Distinguished Service | 아시아태평양지역 최고 공로장 | 아·태지역 최고 공로장 | 편저자 · 세계일보 2015 |
| D-136 | Organizing Committee | 조직위원회 | "잼버리" 접두 없이 | 편저자 |
| D-137 | Subcamp | 분단 | | 편저자 |
| D-138 | Arrival / Departure | 입영 / 퇴영 | 폴란드 제26회 세계잼버리 일정 사례 | 편저자 · 대회 공식 사이트 |
| D-139 | Camp Chief | 야영장 | 장소 "야영장(場)"과 동음, 문맥 구분 | 편저자 |
| D-140 | World Scout Jamboree | (기존 유지) | 이형 "세계잼버리" 추가(언론 최다 용례) | 편저자 |

## 3. 사실 확인 기록

| 번호 | 내용 | 근거 |
|---|---|---|
| D-201 | WOSM 지역사무소 명칭이 Regional Office에서 Support Centre로 바뀐 시점: 2014년 하반기~2015년 상반기(정확한 날짜 미확인) | NST 2014.6.18; scout.org 2015.6.12 |
| D-202 | 유라시아지역은 2023.10.1부로 폐지, 지역은 5개. 유라시아지역사무처도 2023년 폐쇄 | WOSM Circular GLB-C02-2023 |
| D-203 | 세계청년이사 제도: 2023년 폐지 결정, 2024년 세계스카우트총회까지 임기 후 종료. 지역 단위는 지역별 존속 | WOSM Circular GLB-C21-2023 |
| D-204 | 세계스카우트이사회: 투표권 있는 이사 12명 중 의장 1·부의장 2 선출. 사무총장·재무·지역 이사회 의장(또는 부의장)·WSF 이사는 투표권 없는 당연직 | WSC Standing Orders(2024); treehouse.scout.org |
| D-205 | 컵스카우트 급위(다람쥐·토끼·사슴·곰·무지개)의 영문 명칭은 확인하지 못해 미수록 | — |

## 4. 제외 결정

다시 추가하지 않는다. 바꾸려면 편저자 승인이 필요하다.

- 종교계 국제 스카우트 기구(D-003), 각국 연맹 고유 명칭(D-001)
- Founder's Day(편저자 지시로 삭제, v1.0.0 이전 작업 번호 SKT-0018)
- WOSM Treasurer, Youth Programme, World Adults in Scouting Policy, WOSM Services
- 상징·관습(경례, 왼손 악수, 항건고리 등), 단위대·직책(대, 반, 반장 등), 컵스카우트 급위, 연맹 규정 세부 용어(취미장, 도전장 등) — 추후 검토
- 중앙명예회의, 쿠두 잼버렛, 패트롤잼버리, 기독교연맹(영문명 미확보), 스카우트 전략, 세계스카우트센터

## 5. 미결 사항

- Contingent / Delegation이 모두 "대표단", Head of Contingent / Head of Delegation이 모두 "대표단장"(README 한계에 명시)
- 충남세종연맹, 불교연맹의 연맹 공식 영문 명칭
- `source_status = compiler` 7건의 공개 근거 확보
