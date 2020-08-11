import tweepy

username = str(input('Enter the username of your old account with followers: '))

print('Consumer keys must be of a developer account; access keys of your old account with followers (that you entered above).')

consumerKey = str(input('Enter your consumer key: '))
consumerSecret = str(input('Enter your consumer secret key: '))
accessKey = str(input('Enter your access key: '))
accessSecret = str(input('Enter your access secret key: '))

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

ids = []

print('Finding users... ')
for page in tweepy.Cursor(api.friends_ids, screen_name=username).pages():
    ids.extend(page)

print('Got following of', username)

print('Now, enter the access keys for your new account: ')
accessKey = str(input('Enter your access key: '))
accessSecret = str(input('Enter your access secret key: '))

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for user in ids:
    try:
        api.create_friendship(user)
        print('Followed', user)
    except:
        print('There was an error following the user with ID', user)
        continue

print('Your following should have been transferred!')
