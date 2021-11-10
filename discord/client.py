from .http import HttpRequest

class Client:
    def __init__(self, loop = None):
        self.http = HttpRequest()
        self.loop = asyncio.get_event_loop() if loop is None else loop
        
    def dispatch(self, name, *args, **kwargs):
        try:
            coro = getattr(self, name)
        except AttributeError:
            pass
        else:
            self.loop.create_task(coro)
            
    def command(self, coro):
        setattr(self, coro.__name__, coro)
        return coro
