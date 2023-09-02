import datetime
# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
# durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da
# üniversite olmalıdır.
'''
name = input("please input your name: ")
age = int(input("please input your age:"))
education = input("please input your education: ")
if age >= 18:
    if education == 'high school' or education == 'licence':
        print(f"{name}, you can have driving licence")
    else:
        print(f"{name}, you cannot have driving licence,
        your age is sufficient but education level is not suitable")
        # 年龄到了，学位不到
else:
    print(f"{name}, you cannot have driving licence,
    your age is not sufficient")
'''
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
# not aralığına karşılık
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
'''
not1 = float(input("please input your not1: "))
not2 = float(input("please input your not2: "))
ortalama = (not1 + not2)/2
if 0 < ortalama <= 24:
    print(f"your ortalama is {ortalama}")
    print(0)
elif 25 < ortalama <= 44:
    print(f"your ortalama is {ortalama}")
    print(1)
elif 45 < ortalama <= 54:
    print(f"your ortalama is {ortalama}")
    print(2)
elif 55 < ortalama <= 69:
    print(f"your ortalama is {ortalama}")
    print(3)
elif 70 < ortalama <= 84:
    print(f"your ortalama is {ortalama}")
    print(4)
elif 85 < ortalama <= 100:
    print(f"your ortalama is {ortalama}")
    print(5)
'''
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını
# aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#    *** datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2018/8/1) => gün
first_time = input("please enter the time of your first drive: , (2020/2/3)")
first_time = first_time.split('/')
print(type(first_time), '\t', first_time)   # 输出为列表，例 ['2022', '3', '3']

now = datetime.datetime.now()
print(type(now), '\t', now)
first_time = datetime.datetime(year=int(first_time[0]),
                               month=int(first_time[1]),
                               day=int(first_time[2]))
# 上面这行代码， year=， month=， day=，也可以不写，直接位置实参，写了就是关键词实参
# 62 行代码输出的列表中每个元素都是字符串、所以在67行代码需要加上 int
print(type(first_time), '\t', first_time)
fark = now - first_time
print(type(fark), '\t', fark)
# # <class 'datetime.timedelta'> 376 days, 19:15:45.155297
day = fark.days
print(type(day), '\t', day)        # <class 'int'>    528
if day > 0:
    if day <= 365:
        print(f"Your uesing time is {day}")
        print("1. service bakim")
    elif day <= 365*2:
        print(f"Your uesing time is {day}")
        print("2. service bakim")
    elif day <= 365*3:
        print(f"Your uesing time is {day}")
        print("3. service bakim")
    else:
        print("不好意思, 您的质保时间已过期")
else:
    print("请输入正确的时间")
