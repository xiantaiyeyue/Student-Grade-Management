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
             {"number":6,"task":"sort"}
             ]

print("what do yo want to do?")

for num in item_list:#菜单
    print(f"please enter {num["number"]} to {num["task"]}",end = '\n')


def checkstu():#显示学生成绩
    for stu in students_list:
        print(f"NAME:{stu["name"]} SCORE:{stu["score"]}")


def addstu():#添加学生成绩
    addname = input("please enter name:")
    addscore = input("please enter score:")
    add_dict = {"name": addname, "score": addscore}
    students_list.append(add_dict)
    checkstu()


def changestu():#修改学生成绩
    print("please enter change name:")
    changename = input()
    print("please enter change score:")
    changescore = input()
    for count in students_list:
        if changename == count["name"]:
            count["score"] = changescore
            checkstu()
            break
    else:
        print("CAN NOT FIND!")    


def delstu():#删除指定学生
    print("please enter delete name:")
    delname = input()
    for index,count in enumerate(students_list):
        if delname == count["name"]:
            students_list.pop(index)
            checkstu()
            break
    else:
        print("CAN NOT FIND!")  


def averagestu():#计算班级平均分
    num = 0
    for score in students_list:
        num += score["score"]               
    return f"{num/len(students_list):.2f}"


def findstu():#找最高和最低的学生
    score_max = 0
    score_min = 100
    for name in students_list:
        if name["score"] >= score_max:
            score_max = name["score"]
            max_name = name["name"]        
        if name["score"] <= score_min:
            score_min = name["score"]
            min_name = name["name"]
    print(f"The Highest student:{max_name}\nThe Lowest student:{min_name}")


def sortstu():#成绩排序
    sort_list = []
    temp_list = students_list.copy()
    
    while len(temp_list)!=0:
        score_max = -1
        number = -1
        for index,name in enumerate(temp_list):
            if name["score"] > score_max:
                score_max = name["score"]
                number = index
        sort_list.append(temp_list.pop(number))
    for name in sort_list:
        print(name,end='\n')


order = input()

if order == "0":
    checkstu()
if order == "1":
    addstu()
if order == "2":
    changestu()
if order == "3":
    delstu()
if order == "4":
    print(averagestu())
if order == "5":
    findstu()
if order == "6":
    sortstu()