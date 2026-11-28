# students_list = [
#     {"name": "Tom", "score": 92},
#     {"name": "Alice", "score": 92},
#     {"name": "Bob", "score": 76},
#     {"name": "wwee", "score": 76},
#     {"name": "sddd", "score": 40},
#     {"name": "acccc", "score": 92},
#                 ]
students_list = [
    {"name": "Tom", "score": 92},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 92},
    {"name": "wwee", "score": 92},
    {"name": "sddd", "score": 92},
    {"name": "acccc", "score": 92},
                ]
# students_list = []

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
    if len(students_list) != 0:
        return True
    else :
        return False       


def addstu(students_list):#添加学生成绩
    addname = input("please enter stu:")
    addscore = input("please enter score:")
    if addname.isalpha() and addscore.isdecimal() and (0<=int(addscore)<=100):
        add_dict = {"name": addname, "score": int(addscore)}
        students_list.append(add_dict)
        return True
    else :return False 


def changestu(students_list):#修改学生成绩
    print("please enter change stu:")
    changename = input()
    print("please enter change score:")
    changescore = input()
    if changename.isalpha() and changescore.isdecimal() and (0<=int(changescore)<=100):
        for stu in students_list:
            if changename == stu["name"]:
                stu["score"] = int(changescore)
                return True
        else:return False
    else :
        return False 



def delstu(students_list):#删除指定学生
    print("please enter delete stu:")
    delname = input()
    for index,count in enumerate(students_list):
        if delname == count["name"]:
            students_list.pop(index)
            return delname


def averagestu(students_list):#计算班级平均分
    if len(students_list) != 0:
        num = 0
        for stu in students_list:
            num += stu["score"]
        average_score = num/len(students_list)
        return average_score
    else :return


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
        if score_max != score_min:
            return max_name_list,min_name_list
        else :
            return max_name_list + min_name_list
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



def loop_printing(stu_list,result,setted_str):
    if result:
        for stu in stu_list:
            print(f"NAME:{stu['name']} SCORE:{stu['score']}")      
    else:
        print(setted_str)