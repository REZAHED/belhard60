from aiohttp import ClientSession
import asyncio
async def get_response():

    async with ClientSession(base_url='https://catalog.onliner.by') as session:
        response = await session.get(
            url='/dapi/catalog.api/search/player',
            params={
                'player_type[0]': 'hifiplayer',
                'player_type[operation]': 'union',
                'group': '1'
            }
        )

# with Session() as session:
#     response = session.get(
#         url=URL,
#         params={
#             'player_type[0]': 'hifiplayer',
#             'player_type[operation]': 'union',
#             'group': 1
#         }
#     )
        print(response.status)
        # print(response.cookies)
        # print(response.headers)
        # print(await response.text())
        # print(await response.json())
async def main():
    task = [asyncio.create_task(get_response()) for _ in range(1)]
    await asyncio.wait(task)

asyncio.run(main())
