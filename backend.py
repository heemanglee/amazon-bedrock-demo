from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

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

def buff_memory():
    """
    대화 이력을 저장하는 메모리 객체를 생성하고 반환합니다.
    이 메모리는 LLM 대화 컨텍스트를 유지하는 데 사용됩니다.
    """
    buff_memory = bedrock_chatbot()
    memory = ConversationBufferMemory(
        # 대화 이력 처리를 위한 LLM 객체
        llm=buff_memory,
        # 메모리에 저장할 최대 토큰 수 (이전 대화 컨텍스트 유지 길이)
        max_token_limit=200
    )
    return memory

def cnvs_chain(input_text, memory):
    """
    사용자 입력을 받아 LLM에 전달하고 응답을 반환하는 대화 체인을 생성합니다.
    
    Args:
        input_text (str): 사용자 입력 메시지
        memory (ConversationBufferMemory): 대화 이력이 저장된 메모리 객체
        
    Returns:
        str: LLM 응답 텍스트
    """
    chain_data = bedrock_chatbot()
    # 대화 체인 생성 (LLM + 메모리)
    cnvs_chain = ConversationChain(
        llm=chain_data,  # LLM 모델
        memory=memory,   # 대화 이력 메모리
        verbose=True     # 디버깅을 위한 상세 로그 출력 여부
    )

    # 사용자 입력을 LLM에 전달하고 응답 반환
    chat_reply = cnvs_chain.predict(input=input_text)
    return chat_reply
