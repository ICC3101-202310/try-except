from user import User

username = input('Ingresa el username: ')
while True:
    password = input('Ingresa el password: ')
    try:
        usr = User(username, password)
        break
    except ValueError:
        pass

print(usr.username)
print(usr.password)

try:
    print(usr.show())
except ValueError:
    print('Hubo un error')
