import os

from groq import AsyncGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = AsyncGroq(
    api_key=os.getenv("OPENAI_API_KEY")
)


async def ask_llm(question: str):

    response = await client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

async def main():

    questions = ["In 10 words, what is embedding?",
                 "In 10 words, what is AI agents?",
                 "In 10 words, what is RAG?"]
    
    results = await asyncio.gather(
        *(ask_llm(q) for q in questions)
    )

    for question, answer in zip(questions, results):
        print(f"\nQuestion: {question}")
        print(f"Answer: {answer}")


asyncio.run(main())
