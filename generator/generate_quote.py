"""
auth: AJ Boyd
date: 6/19/2024
file: generate_quote.py
desc: generates a quote that embodies a list of adjectives
"""

from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
import re

SYS_PROMPT = "You are Aiyam, an AI language tool committed to providing short, stupid, nonsensical quotes to entertain. The quotes should be bad enough that it's clear an AI made them."
PROMPT = """
Put your generated quote in angle brackets. Generate one single unique, random, and entertaining quote in less than 15 words that subtly embodies different themes. 
It's important that the quotes do not directly name the theme they embody. 

Here is the list of themes: 
"""
def gen_quote(adjectives: list) -> str:
    llm = Ollama(
        model = "mistral",
        verbose = False,
        # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature = 1.82,
        system = SYS_PROMPT,
        top_k = 50,
        top_p = 0.95
    )
    response = llm.invoke(PROMPT + str(adjectives))
    print("response:", response)
    # text cleaning!
    response = response.strip()
    pattern = r'<([^\"]*)>'
    match = re.search(pattern, response)
    if match:
        response = match.group(1)
    if response.startswith("\"") == False:
        response = "\"" + response
    if response.endswith("\"") == False:
        response += "\""

    return response