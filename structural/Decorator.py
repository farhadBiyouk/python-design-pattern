"""
Structural: Decorator
    have different between this pattern and python decorator
"""


class Login:  # additional job
    def check_login(self, username, password):
        if username == 'admin' and password == 'admin':
            return True
        return False


def outer_login(func):
    def inner_login():
        username= input('Enter your username: ')
        password = input('Enter your password:')
        l = Login()
        result = l.check_login(username, password)
        if result:
            func()
        else:
            print('Wrong username or password')
    return inner_login


class Articles:
    def show(self):
        print('All Articles')


@outer_login
def show_all_article():
    a = Articles()
    a.show()


show_all_article()
