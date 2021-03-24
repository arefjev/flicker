from settings import API_KEY, SECRET


def get_secret():
    print('Flickr API_KEY: {0} and SECRET is {1}'.format(API_KEY, SECRET))


if __name__ == '__main__':
    get_secret()
