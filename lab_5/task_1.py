import pprint

i = 0
k = 1
list_numbers = [ ]

while i <= 15:
    d = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    list_numbers.append(d)
    i = i + 1

pprint.pprint(list_numbers, width = 80)
