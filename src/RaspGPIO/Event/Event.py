
class Event:
    @classmethod
    def __init__(self):
        self.handlers = set()

    @classmethod
    def handle(self, handler):
        self.handlers.add(handler)
        return self

    @classmethod
    def unhandle(self, handler):
        try:
            self.handlers.remove(handler)
        except:
            raise ValueError("Handler is not handling this event, so cannot unhandle it.")
        return self

    @classmethod
    def fire(self, *args, **kargs):
        for handler in self.handlers:
            handler(*args, **kargs)

    @classmethod
    def getHandlerCount(self):
        return len(self.handlers)

    __iadd__ = handle
    __isub__ = unhandle
    __call__ = fire
    __len__  = getHandlerCount