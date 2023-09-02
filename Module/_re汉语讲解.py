import re
str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"
# result = re.findall("Python", str)      # 查找所有参数， 输出为列表
result = re.split(" ", str)               # 分割， 输出为列表
result = re.sub(" ", "-", str)         # 替换

result = re.search("Python", str)     # <re.Match object; span=(0, 6), match='Python'>
'''以下9-13根据7'''
# result = result.span()         # span 目标范围
# result = result.group()          # group 查找的目标群
# result = result.start()            # 目标的开头索引
# result = result.end()                # 目标的结尾索引
# result = result.string                 # 查看目标所在字符串
'''以下根据3         finfall()     '''
str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"
result = re.findall("[a-c]", str)        # 查找字符串中a-c（abc）  并且逐个输出为列表
result = re.findall("[abc]", str)       # 输出同16
result = re.findall("[a-chP]", str)       # 查找a-c(abc), h, P
result = re.findall("[0-9]", str)        # 查找0-9的数字
result = re.findall("[^0-9]", str)     # 查找除了0-9的数字
result = re.findall("p", str)           # []
result = re.findall("...", str)            # 使该字符串 以 三个三个的元素(with space)分割成列表
result = re.findall("..", str)           # 类似于22
result = re.findall(".", str)
result = re.findall(".a", str)           # ['ra', 'la', 'ma', 'sa']
result = re.findall("^Python", str)        # 查看是否以该字符开头， 如果是 返回 ['p']    不是返回[]
result = re.findall("t$", str)         # ---------------------结尾，-------------['t']                    []
result = re.findall("saat$", str)        # ['saat']
result = re.findall("\\APython", str)      # 同26     \, \\ 都可以， 但是最好用 \\ , 因为\会出现黄色下划线
print(result)      # ['Python']
result = re.findall("saat\\Z", str)           # 同28
result = re.findall("\\bPython", str)          # ['Python', 'Python']
print(result)       # ['Python', 'Python']
result = re.findall("\\bReh", str)               # ['Reh']    查找字符串中每个单词的开头是否为Reh     不是 []
result = re.findall("on\\b", str)                 # ['on', 'on']     查找字符串中每个单词的结尾是否为on   不是 []
result = re.findall("\\BPy", str)                  # []
result = re.findall("\\Bon", str)                 # ['on', 'on'] \\B 和\\b 作用相反
result = re.findall("Reh\\B", str)               # ['Reh']
result = re.findall("sst\\B", str)                 # []
result = re.findall("\\d", str)                     # 同 [0-9]
result = re.findall("\\D", str)                     # 同 [^0-9]
result = re.findall("\\s", str)                      # 查找space
result = re.findall("\\S", str)                     # 查找 非 space的元素
result = re.findall("\\w", str)                    # 查找 字母， 数字，下划线
result = re.findall("\\W", str)                    # 查找 非 字母， 数字，下划线 的元素
print(result)
