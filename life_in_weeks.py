cur_age1 = int(input("Enter your age: "))
expected_age = 90


def life_in_weeks(cur_age):
    remaining_weeks = int((expected_age - cur_age) * 52)
    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks(cur_age1)