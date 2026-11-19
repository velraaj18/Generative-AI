import asyncio
import time

async def call_llm(question : str):
    print(f"Sending Question, {question}")
    await asyncio.sleep(2)
    print(f"LLM Response for: {question}")

async def main():

    start = time.perf_counter()

    results = await asyncio.gather(
        call_llm("What is RAG?"),
        call_llm("What are embeddings?"),
        call_llm("What is tokenization?")
    )

    for result in results:
        print(result)

    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds")


asyncio.run(main())