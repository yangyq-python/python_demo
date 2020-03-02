#5-1条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
#----------------------------------------------------------
car='subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')
print("\nIs car=='audi' ? I predict False.")
print(car=='audi')
#----------------------------------------------------------
#a.详细研究实际结果，直到你明白了为何它为Trus或False.
#b.创建至少10个测试，且其中结果分别为True和False的测试都至少有5个。
print("测试结果为False：")
print(car=='audia')
print(car=='audib')
print("测试结果为True：")
print(car.title()=='Subaru')
print(car.upper()=='SUBARU')
#5-2更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_test.py中。对于
#下面列出的各种测试。至少编写一个结果为True和False的测试。
#a.检查两个字符串相等和不等。
a='abc'
b='Abc'
print("返回测试为False:")
print(a==b)
print("返回测试为True:")
print(a.title()==b)
print(a==b.lower())
#b.使用函数lower()的测试。
#c.检查两个数字相等、不等、大于、小于、、大于等于和小于等于。
c=5
print("两个数字比较")
print(c==5) #True
print(c!=6) #True
print(c!=5) #False
print(c>=4) #True
print(c<=3) #False
print(c>4) #True
print(c<2) #False
#d.使用关键字and和or的测试。
a=2
b=5
print("使用关键字and和or")
print(a>1 and b<6) #True
print(a<1 or b<4)  #False
#e.测试特定的值是否包含在列表中。
cars=['a','b']
print('a' in cars) #True
#f.测试特定的值是否未包含在列表中。
print('c' not in cars) #True

#5-3外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创一个名为alien_color的变量，并将其设置为‘green’、‘yellow’或‘red’.
#a.编写一条if语句，检查外星人是否是绿色的；如果是就打印一条消息，指出玩家获得了5个点。
#b.编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
print("外星人颜色#1，测试通过，获得5个点")
alien_color='green'
if alien_color=='green':
    print("Get five points")
print("外星人颜色#1，测试未通过，没有输出")
alien_color='red'
if alien_color=='green':
    print("Get five points")
#5-4 外星人颜色#2：像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
#a.如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
#b.如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
#c.编写这个程序的两个版本，在一个版本中执行if代码块，而在另外一个版本中执行else代码块。
print("*************执行if代码快***********")
alien_color='green'
if alien_color=='green':
    print("you get five points")
else:
    print("you get ten points")
print("*************执行else代码快***********")
alien_color='yellow'
if alien_color=='green':
    print("you get five points")
else:
    print("you get ten points")
#5-5外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。
#a.如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
#b.如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
#c.如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
#d.编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
print("*********if-elif-else结构*************")
alien_color='red'
if alien_color=='green':
    print("you get five points")
elif alien_color=='yellow':
    print("you get ten points")
else:
    print("you get fifteen points")
#5-6人生的不同阶段：设置变量age的值，再编写一个if-elif-else结构，根据age的值判断处于人生的哪个阶段。
#a.如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
#b.如果一个人的年龄为2（含）~4岁，就打印一条消息，指出他正蹒跚学步。
#c.如果一个人的年龄为4（含）~13岁，就打印一条消息，指出他是儿童。
#d.如果一个人的年龄为13（含）~20岁，就打印一条消息，指出他是青少年。
#e.如果一个人的年龄为20（含）~65岁，就打印一条消息，指出他是成年人。
#f.如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
age=75
if age<2:
    print("婴儿")
elif 4>age>=2:
    print("蹒跚学步")
elif 13>age>=4:
    print("儿童")
elif 20>age>=13:
    print("青少年")
elif 65>age>=20:
    print("成年人")
else:
    print("老年人")
#5-7喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否包含特定的水果。
#a.将该列表命名为favorite_fruits,并在其中包含三种水果。
#b.编写5条if语句，每条都检查某种水果是否包含列表中，如果包含在列表中，就打印一条消息，如“You really like bananas”
favorite_fruits=['apple','bananas','pear']
if 'apple' in favorite_fruits:
    print("You really like apple.")
if 'bananas' in favorite_fruits:
    print("You really like bananas")
if 'pear' in favorite_fruits:
    print("You really like pear")
if 'mango' in favorite_fruits:
    print("you really like mango")
if 'orange' in favorite_fruits:
    print("you really like orange")
#5-8以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为‘admin’。想象你要编写代码，在每位用户
#登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
#a.如果用户名为‘admin’，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”.
#b.否则打印一条普通的问候消息，如“Hello Eric,thank you for logging in again”.
names=['李明','小花','admin','Eric','丽丽']
for name in names:
    if name=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+name+" ,thank you for logging in again.")
#5-9处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。
#a.如果为空，就打印消息“We need to find some users!”
#b.删除列表中所有的用户名，确定就打印正确的消息。
print("删除列表中的用户名，确保正确打印消息")
names=[]
if names:
    for name in names:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + name + " ,thank you for logging in again.")
else:
    print("we need to find some users!")
#5-10检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
#a.创建一个至少包含5个用户名的列表，并将其命名为current_users。
#b.再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
#c.遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
#d.确保比较时不区分大小写；换句话说，如果用户名John已被使用，应拒绝用户名JOHN.
current_users=['xiaoli','xiaohua','admin','eric','liling']
new_users=['xiaoming','lihua','lili','Eric','liling']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user+" 已存在，请输入别的用户名")
    else:
        print(new_user+"该用户名未被使用，恭喜您可以使用")
#5-11序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
#a.在一个列表中存储数字1~9.
    #b.遍历这个列表。
#c.在循环中使用过一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、4th、5th、6th、7th....
for number in range(1,10):
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(str(number)+'th')