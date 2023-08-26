import os
from github import Github, Auth
from langchain.chat_models import ChatOpenAI, ChatAnthropic

def main():
    # read env
    print(os.environ)
    
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
    PIERRE_LANGCHAIN_LLM_API_TOKEN = os.environ.get('PIERRE_LANGCHAIN_LLM_API_TOKEN', None)
    PIERRE_LANGCHAIN_LLM_API_NAME = os.environ.get('PIERRE_LANGCHAIN_LLM_API_NAME', None)
    
    if not GITHUB_TOKEN or not PIERRE_LANGCHAIN_LLM_API_TOKEN or not PIERRE_LANGCHAIN_LLM_API_NAME:
        print(f"""Missing environment variables:
        {'GITHUB_TOKEN' if not GITHUB_TOKEN else ''}
        {'PIERRE_LANGCHAIN_LLM_API_TOKEN' if not PIERRE_LANGCHAIN_LLM_API_TOKEN else ''}
        {'PIERRE_LANGCHAIN_LLM_API_NAME' if not PIERRE_LANGCHAIN_LLM_API_NAME else ''}
        """)
        return 1

    # setup client
    gh = None
    try:
        gh = Github(auth=Auth.Token(GITHUB_TOKEN))
    except Exception as e:
        print(f"Error initializing Github client: {e}")
        return 1

    # setup client
    llm = None
    try:
        if PIERRE_LANGCHAIN_LLM_API_NAME == 'open-ai':
            llm = ChatOpenAI(
                    model_name="gpt-3.5-turbo", 
                    temperature=0.7, 
                    request_timeout=240,
                    max_retries=4,
                    max_tokens=1000,
                    streaming=True,
                    openai_api_key=PIERRE_LANGCHAIN_LLM_API_TOKEN
            )
        elif PIERRE_LANGCHAIN_LLM_API_NAME == 'anthropic':
            llm = ChatAnthropic(model_name="claude-instant", anthropic_api_key=PIERRE_LANGCHAIN_LLM_API_TOKEN)
        elif PIERRE_LANGCHAIN_LLM_API_NAME == 'code-llama':
            llm = None
        else:
            raise Exception(f"""Unsupported PIERRE_LANGCHAIN_LLM_API_NAME: {PIERRE_LANGCHAIN_LLM_API_NAME}
                Supported options: open-ai anthropic code-llama
            """)
    except Exception as e:
        print(f"Error initializing {PIERRE_LANGCHAIN_LLM_API_NAME} client: {e}")
        return 1

    # fetch the diff

    # send to langchain

    # write a comment/description

    return 0

if __name__ == "__main__":
    main()