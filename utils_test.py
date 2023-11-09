import my_utils

if __name__ == '__main__':
    ave = my_utils.average([10, 23, 30])
    print("Average is", ave)
    print("Another average is", my_utils.average([10.2, 8.8, 2.6]))
    area = my_utils.area_rectangle(10,20)
    print("area = ",area)