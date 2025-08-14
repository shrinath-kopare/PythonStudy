cities = {
    "Maharashtra" : "Pune",
    "Karnataka" : "Bangalore",
}

print(cities)

for city in cities:
    print(city)
    print(cities[city])

stud_subjects = {
    "Shrinath" : ["Math", "Science"],
    "Komal" : ["History", "Chemistry"],
}

print(stud_subjects["Shrinath"][1])

nested_list = ["a", "b",["c", "d"]]
print(nested_list)
print(nested_list[0])
print(nested_list[2][0])

nested_dict ={
    "Shri" : {
        "Sub" : "Math",
        "Grade" : "10th", },
}

print(nested_dict["Shri"]["Sub"])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4
print(dict)