chars_list1 = ["T","R","U","E"]
chars_list2 = ["L","O","V","E"]
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    count1 = 0
    count2 = 0
    for char1, char2 in zip(chars_list1, chars_list2):
        count1 += combined_names.count(char1)
        count2 += combined_names.count(char2)

    print("Your love score is: " + str(count1) + str(count2))
    #count(char)
name1 = input("Enter name1: ")
name2 = input("Enter name2: ")
calculate_love_score(name1, name2)