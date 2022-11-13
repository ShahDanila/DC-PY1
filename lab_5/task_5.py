import random


def get_random_password():
    n = 8
    i = 0
    password = ''
    population = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    x = random.sample(population, n)
    while i < n:
        password = password + x[ i ]
        i = i + 1
    return(password)

print(get_random_password())


