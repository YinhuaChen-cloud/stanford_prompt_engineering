import os
from openai import OpenAI

# 1. 根据环境变量获取 openai key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 2. 定义 get_completion 方法
def get_completion(prompt, model="gpt-3.5-turbo"):
    response = client.responses.create(
        model=model,
        instructions=f"""Summarize the text delimited by triple backticks \ 
                    into a single sentence.""",
        input=prompt,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.output_text

# 3. 使用模型
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""

prompt = f"""
```{text}```
"""

response = get_completion(prompt)

print(response) 


