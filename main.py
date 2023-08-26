import os
from github import Github, Auth

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
    G = Github(auth=Auth.Token(GITHUB_TOKEN))

    # fetch the diff

    # send to langchain

    # write a comment/description
    print('Hello World!')
    return 0

if __name__ == "__main__":
    main()