from csv import writer,  reader

# with open("cars.csv", "w") as file:
# # 就算是使用了csv模块、还是基于python内置的所以可以用‘w'
#     csv_writer = writer(file)
#     # 先把file作为实例导入到csv模块中的writer类、使csv_writter是其类的实例对象
#     csv_writer.writerow(["Marka", "Model"])   # writerow是写单行、 row是行的意思
#     csv_writer.writerow(["Toyota", "Yaris"])
#     csv_writer.writerow(["Toyota", "Corolla"])

# with open("cars.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerows([["Marka", "Model"],
#                ["Toyota", "Yaris"], ["Toyota", "Corolla"]])
# writerows 是写多行、列表内的元素一行一行的写出来、delimiter默认是逗号


# with open("cars.csv", "a") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Toyota", "Rav4"])

# with open("products.csv") as file:
#     csv_reader = reader(file)
#     with open("new-products.csv", "w") as file:
#         csv_writer = writer(file)
#         for product_row in csv_reader:
#             csv_writer.writerow([p.upper() for p in product_row])


with open("products.csv", "r+", newline='') as file:
    csv_reader = reader(file)    # delimerit的默认值是逗号
    csv_writer = writer(file)
    f_liste = []
    try:
        # 这个try只能解决最后出现的错误数据、如果文本是汉语的、你需要再加一个except UnicodeencodeError
        next(csv_reader)
        for p in csv_reader:
            f_liste.append([p[0], float(p[1])*1.2, p[2], p[3], p[4]])
    except ValueError:
        pass
    except IndexError:
        pass

    file.seek(0)
    csv_writer.writerow(["ProductName", "Price",
                         "IsPublished", "Category", "Reviews"])
    csv_writer.writerows(f_liste)

'''
如何解决打印的文件里会每一行之后多一行空行?
剋看上面第30行的 newline='' 这个就能解决
'''
