from csv import DictReader

with open("products.csv") as file:
    csv_reader = DictReader(file)
    print(list(csv_reader))
    print('-----------------------------')
    file.seek(0)      # 因为在第五行已经遍历完了、所以重新遍历需要回到开头
    next(csv_reader)
    for i in csv_reader:
        print(i)
    print('------------------------------')
    file.seek(0)        # 因为在第89行已经遍历完了、所以重新遍历需要回到开头
    for p in csv_reader:
        if (p["Category"] == "Bilgisayar"):
            print(p['ProductName'], p['Price'])
