import ujson
import aiohttp


async def send_message(self, content: str):
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        await session.post(url="https://discord.com/api/v10/channels/1033659369998528553/messages", json={'content': content})