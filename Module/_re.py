import re

# result = dir(re)    # 查看re模块的函数目录

# re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()          # 搜索全部

# result = re.findall("Python", str)
# result = len(result)

# re.split()       # 分割

# result = re.split(" ",  str)
# result = re.split("R",  str)

# re.sub()        # 替换

# result = re.sub(" ", "-", str)
# result = re.sub("\s", "-", str)

# re.search()          # 查找

# result = re.search("Python", str)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

# regular expression

"""
    [] - Köşeli parantezler arasina yazilan bütün karakterler
         aranir.
         [abc] => a      : 1 match
                  ac     : 2 match
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]
         [^abc] => abc dişindaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""

result = re.findall("[abc]", str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]",  str)
result = re.findall("[a-z]",  str)
result = re.findall("[0-5]",  str)
result = re.findall("[^abc]",  str)
result = re.findall("[^0-9]",  str)

"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches
"""

result = re.findall("...",  str)
result = re.findall("Py..on",  str)

"""
    ^ - Belirtilen string karakterlerle başliyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""

result = re.findall("^P", str)


"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match
"""

result = re.findall("t$", str)
result = re.findall("saat$", str)
result = re.findall("saatt$", str)

"""
     * - Bir karakterin sifir ya da daha fazla sayida olmasini
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nin arkasina n gelmiyor.)
"""
result = re.findall("sa*t", str)

"""
     + - Bir karakterin bir ya da daha fazla sayida olmasini
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nin arkasina n gelmiyor.)
"""

result = re.findall("sa+t", str)

"""
    ? - Bir karakterin sifir ya da bir kez olmasini
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nin arkasina n gelmiyor.)
"""

result = re.findall("sa?t", str)

"""
    {} - Karakter sayisini kontrol eder.
        al{2}   => a karakterinin arkasina l karakteri 2 kez tekrarlamali.
        al{2, 3} => a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlamali.
        [0-9]{2, 4} => en az 2 en çok 4 basamakli sayilar.
"""
result = re.findall("a{2}",  str)
result = re.findall("[0-9]{2}",  str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match
"""

"""
    () - gruplamak için kullanilir.
         (a|b|c)xz => a, b, c karakterlerinin arkasina xz gelmelidir.
"""
# 以下挺重要的
"""
老师写的是'\' , 但是我们最好写 '\\ , 两个都一样  但是 '\' 会有黄色下划线
    \\ - Özel karakterleri aramamizi sağlar.
            \\$a => $ karakterinin arkasina a karakterinin arar. Yani
                    $ regular exp. engine tarafindan yorumlanmaz.
    \\A - Belirtilen karakter string in başinda mi ?
            \\Athe => the string in başindami
                result = re.findall("\\APython",  str)
                result = re.findall("saat\\Z",  str)
    \\Z - Belirtilen karakter string in sonunda mi ?
            the\\Z => the string in sonunda mi
    \\b - Belirtilen karakter kelimenin in başinda ya da sonunda mi ?
            \\bthe => the kelimenin in başinda mi?
            the\\b => the kelimenin in sonunda mi?
    \\B - Belirtilen karakter kelimenin in başinda ya da sonunda değil mi ?
            \\Bthe => the kelimenin in başinda değil mi?
            the\\B => the kelimenin in sonunda değil mi?

    \\d - [0-9] ile ayni anlama gelir yani rakamlari arar.
            \\d => 12abc34
    \\D - [^0-9] ile ayni anlama gelir yani rakam olmayanlari arar.
            \\D => 1ab44_50
    \\s - Boşluk karakterlerini arar.
    \\S - Boşluk karakterleri dişindakiler.
    \\w - Alfabetik karakterler,  rakamlar ve alt çizgi karakteri.
    \\W - \\w nin tam tersi
"""


print(result)
