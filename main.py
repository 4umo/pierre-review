import os
import json
import requests
from prompt import generate_prompt, generate_comment

## FILLER FROM AUTOCOMPLETE

def get_pull_request_info():
    # Fetch the pull request info from GitHub API
    # (Replace with actual API calls)
    return {
        'id': 1,
        'diff_url': 'https://api.github.com/repos/owner/repo/pulls/1.diff'
    }

def post_comment_to_pr(pr_id, comment):
    # Post a comment to the pull request using GitHub API
    # (Replace with actual API calls)
    api_url = f"https://api.github.com/repos/owner/repo/pulls/{pr_id}/comments"
    headers = {
        'Authorization': f"token {os.getenv('GITHUB_TOKEN')}",
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'body': comment
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print(f"Successfully posted comment to PR {pr_id}")

def main():
    # Fetch pull request info
    pr_info = get_pull_request_info()
    pr_id = pr_info['id']
    diff_url = pr_info['diff_url']

    # Get code difference
    prompt = generate_prompt(diff_url)

    # Generate comments based on code difference
    comment = generate_comment(prompt)

    # Post each comment to the pull request
    post_comment_to_pr(pr_id, comment)

if __name__ == "__main__":
    main()
