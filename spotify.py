import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


spotify_id = 'c20725b1c7e44fc6876be40395967a6a'
spotify_secret = '78a0e4214dd945f1b9d66fd13ffbe663'

credentials = SpotifyClientCredentials(
    client_id=spotify_id,
    client_secret=spotify_secret
)

token = credentials.get_access_token()
sp = spotipy.Spotify(
    auth=token
)

results = sp.search(q='artist:' + 'kesha', type='artist')