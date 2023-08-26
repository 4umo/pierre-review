"""Interface for a GPT Prompts."""
import os
import sys

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from dotenv import dotenv_values

import openai 

SUMMARY_PROMPT = """
Summarize the following file changed in a pull request submitted by a developer on GitHub,
  focusing on major modifications, additions, deletions, and any significant updates within the files.
  Do not include the file name in the summary and list the summary with bullet points.

  {diff}
"""

def generate_prompt(summary_prompt = SUMMARY_PROMPT) -> str:
    """Load the summary yaml"""
    summary_prompt

def generate_comment():
    """Run the prompt to get PR comment"""
    pass