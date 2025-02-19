# practice 7
# create a list from the two list provided by the user. And the user picks what numbers should be in the new list

# this the first list
def first_list():
    list1 = []
    n = 1
    print("now we are going to create the first list.")
    while n <= 6:
        value = input("** please provide a number here: ")
        if value.isdigit():
            list1.append(value)
            n += 1
        else:
            print("")
            print("the input provided is not a number.\n"
                  "please try again.")
            print("")
    print("")
    return f"this is the first list : {str(list1)}"

# this is the second list
def second_list():
    list2 = []
    n = 1
    print("now we are going to create the second list.")
    while n <= 6:
        value = input("** please provide a number here: ")
        if value.isdigit():
            list2.append(value)
            n += 1
        else:
            print("")
            print("the input provided is not a number.\n"
                  "please try again.")
            print("")
    print("")
    return f"this is the second list : {str(list2)}"

# this is the third list
def third_list():
    list3 = []
    n = 1
    print("now we are going to create the third list.")
    while n <= 6:
        value = input("** please choose a number from the previous lists: ")
        if value.isdigit():
            if value in result_1 or value in result_2:
                list3.append(value)
                n += 1
            else:
                print("")
                print("the value provided is not in any of the previous lists.\n"
                      "please try again.")
                print("")
        else:
            print("")
            print("the input provided is not a number.\n"
                  "please try again.")
            print("")
    print("")
    return f"this is the third list : {str(list3)}"

# here the program starts
print("hello there. this program is designed to create a list based on your choosing.\n"
      "please take your time to answer our requests so we can provide you with the output.\n"
      "thank you :)")
print("")

result_1 = first_list()
print(result_1)
print("")

result_2 = second_list()
print(result_2)
print("")

result_3 = third_list()
print(result_3)