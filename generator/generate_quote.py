"""
auth: AJ Boyd
date: 6/19/2024
file: generate_quote.py
desc: generates a quote that embodies a list of adjectives
"""

from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
import re, random
#It's important that the quotes do not directly name the theme they embody. 
SYS_PROMPT = "You are Aiyam, an AI language tool pretending to be a half-baked philosopher who gives short, stupid, nonsensical quotes and sayings. The quotes should be bad enough that it's clear they are satire."
PROMPT = """
Put your generated quote in square brackets and not quotations. Generate one single unique, random, and ironic saying or quote in less than 15 words that subtly embodies different themes. 
Quotes must be taken from the perspective of humans and may contain mature themes.\n

Here is the list of themes: 
"""
def gen_quote(themes: list) -> str:
    themes = random.sample(themes, len(themes))
    print("shuffled themes:", themes)
    llm = Ollama(
        model = "mistral",
        verbose = False,
        # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature = 1.82,
        system = SYS_PROMPT,
        top_k = 50,
        top_p = 0.95
    )
    response = llm.invoke(PROMPT + str(themes))
    print("response:", response)
    # text cleaning!
    response = response.strip()
    pattern = r'\[([^\]]*)\]'
    matches = re.findall(pattern, response)
    if matches:
        print("matches!")
        response = matches[0]
    response = response.replace("\"", "\'")
    if response.startswith("\"") == False:
        response = "\"" + response
    if response.endswith("\"") == False:
        response += "\""

    return response