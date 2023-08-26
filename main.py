import os
from github import Github, Auth
from langchain.chat_models import ChatOpenAI, ChatAnthropic

def main():
    # read env
    print(os.environ)
    
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
    LANGCHAIN_LLM_API_TOKEN = os.environ.get('LANGCHAIN_LLM_API_TOKEN', None)
    LANGCHAIN_LLM_KEY = os.environ.get('LANGCHAIN_LLM_KEY', None)
    
    if not GITHUB_TOKEN or not LANGCHAIN_LLM_API_TOKEN or not LANGCHAIN_LLM_KEY:
        print(f"""Missing environment variables:
        {'GITHUB_TOKEN' if not GITHUB_TOKEN else ''}
        {'LANGCHAIN_LLM_API_TOKEN' if not LANGCHAIN_LLM_API_TOKEN else ''}
        {'LANGCHAIN_LLM_KEY' if not LANGCHAIN_LLM_KEY else ''}
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
        if LANGCHAIN_LLM_KEY == 'open-ai':
            llm = ChatOpenAI(
                    model_name="gpt-3.5-turbo", 
                    temperature=0.7, 
                    request_timeout=240,
                    max_retries=4,
                    max_tokens=1000,
                    streaming=True,
                    openai_api_key=LANGCHAIN_LLM_KEY
                    )
        elif LANGCHAIN_LLM_KEY == 'code-anthropic':
            llm = ChatAnthropic(model_name="claude-instant", anthropic_api_key=LANGCHAIN_LLM_API_TOKEN)
        elif LANGCHAIN_LLM_KEY == 'code-llama':
            llm = None
        else:
            raise Exception(f"""Unsupported LANGCHAIN_LLM_KEY: {LANGCHAIN_LLM_KEY}
                Supported options: open-ai anthropic code-llama
            """)
    except Exception as e:
        print(f"Error initializing {LANGCHAIN_LLM_KEY} client: {e}")
        return 1

    # fetch the diff

    # send to langchain

    # write a comment/description
    print('Hello World!')
    return 0

if __name__ == "__main__":
    main()