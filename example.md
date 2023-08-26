Diff

```
@@ -0,0 +1,31 @@
+"""Interface for a GPT Prompts."""
+import os
+import sys
+
+from langchain.prompts import (
+    ChatPromptTemplate,
+    SystemMessagePromptTemplate,
+    HumanMessagePromptTemplate,
+    AIMessagePromptTemplate
+)
+from langchain.chains import LLMChain
+from langchain.chat_models import ChatOpenAI
+from dotenv import dotenv_values
+
+import openai
+
+SUMMARY_PROMPT = """
+Summarize the following file changed in a pull request submitted by a developer on GitHub,
+  focusing on major modifications, additions, deletions, and any significant updates within the files.
+  Do not include the file name in the summary and list the summary with bullet points.
+
+  {diff}
+"""
+
+def generate_prompt(summary_prompt = SUMMARY_PROMPT) -> str:
+    """Load the summary yaml"""
+    summary_prompt
+
+def generate_comment():
+    """Run the prompt to get PR comment"""
+    pass
\ No newline at end of file
```

Response

```
- Added import statements for various modules and packages
- Added a prompt template for GPT prompts
- Added import statement for the LLMChain class from langchain.chains module
- Added import statement for the ChatOpenAI class from langchain.chat_models module
- Added import statement for the dotenv_values function from dotenv module
- Added import statement for the openai module
- Added a constant variable named SUMMARY_PROMPT with a multi-line string as its value
- Defined a function named generate_prompt that takes a summary_prompt parameter and returns a string
- Inside the generate_prompt function, the summary_prompt is not being used
- Defined a function named generate_comment, but the implementation is not provided
```
