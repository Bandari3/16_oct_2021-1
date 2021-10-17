# List

# friends = ["Anne", "Peggy", "Ram", "Shobhit", "Priya"]
# print(type(friends))
# # Indexing and Slicing
# print(friends[1])
# print(friends[-1])
# print(friends[:3])
# print(friends[2:])
# print(friends[-2:])
# print(len(friends))
#
# # List Manipulation
# print(hex(id(friends)))
# friends.append("Raman")
# print(hex(id(friends)))
# print(friends)
# more_friends = ["Peter", "John", "Sam"]
# friends.extend(more_friends)
# print(friends)
# friends.insert(0, "Dimple")
# print(friends)
# friends.remove("Dimple")
# print(friends)
# print(friends.pop(4))
# friends.pop()
# print(friends)
# friends.insert(0, more_friends)
# print(friends)
# for index, value in enumerate(more_friends):
#     friends.insert(index, value)
#
# print(friends)
# print(friends.index("John"))
# print('Sam' in friends)
# print('Sam' not in friends)
#
# total_friends = friends + more_friends
# print(total_friends)
# print(total_friends*2)

# Tuple

friends = ("Anne", "Peggy", "Ram", "Shobhit", "Priya", "Peggy", "Peggy")
friends_list = list(friends)
print(friends_list)
# print(len(friends))
# print(max(friends))
# print(min(friends))
# print(type(friends))
# print(friends[3])
# print(friends[:2])
# print(friends.index("Ram"))
# print(friends.count("Peggy"))
# print(hex(id(friends)))
# friends = ("Anne", "Peggy", "Ram", "Shobhit")
# print(friends)
# print(hex(id(friends)))

# Dictionary

# student = {'name': 'Saurabh', 'age': 34, 'marks': [76, 89, 67, 98, 76]}
# print(student['name'])
# print(student['marks'])
# print(student.get('subject', 'CSE'))
# #print(student['subject'])
# student['name'] = "Sam"
# print(student)
# student['subject'] = "ME"
# print(student)
# student.pop('name')
# print(student)
# student.popitem()
# print(student)
# #del student
# student.clear()
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# Sets
friends = {"Anne", "Peggy", "Ram", "Shobhit", "Priya", "Peggy"}
print(type(friends))
print(friends)

for f in friends:
    print(f)
friends.add("John")
print(friends)
friends.discard("John")
print(friends)
close_friends = {"Priya", "Raman", "Sam"}
print(friends.union(close_friends))
print(friends.intersection(close_friends))
print(friends.difference(close_friends))
print(close_friends.difference(friends))
