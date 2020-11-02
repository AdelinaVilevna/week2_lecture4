# Bishkek = {
#  univery:{
#      gruppy:{
#          studenty:{                        # filtrasiya, poisk sortirovka

#          }
#      }
#  }   
# }

# student = {
#     "name": "Bakyt", 
#     "surname": "Bakytov", 
#     "age": 23, 
#     "languages": ["english","russian", "kyrgyz"],
#     "smokes": False,
#     "othe_dict": {1: "one", 2:"two"},
#     True: "True Pet",
#     (1, 2, 3): "eto tuple",
#     }
    # print(student[(1, 2, 3)])
    # print (student["othe_dict"][2])

# student.clear()
# new_student = student.copy()

# print(student.items())                 # iz elementov slovarya cdelal spisok, dlya togo chtoby proitis' po leementam

# for item in student.items():
#     print(item)
# print(student.keys())
# for item in student.keys():
#     print(item)
# print(student.values())
# for item in student.values():
#     print(item)
# new_item = student.pop("name")
# print(new_item)
# print(student)
# new_item = student.popitem()
# print(new_item)
# student.setdefault(10, "DEFDEF")

# student.update([("blake", 6), ("white", 8,)])
# student.update({"key1":1, "key2":2})
# print(student)

# print(student)

# student = {}
# print(type(student))
# student = dict((("winter", 1), ("spring", 2), ("fall", 3)))
# print(type(student))
# print(len(student))
# student["name"] = "Askat"
# print(student["name"])
# del student["name"]
# print(student)
# surname = student.get("surname")
# name = student["name"]
# print(surname)
# print(name)
# my_tuple = (("one",1),("two", 2),("three", 3))
# dict_=dict(my_tuple)
# # dict_= dict(one = 1, two = 2, three = 3)
# print(dict_)

# days = [1, 2, 3]
# days_name = ["mon","tues","wed"]
# one_more =[5, 6, 7]
# dict_days = (zip(days, days_name, one_more))
# print(dict_days)

# dict()
# student = dict.fronkeys([1, 2, 3], "Makers")
# print(student)