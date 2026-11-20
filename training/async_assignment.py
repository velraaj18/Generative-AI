import asyncio
import time

semaphore = asyncio.Semaphore(2)

async def async_ass(text : str):
    async with semaphore:
        await asyncio.sleep(2)
        return(f"Embedding generated for: {text}") 

async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        async_ass("Embedding"),
        async_ass("RAG"),
        async_ass("Agentic_AI"),
        async_ass("Embedding"),
        async_ass("RAG"),
        async_ass("Agentic_AI"),
        async_ass("Embedding"),
        async_ass("RAG"),
        async_ass("Agentic_AI")
    )

    for r in results:
        print (r)

    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds")

asyncio.run(main())