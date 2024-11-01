#! /home/adam/Desktop/PhD/Database/venv/bin/python

import aiohttp
import asyncio
import random

query = ["abc+def", "ddd+d"]
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"

async def main():
    async with aiohttp.ClientSession(headers={"User-Agent": user_agent}) as session:
        for i in query:
            await asyncio.sleep(random.uniform(1, 3))  # Add a random delay between requests
            async with session.get('https://scholar.google.com/scholar', params={'q': i}) as resp:
                print(f"Query: {i} -> Status: {resp.status}")
    
asyncio.run(main())
