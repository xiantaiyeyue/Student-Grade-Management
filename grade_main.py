import grade_tools
str1 = "You should add students first"
while True:
    grade_tools.show_menu()
    action_str = input("please select the action to perform:")

    print(f"the action you selected is:'{action_str}'")

    if action_str == "0":
        check_result = grade_tools.checkstu(grade_tools.students_list)
        grade_tools.loop_printing(grade_tools.students_list,check_result,str1)
    
    elif action_str == "1":
        add_result = grade_tools.addstu(grade_tools.students_list)
        if add_result:
            print("Added successfully")
        else:
            print("Failed to add, please try again")

    elif action_str == "2":
        change_result = grade_tools.changestu(grade_tools.students_list)
        if change_result:
            print("Changed successfully")
        else:
            print("Failed to change, please try again")

    elif action_str == "3":
        del_result = grade_tools.delstu(grade_tools.students_list)
        if del_result:
            print(f"{del_result} has been deleted")
        else:
            print("CAN NOT FIND!")

    elif action_str == "4":
        average_result = grade_tools.averagestu(grade_tools.students_list)
        if  average_result is None:
            print(str1)
        else:
            print(round(average_result,2))
    
    elif action_str == "5":
        find_result = grade_tools.findstu(grade_tools.students_list)
        if find_result is None:
            print(str1)
        elif len(find_result) == 2:
            max_list,min_list = find_result          
            #for max_name in max_list:
            print(" & ".join(max_list))
            print(" & ".join(min_list))
        else :
            print(" & ".join(find_result))
            #     print("The Highest student:%s\nThe Lowest student:%s" % (max,min))

    elif action_str == "6":
        sort_result = grade_tools.sortstu(grade_tools.students_list)
        grade_tools.loop_printing(sort_result,sort_result,str1)
    
    elif action_str =="-1":
        print("welcome to use it again next time")
        break

    else:
        print("please enter again")
