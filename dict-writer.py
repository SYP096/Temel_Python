from csv import DictWriter,  DictReader

with open("products.csv", "w") as file:
    headers = ["ProductName", "Price", "IsPublished", "Category", "Reviews"]
    csv_writer = DictWriter(file,  headers)
    csv_writer.writeheader()    # DictWriter类中的一个实例方法或者类方法、用来写Header的
    csv_writer.writerow({
        "ProductName": "IPhone 7",
        "Price": 3000,
        "IsPublished": True,
        "Category": "Telefon",
        "Reviews": 4.7
    })    # 写单行数据、然后就是必须以字典的形式写
    csv_writer.writerow({
        "ProductName": "IPhone 8",
        "Price": 4000,
        "IsPublished": True,
        "Category": "Telefon",
        "Reviews": 4.7
    })
'''下面这个是写多行的'''
# with open("products.csv", "w") as file:
#     headers = ["ProductName", "Price", "IsPublished", "Category", "Reviews"]
#     csv_writer = DictWriter(file,  headers)
#     csv_writer.writeheader()
#     csv_writer.writerows([
#         {
#             "ProductName": "IPhone 7",
#             "Price": 3000,
#             "IsPublished": True,
#             "Category": "Telefon",
#             "Reviews": 4.7
#         },
#         {
#             "ProductName": "IPhone 8",
#             "Price": 4000,
#             "IsPublished": True,
#             "Category": "Telefon",
#             "Reviews": 4.7
#         },
#         {
#             "ProductName": "IPhone X",
#             "Price": 5000,
#             "IsPublished": True,
#             "Category": "Telefon",
#             "Reviews": 4.7
#         }
#     ])

# with open("products.csv", "a") as file:
#     headers = ["ProductName", "Price", "IsPublished", "Category", "Reviews"]
#     csv_writer = DictWriter(file,  headers)
#     csv_writer.writerow(
#         {
#             "ProductName": "IPhone 12",
#             "Price": 8000,
#             "IsPublished": True,
#             "Category": "Telefon",
#             "Reviews": 4.7
#         }
#     )


def price_with_tax(price):
    return float(price) * 1.18


with open("products.csv") as file:
    csv_reader = DictReader(file)
    products = list(csv_reader)

with open("new-products.csv", "w") as file:
    headers = ["ProductName", "Price", "IsPublished", "Category", "Reviews"]
    csv_writer = DictWriter(file,  headers)
    csv_writer.writeheader()
    for p in products:
        csv_writer.writerow({
            "ProductName": p["ProductName"],
            "Price": price_with_tax(p["Price"]),
            "IsPublished": p["IsPublished"],
            "Category": p["Category"],
            "Reviews": p["Reviews"]
        })
