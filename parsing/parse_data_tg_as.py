from telethon import TelegramClient
import time
import asyncio


class TgParse:
    def __init__(self, api_id: str, api_hash: str, chat: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.chat = chat

    async def get_gas_tg(self):
        async with TelegramClient('gas', self.api_id, self.api_hash) as client:
            await client.send_message(self.chat, '📃 Мій рахунок')
            await asyncio.sleep(5)
            try:
                async for message in client.iter_messages(self.chat, limit=1):
                    return float(message.message.split()[7])
            except:
                return "Data not received"

    async def get_jek_tg(self):
        async with TelegramClient('jek', self.api_id, self.api_hash) as client:
            await client.send_message(self.chat, '/to_pay')
            await asyncio.sleep(5)
            try:
                i = 0
                async for message in client.iter_messages(self.chat, limit=4):
                    i += 1
                    if i == 4:
                        return float(message.message.split()[9])
            except:
                return "Data not received"


if __name__ == '__main__':
    pass
