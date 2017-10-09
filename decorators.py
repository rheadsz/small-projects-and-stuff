

class User():

    def __init__(self,user):
        self.user = user

    def isLoggedin(func):
        def check(self):
            if self.user in login_list:
                func(self)
        return check

    @isLoggedin
    def sayhi(self):
        print("Hello, {}".format(self.user))


class Numbers():

    magic_num = 7

    def __init__(self):
        pass

    def checkIfNumber(func):
        def checkif7(self,num):
            if num == Numbers.magic_num:
                func(self,num)
                print("Yay!")
        return checkif7

    @checkIfNumber
    def choice(self,num):
        self.num = num
        print("Your number is",self.num)

x = Numbers()
x.choice(7)

#login_list = ['Harowitz Black']
#x = User('Harowitz Black')
#x.sayhi()
