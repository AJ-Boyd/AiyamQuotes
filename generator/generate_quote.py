"""
auth: AJ Boyd
date: 6/19/2024
file: generate_quote.py
desc: generates a quote that embodies a list of adjectives
"""

from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

def gen_quote(adjectives: list) -> str:
    return "I Love AI!!!!!"