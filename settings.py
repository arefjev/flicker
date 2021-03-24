from decouple import config


API_KEY = config('FLICKR_APIKEY')
SECRET = config('FLICKR_SECRET')


if __name__ == '__main__':
    print(API_KEY)
    print(SECRET)
