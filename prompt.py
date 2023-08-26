"""Interface for a GPT Prompts."""

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import LLMChain


SUMMARY_PROMPT = """
Summarize the following files changed in a pull request denoted in backticks submitted by a developer on GitHub, focusing on major modifications, additions, deletions, and any significant updates within the files.
Do not include the file name in the summary and list the summary with bullet points.

```
{diff}
```
"""

def generate_prompt(code_diff, llm, summary_prompt=SUMMARY_PROMPT) -> str:
    """Load the summary yaml"""

    human_prompt = HumanMessagePromptTemplate.from_template(
        summary_prompt)

    prompt_template = ChatPromptTemplate.from_messages(
        [human_prompt])
        
    chain = LLMChain(llm=llm,
                     prompt=prompt_template)

    output = chain.run({"diff": code_diff})
    
    return output 
