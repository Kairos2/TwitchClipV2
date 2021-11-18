import requests

url = "https://gql.twitch.tv/gql"
json_req = """[{"query":"query ClipsCards__Game($gameName: String!, $limit: Int, $cursor: Cursor, $criteria: GameClipsInput) { game(name: $gameName) { id clips(first: $limit, after: $cursor, criteria: $criteria) { pageInfo { hasNextPage __typename } edges { cursor node { id slug url embedURL title viewCount language curator { id login displayName __typename } game { id name boxArtURL(width: 52, height: 72) __typename } broadcaster { id login displayName __typename } thumbnailURL createdAt durationSeconds __typename } __typename } __typename } __typename } } ","variables":{"gameName":"League of Legends","limit":100,"criteria":{"languages":[],"filter":"LAST_DAY"},"cursor":"MjA="},"operationName":"ClipsCards__Game"}]"""
r = requests.post(url, data=json_req, headers={"client-id":"kimne78kx3ncx6brgo4mv6wki5h1ko"})
r_json = r.json()

print(r_json)
edges = r_json[0]['data']['game']['clips']['edges']
urls = [edge['node']['url'] for edge in edges]

for url in urls:
    print(url)