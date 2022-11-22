import asyncio
async def test():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

await test("async_.py")