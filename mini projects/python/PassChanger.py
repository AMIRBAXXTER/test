from functools import wraps
users = {"amir": "13761376", "mohadese": "13791379", "havva": "13131313"}
ban_users = {"mohadese"}


def ban_check(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in ban_users:
            print("you are banned...!")
        else:
            func(*args, *kwargs)
    return inner

@ban_check
def show_user(username):
    print(username, ":", users[username])

@ban_check
def change_pass(username, newpass):
    users[username] = newpass
    print(username, ":", users[username])


change_pass("amir", "12345678")
print(users)
