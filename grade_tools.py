students_list = [
    {"name": "Tom", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 76}
                ]
item_list = [{"number":0,"task":"checkstu"},
             {"number":1,"task":"addstu"},
             {"number":2,"task":"changestu"},
             {"number":3,"task":"delstu"},
             {"number":4,"task":"average"},
             {"number":5,"task":"find"},
             {"number":6,"task":"sort"},
             {"number":-1,"task":"exit"}
             ]


def checkstu(students_list):#显示学生成绩
    for stu in students_list:
        print(f"NAME:{stu['name']} SCORE:{stu['score']}")


def addstu():#添加学生成绩
    addname = input("please enter name:")
    addscore = input("please enter score:")
    if addname.isalpha() and addscore.isdecimal() and (0<=int(addscore)<=100):
        add_dict = {"name": addname, "score": int(addscore)}
        students_list.append(add_dict)
        print("Added successfully")
    else :
        print("Failed to add, please try again")


def changestu():#修改学生成绩
    print("please enter change name:")
    changename = input()
    print("please enter change score:")
    changescore = input()
    if changename.isalpha() and changescore.isdecimal() and (0<=int(changescore)<=100):
        for count in students_list:
            if changename == count["name"]:
                count["score"] = int(changescore)
                break
        else:
            print("CAN NOT FIND!")
    else :print("Failed to add, please try again")


def delstu():#删除指定学生
    print("please enter delete name:")
    delname = input()
    for index,count in enumerate(students_list):
        if delname == count["name"]:
            students_list.pop(index)
            checkstu(students_list)
            break
    else:
        print("CAN NOT FIND!")  


def averagestu():#计算班级平均分
    if len(students_list) != 0:
        num = 0
        for score in students_list:
            num += score["score"]
        average_score = f"{num/len(students_list):.2f}"
        print(average_score)
    else :print("The current score sheet is empty" \
    "Please add student grades first")

def findstu():#找最高和最低的学生
    if len(students_list) != 0:
        first_stu = students_list[0]
        score_max = first_stu["score"]
        score_min = first_stu["score"]
        for name in students_list:
            if name["score"] >= score_max:
                score_max = name["score"]
                max_name = name["name"]        
            if name["score"] <= score_min:
                score_min = name["score"]
                min_name = name["name"]
        print(f"The Highest student:{max_name}\nThe Lowest student:{min_name}")
    else :print("Please add student grades first")


def sortstu():#成绩排序
    temp_list = students_list.copy()

    score_list = sorted(temp_list,key=lambda stu:stu["score"],
                       reverse=True)
    checkstu(score_list)

def show_menu():
    print("*" * 50)
    print("what do you want to do?")
    for num in item_list:#菜单
            print(f"enter {num['number']} to {num['task']}",end = '\n')
    print("*" * 50)
