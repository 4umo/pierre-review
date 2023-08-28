# 🇫🇷 Pierre-Review ☕️ 🥖 - LLM-Powered PR Summaries

## Overview

<img width="1039" alt="image" src="https://github.com/aummo/pierre-review/assets/9997548/3bc6f571-217d-47ec-bbc5-15474aed6b45">

🥖 🥖 🥖

Meet Pierre-Review, your personal PR (Pull Request) reviewer. Designed to streamline your code review process, Pierre automatically adds a comment on pull requests based on the code differences. This GitHub Action uses LLMs to summarize the PR and make your team's PR reviews a breeze.

## Features

- 🤖 Automated Code Review Comments: Get Pierre's precise and insightful comments instantly.
- 📝 Customizable Rules: Choose your model based on which you prefer.
- 🛠️ Easy Integration: Pierre is friendly and works seamlessly with your existing GitHub repositories.

## Quick Start

Add Pierre-Review as a github action to your repository! Once installed, Pierre-Review will automatically comment on new pull requests and add updates to existing ones.

## Installation

Create a `.github/workflows/pierre-review.yml` file in your GitHub repository.
Add the following YAML configuration to pierre-review.yml:

```yaml
name: Pierre-Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  autocomment:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run Pierre-Review
        uses: aummo/pierre-review@main
```

## Configuration

### Available LLMs

You can choose which LLM model Pierre uses by changing the `PIERRE_LANGCHAIN_LLM_API_NAME` environment variable in your github secrets. Pierre supports the following LLMs out of the box:

`open-ai` - running model "gpt-3.5-turbo"
`anthropic` - running model "claude-instant"

```
PIERRE_LANGCHAIN_LLM_API_NAME=open-ai|anthropic
```
