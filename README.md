# Amazon Bedrock 챗봇

Amazon Bedrock과 Claude 3.5 Sonnet 모델을 활용한 대화형 챗봇 데모 프로젝트입니다.

## Amazon Bedrock 소개

Amazon Bedrock은 AWS에서 제공하는 서버리스 기반 생성형 AI 서비스입니다. 다양한 기반 모델(Anthropic의 Claude, AI21의 Jurassic, Stability AI의 Stable Diffusion 등)에 통합 API로 접근할 수 있게 해주며, 추가 인프라 관리 없이 생성형 AI 애플리케이션을 구축할 수 있습니다.

주요 특징:
- 다양한 기반 모델 선택 가능
- 프라이빗 엔드포인트 제공으로 데이터 보안 강화
- 기업 데이터로 모델 커스터마이징 가능
- 서버리스 아키텍처로 확장성 제공

## 기술 스택

- **Python**: 3.13
- **프론트엔드**: Streamlit
- **백엔드**: 
  - LangChain: AI 모델 오케스트레이션
  - Amazon Bedrock: Claude 3.5 Sonnet 모델
  - dotenv: 환경 변수 관리
- **대화 관리**: ConversationBufferMemory, ConversationChain

## 실행 방법

### 사전 준비

1. AWS 계정 및 Bedrock 접근 권한 설정
2. Python 3.13 이상 설치
3. Git 설치

### 프로젝트 설정

1. 저장소 복제
   ```bash
   git clone https://github.com/사용자명/amazon-bedrock-demo.git
   cd amazon-bedrock-demo
   ```

2. 가상환경 생성 및 활성화
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. 의존성 설치
   ```bash
   pip install -r requirements.txt
   ```

4. 환경 변수 설정
   - `.env` 파일 생성:
   ```
   AWS_PROFILE_NAME=your_aws_profile
   ```

### 실행

1. 챗봇 실행
   ```bash
   streamlit run frontend.py
   ```

2. 웹 브라우저에서 접속
   - 기본 URL: http://localhost:8501

## 개발 환경

### 모듈 버전
- Python: 3.13
- LangChain: 0.3.25
- LangChain Community: 0.3.x
- Streamlit: 1.45.1
- boto3: 1.x.x

### 시스템 요구사항
- 운영체제: macOS, Linux, Windows
- RAM: 최소 4GB (8GB 이상 권장)
- 인터넷 연결: AWS Bedrock 서비스 접근을 위해 필요

## 문제 해결

- **ImportError**: 가상환경이 활성화되어 있는지 확인하세요.
- **AWS 인증 오류**: AWS 자격 증명이 올바르게 설정되어 있는지 확인하세요.
- **리전 오류**: Bedrock이 지원되는 리전(us-east-1, us-west-2 등)을 사용하고 있는지 확인하세요.