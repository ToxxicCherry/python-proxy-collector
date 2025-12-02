from pydantic import BaseModel

class Proxy(BaseModel):
    ip: str
    port: int
    protocol: str = 'http'

    def as_url(self):
        return f'{self.protocol}://{self.ip}:{self.port}'