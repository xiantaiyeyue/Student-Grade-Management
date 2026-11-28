students_list = [
    {"name": "Tom", "score": 92},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 76},
    {"name": "wwee", "score": 76},
    {"name": "sddd", "score": 40},
    {"name": "acccc", "score": 92},
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
    

def addstu(students_list):#添加学生成绩
    result = user_input()
    if result is None:
        return None
    else :
        addname,addscore = result
        for stu in students_list:
            if addname == stu["name"]:
                return False   
        else:
            add_dict = {"name": addname, "score": addscore}
            students_list.append(add_dict)
            return True 


def changestu(students_list):#修改学生成绩
    result = user_input()
    if result is None:
        return None
    else:
        changename,changescore = result
        for stu in students_list:
            if changename == stu["name"]:
                stu["score"] = changescore
                return True
        else:return False 



def delstu(students_list):#删除指定学生
    print("please enter delete stu:")
    delname = input()
    for index,count in enumerate(students_list):
        if delname == count["name"]:
            students_list.pop(index)
            return delname
    else:
        return False


def averagestu(students_list):#计算班级平均分
    if len(students_list) != 0:
        num = 0
        for stu in students_list:
            num += stu["score"]
        average_score = num/len(students_list)
        return average_score
    else :
        return False


def findstu(students_list):#找最高和最低的学生
    if len(students_list) != 0:
        first_stu = students_list[0]
        score_max = first_stu["score"]
        score_min = first_stu["score"]
        max_name_list = []
        min_name_list = []
        for stu in students_list:
            if stu["score"] > score_max:
                score_max = stu["score"]
            if stu["score"] < score_min:
                score_min = stu["score"]    
        for stu in students_list:
            if stu["score"] == score_max:
                max_name_list.append(stu["name"])
            if stu["score"] == score_min:
                min_name_list.append(stu["name"])
        return max_name_list,min_name_list
    else :
        return False


def sortstu(students_list):#成绩排序
    if len(students_list) != 0:
        temp_list = students_list.copy()
        score_list = sorted(temp_list,key=lambda stu:stu["score"],reverse=True)
        return score_list
    else :
        return False
        

def show_menu():
    print("*" * 50)
    print("what do you want to do?")
    for num in item_list:#菜单
            print(f"enter {num['number']} to {num['task']}",end = '\n')
    print("*" * 50)



def loop_printing(students_list,setted_str):
    if students_list:
        for stu in students_list:
            print(f"NAME:{stu['name']} SCORE:{stu['score']}")      
    else:
        print(setted_str)


def user_input():
    print("Please enter the student information:")
    print("Enter 'esc' to exit")
    while True:  
        result1 = input("please enter stu_name:")
        if result1 == "esc":
            return None
        elif result1.isalpha():
            break
        else:
            print("The name can only be letters")
    while True:
        result2 = input("please enter score:")
        if result2 =="esc":
            return None
        elif result2.isdecimal() and (0<=int(result2)<=100):
            break
        else :
            print("Scores can only be numbers from 0 to 100")
    return result1,int(result2)
    