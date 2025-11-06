student_info1 = {
    "name": "Anirudh",
    "age": 33,
    "address": {"home address": "Hyderabad plot no 145",
                "office address": "Nallakunta"
                }
}

student_info2 = {
    "name": "Gus",
    "age": 33,
    "address": {"home address": "Hyderabad plot no 146",
                "office address": "Algaddabai"
                }
}

student_info3 = {
    "name": "Gusttgh",
    "age": 67,
    "address": {"home address": "Hyderabad plot no 1445",
                "office address": "podn"
                }
}


student_list = [student_info1, student_info2,student_info3]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["address"])
print(student_list[0]["address"]["home address"])
print(student_list[1]["address"]["home address"])
print(student_list[2]["address"]["office address"])
print(student_info3["address"]["office address"])






