try:
    with open("msg.txt", "r", encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatasi: ", e)
finally:
    print("dosya kapandi")
# with 就是打开之后自动关闭
