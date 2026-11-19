# Generative AI training

# Calling an LLM using the OpenAI() API function

import os
from openai import OpenAI
from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")
