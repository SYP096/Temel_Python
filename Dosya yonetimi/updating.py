# with open("markalar.txt","a") as file:
#     file.write("6-Bmw")

# with open("markalar.txt","r+",encoding="utf-8") as file:
#     markalar = file.read()             5、6行 执行结果等于 7、8行
#     markalar = "1-Toyota\n" + markalar
#     file.seek(0)
#     file.write(1-Toyota\n)

with open("markalar.txt", "r+", encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2, "3-Renault\n")
    file.seek(0)
    # for marka in markalar:          14、15行 执行结果等于 16行
    #     file.write(marka)
    file.writelines(markalar)

with open("markalar.txt") as file:
    print(file.read())
