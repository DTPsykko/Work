user1 = {
    'name': 'Sorna',
    'valid': True
}
user2 = {
    'name': 'Obama',
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            fn(*args, **kwargs)
        else:
            print('Not Authenticated')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user2)
