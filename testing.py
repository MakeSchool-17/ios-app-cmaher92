from TwitterAPI import TwitterAPI

consumer_key = '7G4Iej1RdPUlhE4D8cQly14JD'
consumer_secret = 'dfZxFrG2ny9IlCeeiMZUrdTyq3Fbjv7yJbuxBTtaP3ljoAnUhQ'
access_token_key = '1679226714-CzxZ3cKp62vby4AqNoJ3W0ZtBom4hZZErMtPN5J'
access_token_secret = 'usl4ODEdismL71aN8RJDvpiECAI41287HWjAbBzboQJjH'
count = 0

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

r = api.request('statuses/filter', {'track': 'bitcoin'})
for item in r.get_iterator():
    if 'text' in item:
        count += 1
        print(count)
