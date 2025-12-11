#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if x > len(my_list):
                break
            print(my_list[i], end="")
        print()
        return int(x)
    except:
        print("An error occured")
