from aiohttp import ClientSession

class HttpRequest:
    def __init__(self, bot):
        self.bot = bot
        self.session = ClientSession(loop = bot.loop)
        
    async def request(method, url, **kwargs):
        headers = {
            "Authorization": f"Bot {self.bot.token}",
            "User-Agent": "DiscordBot (https://github.com/tuna2134/discord-interaction.py, 0.0.1)"
        }
        kwargs["headers"] = headers
        async with session.request(method, "https://discord.com/api/v8" + url, **kwargs) as r:
            return await r.json()
