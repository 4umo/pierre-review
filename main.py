import os
import json
from github import Github, Auth
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from prompt import (generate_prompt)

def main():
    # read env
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
    GH_APP_ID = os.environ.get('GH_APP_ID', None)
    GH_APP_PKEY = os.environ.get('GH_APP_PKEY', None)
    GITHUB_EVENT_PATH = os.environ.get('GITHUB_EVENT_PATH', None)
    PIERRE_LANGCHAIN_LLM_API_TOKEN = os.environ.get('PIERRE_LANGCHAIN_LLM_API_TOKEN', None)
    PIERRE_LANGCHAIN_LLM_API_NAME = os.environ.get('PIERRE_LANGCHAIN_LLM_API_NAME', None)
    
    if not GITHUB_TOKEN or not PIERRE_LANGCHAIN_LLM_API_TOKEN or not PIERRE_LANGCHAIN_LLM_API_NAME:
        print(f"""Missing environment variables:
        {'GITHUB_TOKEN' if not GITHUB_TOKEN else ''}
        {'GH_APP_ID' if not GH_APP_ID else ''}
        {'GH_APP_PKEY' if not GH_APP_PKEY else ''}
        {'GITHUB_EVENT_PATH' if not GITHUB_EVENT_PATH else ''}
        {'PIERRE_LANGCHAIN_LLM_API_TOKEN' if not PIERRE_LANGCHAIN_LLM_API_TOKEN else ''}
        {'PIERRE_LANGCHAIN_LLM_API_NAME' if not PIERRE_LANGCHAIN_LLM_API_NAME else ''}
        """)
        return 1

    # setup client
    gh = None
    try:
        gh = Github(auth=Auth.AppAuth(GH_APP_ID, GH_APP_PKEY))
    except Exception as e:
        print(f"Error initializing Github client: {e}")
        return 1

    # setup client
    llm = None
    try:
        if PIERRE_LANGCHAIN_LLM_API_NAME == 'open-ai':
            llm = ChatOpenAI(
                    model_name="gpt-3.5-turbo-16k", 
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

    event = {}
    with open(GITHUB_EVENT_PATH, 'r') as f:
        event = json.load(f)
    
    # fetch the diff
    pr_number = event["number"]
    repo_name = event["pull_request"]["base"]["repo"]["full_name"]

    # Get the repository
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    diff = '\n\n'.join([f.patch for f in pr.get_files()])
    diff = pr.get_files()[0].patch
    
    # send to langchain
    gen_description = generate_prompt(code_diff=diff, llm=llm)
    
    # write a comment/description
    pr.create_issue_comment(f"""🇫🇷 Pierre Review ☕️🥖:
                            {gen_description}
    """)
    
    return 0

if __name__ == "__main__":
    main()