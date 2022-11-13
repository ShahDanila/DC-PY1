import random

def get_unique_list_numbers():
    n = 15
    list_ = set()
    while len(list_)< n:
        list_.add(random.randint(-10, 10))
    return list_


print(get_unique_list_numbers())


