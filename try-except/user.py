class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if len(str(value)) < 5:
            raise ValueError('La contraseña debe tener a lo menos 5 caracteres')
        self.__password = value

    @property
    def username(self):
        # return self.__username
        raise PermissionError
    
    @username.setter
    def username(self, value):
        self.__username = value

    def show(self):
        if len(self.username) < 3:
            raise ValueError
        return f'{self.username}: {self.password}'
