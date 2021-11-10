from .http import HttpRequest

class Client:
    def __init__(self, loop = None):
        self.http = HttpRequest(self)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.cmd = []
        self.cmd_data = []
        
    def dispatch(self, name, *args, **kwargs):
        try:
            coro = getattr(self, name)
        except AttributeError:
            pass
        else:
            self.loop.create_task(coro)
            
    def event(self, coro):
        setattr(self, coro.__name__, coro)
        return coro
    
    def command(self, coro):
        self.cmd.append(coro)
        return coro
    
    async def fetch_command(self):
        return await self.http.request("GET", f"/applications/{self.user.id}/commands")

    async def set_command(self):
        for coro in self.cmd:
            cmd = {
                "name": coro.__name__,
                "type": 1,
                "description": "..."
            }
            self.cmd_data.append(cmd)
         
    async def setup(self):
        cmds = await self.fetch_command()
        for data in cmds:
