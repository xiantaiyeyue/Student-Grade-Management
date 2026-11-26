import grade_tools
while True:
    grade_tools.show_menu()
    action_str = input("please select the action to perform:")
    print(f"the action you selected is:'{action_str}'")
    
    if action_str in ["0","1","2","3","4","5","6"]:
        if action_str == "0":
            grade_tools.checkstu(grade_tools.students_list)
        elif action_str == "1":
            grade_tools.addstu()
        elif action_str == "2":
            grade_tools.changestu()
        elif action_str == "3":
            grade_tools.delstu()
        elif action_str == "4":
            grade_tools.averagestu()
        elif action_str == "5":
            grade_tools.findstu()
        elif action_str == "6":
            grade_tools.sortstu()

    elif action_str =="-1":
        print("welcome to use it again next time")
        break

    else:
        print("please enter again")
