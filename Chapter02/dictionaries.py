


employees=[
{"name": "John Mckee","age": 38,"department": "Sales"},
{"name": "Lisa Crawford","age": 29,"department": "Marketing"},
{"name": "Sujan Patel","age": 33,"department": "HR"}
]
print(employees)

for employee in employees:
    print("Name:", employee['name'])
    print("Age:", employee['age'])
    print("Department:", employee['department'])
    print('-' * 23)

orders = {'apple':5, 'orange':3, 'banana':2}
print(orders.values())
print(list(orders.keys()))
print(list(orders.values()))

for tuple in list(orders.items()):
    print(tuple)