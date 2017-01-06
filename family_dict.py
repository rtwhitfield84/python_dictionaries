family = { 'sister': { 'name': 'Angela', 'age': 34 }, 'mother': { 'name': 'Patti', 'age': 63 }, 'father': { 'name': 'Jeff', 'age': 61 }, 'brother': { 'name': 'David', 'age': 35 } } 

my_family = {v['name'] + ' is my ' + k + ' and is ' + str(v['age']) + ' years old.' for (k,v) in family.items()}

print(my_family)