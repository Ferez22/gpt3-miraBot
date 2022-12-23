from flask import Flask, request
from dotenv import load_dotenv
from random import choice
import os
import openai

load_dotenv()
open.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: how old is earth Earth is estimated to be about 4.5 billion years old. Is there anything else I can help you with?"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt_text,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    storx = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

