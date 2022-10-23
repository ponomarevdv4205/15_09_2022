class User:

    def __init__(self, name, Email):
        self.name = name
        self.Email = Email

    def __str__(self):
        return self.name


class ToDo:

    def __init__(self, text, user):
        self.user = user
        self.text = text


class Project:

    def __init__(self, name, users):
        self.name = name
        self.users = users
