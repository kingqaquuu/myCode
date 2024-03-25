'''
Author: kingqaquuu
Date: 2024-03-25 17:38:37
FilePath: \myCode\python-learn\heima\dict.py
'''
def main():
    my_dict={
        "王力宏":{
            "部门":"科技部",
            "工资":3000,
            "级别":"1"
        },"周杰伦":{
            "部门":"市场部",
            "工资":5000,
            "级别":"2"
        },"林俊杰":{
            "部门":"市场部",
            "工资":7000,
            "级别":"3"
        },"张学友":{
            "部门":"科技部",
            "工资":4000,
            "级别":"1"
        },"刘德华":{
            "部门":"市场部",
            "工资":6000,
            "级别":"2"
        }
    }
    print("当前全体员工信息如下:")
    print(my_dict)
    for key in my_dict:
        if my_dict[key]["级别"]=="1":
            my_dict[key]["工资"]+=1000
            my_dict[key]["级别"]="2"
    print("升级后的员工信息如下:")
    print(my_dict)
if __name__ == "__main__":
    main()