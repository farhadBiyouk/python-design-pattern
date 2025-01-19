class Database:
    def work(self):
        print('You have allow to work this database. you have access . have good time')


class Proxy:

    def check_access(self):
        password = input('Enter your password:  ')
        if password == '6600pasopish':
            db = Database()
            db.work()

        else:
            print('you do not have access to database')


pr = Proxy()
pr.check_access()