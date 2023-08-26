import os
import json
import requests
from prompt import generate_comment

## FILLER FROM AUTOCOMPLETE

def main():
    print("Hello World")
    # comment = generate_comment(prompt)

    # Post each comment to the pull request
    # post_comment_to_pr(pr_id, comment)

if __name__ == "__main__":
    main()
    # GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Replace with your GitHub token
    # REPO_NAME = "owner/repo"  # Replace with your repository name "owner/repo"
    # PR_NUMBER = 1  # Replace with your pull request number
    
    # diff_content = get_pr_diff(REPO_NAME, PR_NUMBER, GITHUB_TOKEN)
    # print("Diff Content:")
    # print(diff_content)
