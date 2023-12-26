from time import sleep
import asyncio

# versão sincrona
# class SyncSpongeBob:
#     def cook_bread(self):
#         await sleep(3)
#     def cook_hamburgue(self):
#         await sleep(10)
#     def mount_sandwich(self):
#         await sleep(3)
#     def make_milkshake(self):
#         await sleep(5)
#     def cook(self):
#         self.cook_bread()
#         self.cook_hamburgue()
#         self.mount_sandwich()
#         self.make_milkshake()

# sync_spongebob = SyncSpongeBob()
# sync_spongebob.cook()


# versão assincrona
# class AsyncSpongeBob:
#     async def cook_bread(self):
#         await asyncio.sleep(3)
#     async def cook_hamburgue(self):
#         await asyncio.sleep(10)
#     async def mount_sandwich(self):
#         await asyncio.sleep(3)
#     async def make_milkshake(self):
#         await asyncio.sleep(5)
#     async def cook(self):
#         await asyncio.gather(
#             self.cook_bread(),
#             self.cook_hamburgue(),
#             self.make_milkshake()
#         )
#         await self.mount_sandwich()


# async_spongebob = AsyncSpongeBob()
# asyncio.run(async_spongebob.cook())




# versão assincrona
class AsyncSpongeBob:
    async def cook_bread(self):
        await asyncio.sleep(3)
    async def cook_hamburgue(self):
        await asyncio.sleep(10)
    async def mount_sandwich(self):
        await asyncio.sleep(3)
    async def make_milkshake(self):
        await asyncio.sleep(5)
    async def make_sanduich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburgue(),
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())

    async def cook(self):
        await asyncio.gather(
            self.make_sanduich(),
            self.make_milkshake()
        )


async_spongebob = AsyncSpongeBob()
asyncio.run(async_spongebob.cook())










