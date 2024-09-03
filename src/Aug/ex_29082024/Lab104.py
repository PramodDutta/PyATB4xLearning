# Dict
# Key and Value
# name -> "Pramod"

student_infor = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": "KA"
}

print(student_infor)
print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])

student_infor["age"] = 100
print(student_infor)

student_infor = dict(name="Pramod", age=67, address="KA")
# A dictionary is an unordered collection of data


student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_list= [student_infor1,student_infor2]
print(student_list)