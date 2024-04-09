import unittest
from unittest.mock import AsyncMock
import asyncio


async def birthABoy():
    await asyncio.sleep(1)
    return "This is Boy"


class AsyncClass:
    async def birthAGirl(self):
        await asyncio.sleep(1)
        return "This is Girl"


class TestAsync(unittest.TestCase):
    async def test_Class(self):
        class_instance = AsyncClass()
        class_instance.birthAGirl = AsyncMock(return_value="Letty Dom")
        result = class_instance.birthAGirl()
        print(result)


if __name__ == "__main__":
    unittest.main()
