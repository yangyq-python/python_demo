#3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names=['xiaohong','xiaoming','xiaoli','xiaoning','xiaohua']
for name in names:
    print(name)
#3-2 问候语：继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for name in names:
    print("Hello "+name)
#3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言
# ，如“I would like to own a Honda mmotorcycle”
commutes=['bus','mmotorcycle','run','bike']
for commute in commutes:
    if commute=='mmotorcycle':
        print("I would like to own a Honda mmotorcycle")
    elif commute=='bus':
        print("I would like to own a Toyota bus")
    elif commute=='bike':
        print("I would like to own a bike sharing")
    else:
        print("I would like to running to work")
#3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请那些人？请创建一个列表，其中包含至少3个你想邀请的人；
# 然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
name_lists=['xiaodong','xiaonan','xiaoxi','xiaobei']
print('Welcome '+ name_lists[0]+' having dinner together')
for name_list in name_lists:
    print('welcome '+name_list+' having dinner together.')
print("I have invited "+str(len(name_lists)) +" having dinner together.")
#3-5修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
#a.以完成练习3-4时编写的程序为基础，在程序末尾添加一条print语句，指出哪位嘉宾无法赴约。
print("But xiaobei  can't come to the appointment ")
#b.修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
del name_lists[-1]
name_lists.append('new_xiaobei')
print(name_lists)
#c.再次打印一系列消息，向名单中的每位嘉宾发出邀请。
for new_name_list in name_lists:
    print('Welcom '+new_name_list +' having dinner together.')
#3-6添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
#a.以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print语句，指出你找到了一个更大的餐桌。
print("I find one bigger table,can sit a lot of people.")
#b.使用insert()将一位新嘉宾添加到名单开头。
name_lists.insert(0,'new_guest01')
#c.使用insert()将另一位新嘉宾添加到名单中间。
name_lists.insert(3,'new_guest02')
#d.使用append()将最后一位新嘉宾添加到名单末尾。
name_lists.append('new_guest03')
print(name_lists)
#3-7缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
#a.以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
print("The new table couldn't arrive in time. I had to invite two people.")
#b.使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
print("Sorry " + name_lists.pop(0) + " can't invite you to dinner")
print("Sorry " + name_lists.pop(0) + " can't invite you to dinner")
print("Sorry " + name_lists.pop(0) + " can't invite you to dinner")
print("Sorry " + name_lists.pop(0) + " can't invite you to dinner")
print("Sorry " + name_lists.pop(0) + " can't invite you to dinner")
# print(name+", It's pleasure to invite you to dinner")
#c.对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
print(name_lists)
print(name_lists[0]+", It's pleasure to invite you to dinner")
print(name_lists[1]+", It's pleasure to invite you to dinner")
#d.使用del将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
del name_lists[0]
del name_lists[0]
print(name_lists)
#3-8放眼世界：想出至少5个你渴望取旅游的地方。
#1.将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
a=['huangshan','shanghai','beijing','tianjin']
#2.按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
print(a)
#3.使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(a))
#4.再次打印该列表，核实排列顺序未变。
print(a)
#5.使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print("\nHere is sorted.reverse list:")
print(sorted(a,reverse=True))
#6.再次打印该列表，核实排列顺序未变。
print(a)
#7.使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
a.reverse()
print("\nHere is reverse list:")
print(a)
#8.使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
a.reverse()
print("\nHere is original list again:")
print(a)
#9.使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
a.sort()
print("\nHere is sort list:")
print(a)
#10.使用sort()修改该列表，使其元素按字与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
a.sort(reverse=True)
print("\nHere is sort.reverse list:")
print(a)
#3-9完成嘉宾：在完成练习3-4~练习3-7时编写的程序之一中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
#3-10尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
#此处不再重复
