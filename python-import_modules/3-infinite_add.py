#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv

    sum = 0

    if len(args) - 1 == 0:
        print(0)
    for i in range(1, len(args)):
        sum = sum + int(args[i])
    print(sum)
