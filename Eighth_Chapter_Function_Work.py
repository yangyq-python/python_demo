import  Eighth_Chapter_Function as fun
# 8-1消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。;;#
def display_message():
    """本章学习内容"""
    print("本章主要学习函数")
display_message()  #函数的调用
# 8-2喜欢的图书：编写一个名为favorite_book()的函数，其中包含一个名为title的形参。这个函数打印一条消息，如One of my favorite
# books is Alice in Wonderland.调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_boot(booke_name):
    print("\nOne of my favorite books is "+booke_name.title()+ " in Wonderland")
favorite_boot('alice')
# 8-3 T恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用函数来制作一件T恤；再使用关键字实参来调用这个函数。
def make_shirt(size,word):
    print("T恤的尺码是："+size+", 印在上面的字样是："+word.title())
make_shirt('xl','花样年华') #位置实参
make_shirt(word='花样年华',size='xl') #关键字实参
# 8-4 大号T恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样"I love Python"的大号T恤。调用这个函数来制作如下T恤：一件印有
# 默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size='大号',word='I love Python'):
    print('\nThis is a '+size+',且T恤印有：'+word+" 的字样")
make_shirt()
make_shirt(size='中号')
make_shirt(word='hello')
# 8-5 城市：编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，如Reykjavik is
# in Tceland.给用于存储国家的形参指定默认值。为三种不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
def describe_city(city_name,country='china'):
    print(city_name.title()+" is in "+country.title())
describe_city('shanghai')
describe_city('tokyo',country='japan')
describe_city('beijing')
# 8-6城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
# "Santiagp,Chile"，至少使用三个城市-国家对调用这个函数，并打印它返回的值。
def city_country(city_name,country):
    print(city_name.title()+","+country.title())
city_country('santiagp','chile')
city_country('beijing','china')
city_country('tokyo','japan')
# 8-7专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息
# 的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
def make_album(singer,album_name):
    albums={"singer":singer,"name":album_name}
    return albums
album_01=make_album('singer1','album_01')
album_02=make_album('singer2','album_02')
album_03=make_album('singer3','album_03')
album=[album_01,album_02,album_03]
print(album)
print(album_01,album_02,album_03)
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
# 调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(singer,album_name,sum_album=''):
    albums={"singer":singer,"name":album_name}
    if sum_album:
        albums['s_album']=sum_album
    return albums
a=make_album('singer4','album_04')
b=make_album('singer5','album_05','20')
print(a,b)
# 8-8用户的专辑：在为完成8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()，
# # 并将创建的字典打印出来。在这个while循环中，务必要提供退出途径。
# while True:
#     print("\nPlease enter singer and album name: ")
#     print("(enter 'q' at any time to quit)")
#     singer_names=input("singer_name: ")
#     if singer_names=='q':
#         break
#     ablums=input("album_name: ")
#     if ablums=='q':
#         break
#
#     make_albums=make_album(singer=singer_names,album_name=ablums)
#     print("\nHello, "+str(make_albums)+'!')
# 8-9魔术师:创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
magicians=['liu','zhang','wang']
def show_magicians(magicians_names):
    for magician_name in magicians_names:
        print("\nHello,"+magician_name.title())
show_magicians(magicians)
# 8-10了不起的魔术师：在你为完成练习8-9而编写的程序中，编写一个名为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样
# "the Great"。调用函数show_magicians(),确认魔术师列表确实变了。
def make_great(great_magicians):
    for i in range(len(great_magicians)):
        great_magicians[i]="the Great "+great_magicians[i]
    return great_magicians
print("对魔术师列表进行修改，每个魔术师的名字中加入the Great字样")
print(make_great(magicians))
show_magicians(magicians)
# 8-11不变的魔术师：修改你为完成8-10而编写的程序，在调用函数make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后的
# 列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians()，确认一个列表包含的是庲的魔术师名字，而另一个列表包含的是添加了
# 字样“the Great”的魔术师名字。
magicians=['liu','zhang','wang']
print("禁止函数修改列表，使用列表副本")
fuben=magicians[:]
make_great(fuben)
print(fuben)
print(magicians)
show_magicians(fuben)
show_magicians(magicians)
# 8-12三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，
# 对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def ingredients(*ingredients_name):
    print(ingredients_name)
ingredients('pepper')
ingredients('salt','sichuan pepper')
ingredients('pepper','salt')
# 8-13用户简介：复制前面的程序user_profile.py,在其中调用build_profile()来创建有关你的简介；调用这个函数，指定你的名和姓，以及三个描述你的键-值对。
self_introduction=fun.build_profile('李','名',height='175',weight='62kg',native_place='中国')
print(self_introduction)
# 8-14汽车：编写一个函数，将一辆汽车的信息存储在一个字典中，这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数；
# 提供必不可少的信息，以及两个名称-值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car=make_car('subaru','outback',color='blue',tow_package=True)打印返回的字典，确认正确地处理了所有的信息。
def make_car(manufacturer,model,**other):
    cars={}
    cars['manufacturer']=manufacturer
    cars['model']=model
    for key,value in other.items():
        cars[key]=value
    return cars
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
# 8-15打印模型：将示例print_models.py中的函数放在另一个名为pringting_functions.py的文件中；在print_models.py的开头编写一条import语句，
# 并修改这个文件以使用导入的函数。
# 8-16导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# -------------------------------
# 8-17函数编写指南：选择你在本章中编写的三个程序，确保它们遵循了本节介绍的函数编写指南。
# 导入函数的作业不做