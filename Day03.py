

while True:
    dan = int(input("Dan(0) to quit : "))
    if dan == 0:
        break
    elif 1 < dan < 10:
        i = 1
        while i < 10:
            print("{0}*{1} = {2}\n".format(dan , i ,dan*i))
            i += 1
    else:
        print("2에서 9사이의 숫자를 입력하세요")

