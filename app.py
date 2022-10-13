from requests import Session

URL: str = 'https://catalog.onliner.by/sdapi/catalog.api/search/player'


with Session() as session:
    response = session.get(
        url=URL,
        params={
            'player_type[0]': 'hifiplayer',
            'player_type[operation]': 'union',
            'group': 1
        }
    )
    print(response.status_code)
    print(response.cookies)
    print(response.headers)
    print(response.text)
    print(response.json())
