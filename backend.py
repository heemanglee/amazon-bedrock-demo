from langchain_community.chat_models import BedrockChat
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드
load_dotenv()

def bedrock_chatbot():
    """
    Amazon Bedrock에 접근하기 위한 BedrockChat 객체를 생성하고 반환합니다.
    """
    bedrock_llm = BedrockChat(
        # AWS 자격 증명 프로필 이름 (.aws/credentials 파일에서 참조)
        credentials_profile_name=os.getenv("AWS_PROFILE_NAME", "default"),
        # 사용할 모델 ID (Claude 3.5 Sonnet 모델)
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0", 
        model_kwargs={
            # 온도 값: 높을수록 더 창의적인 응답 (0.0-1.0)
            "temperature": 0.5,
            # 상위 확률 샘플링: 확률이 높은 토큰만 고려 (0.0-1.0)
            "top_p": 1,
            # 상위 k개 토큰만 고려: 후보 토큰 수 제한 (1-500)
            "top_k": 250,
            # 최대 생성 토큰 수: 응답 길이 제한
            "max_tokens": 512
        }
    )

    return bedrock_llm

def simple_chat(input_text):
    """
    메모리 저장 없이 단순하게 채팅 테스트를 수행하는 함수입니다.
    
    Args:
        input_text (str): 사용자 입력 메시지
        
    Returns:
        str: LLM 응답 텍스트
    """
    # BedrockChat 객체 생성
    bedrock_llm = bedrock_chatbot()
    
    # 사용자 입력에 대한 응답 생성
    response = bedrock_llm.invoke(input_text)
    
    # 응답 반환
    return response.content
