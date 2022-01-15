class Survey:
    def __init__(self, name, c_acc, email, major):
        self.name = name
        self.c_acc = c_acc
        self.email = email
        self.major = major

    def name(self, name):
        self.name = name
        return self.main

    def c_acc(self, c_acc):
        self.c_acc = c_acc
        return self.c_acc

    def email(self, email):
        self.email = email
        return self.email

    def major(self, major):
        self.major = major
        return self.major

class Student:
    def __init__(self, name, c_acc, email, major, session):
        self.name = name
        self.c_acc = c_acc
        self.email = email
        self.major = major
        self.session = session

    def name(self, name):
        self.name = name
        return self.main

    def c_acc(self, c_acc):
        self.c_acc = c_acc
        return self.c_acc

    def email(self, email):
        self.email = email
        return self.email

    def major(self, major):
        self.major = major
        return self.major

    def session(self, session):
        self.session = session
        return self.session
