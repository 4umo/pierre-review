# Pierre-Review: Your Personal PR Reviewer

## Overview

Meet Pierre-Review, your personal PR (Pull Request) reviewer. Designed to streamline your code review process, Pierre automatically adds a comment on pull requests based on the code differences. This GitHub Action uses LLMs to summarize the PR and make your team's PR reviews a breeze.

## Features

- 🤖 Automated Code Review Comments: Get Pierre's precise and insightful comments instantly.
- 📝 Customizable Rules: Choose your model based on which you prefer.
- 🛠️ Easy Integration: Pierre is friendly and works seamlessly with your existing GitHub repositories.

## Quick Start

Add Pierre-Review as a github action to your repository!

## Usage

Once installed, Pierre-Review will automatically comment on new pull requests and updates to existing ones.

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
        uses: yourusername/pierre-review@main
```
