# 📓 ml_note

> Splunk Engineer → MLOps / AI Platform Engineer

---

## 📌 About

보안 로그 인프라 엔지니어의 ML 학습 기록입니다.

---

## 🗺 학습 로드맵

| 레벨 | 주제 | 상태 |
|---|---|---|
| Lv.1 | ML 기초 (sklearn · pandas · Kaggle) | 🔥 진행 중 |
| Lv.2 | 딥러닝 · PyTorch · CNN · RNN | ⏳ 예정 |
| Lv.3 | NLP · Transformer · BERT · GPT | ⏳ 예정 |
| Lv.4 | LLM · LoRA · PEFT · RAG · Agent | ⏳ 예정 |
| Lv.5 | MLOps · Docker · FastAPI · MLflow | ⏳ 예정 |
| Splunk AI | MLTK · DSDL · ES RBA | 🔥 병행 |

---

## 📁 디렉토리 구조

```
ml_note/
├── lv1/          # ML 기초
├── lv2/          # 딥러닝
├── lv3/          # NLP · Transformer
├── lv4/          # LLM · RAG · Agent
├── lv5/          # MLOps
├── splunk_ai/    # Splunk × AI
└── resources/    # 참고 자료
```

---

## ⚙ 환경 설정

```bash
# 미니콘다 + uv 환경
conda create -n ml_note python=3.11
conda activate ml_note
uv pip install -r requirements.txt
```

---

## 🛠 Tech Stack

**보유**

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat&logo=splunk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)

**학습 중**

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)

---

## 📝 Blog

[![Velog](https://img.shields.io/badge/Velog-20C997?style=flat&logo=velog&logoColor=white)](https://velog.io/@justnormguy)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dongmin-bae-97358818a)

---

## 커밋 규칙
| 말머리 | 용도 |
|---|---|
| `[feat]` | 새 기능 · 새 모델 · 새 분석 추가 |
| `[study]` | 강의 · 책 실습 코드 · 학습 노트 |
| `[fix]` | 오류 · 버그 수정 |
| `[docs]` | README · 주석 · 문서 수정 |
| `[refactor]` | 코드 구조 개선 · 정리 |
| `[chore]` | 환경 설정 · 패키지 · 잡일 |
| `[add]` | 데이터 · 파일 · 폴더 추가 |