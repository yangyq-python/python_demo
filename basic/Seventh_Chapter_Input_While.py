# 用户输入input工作原理:函数input()让程序暂停运行,等待用户输入一些文本.获取用户输入后,Python将其存储在一个变量中,方便使用.
# message=input("Tell me something, and I will repeat it back to you: ")
# print(message)
#每当你使用函数input()时,都应指定清晰而易于明白的提示,准确地指出你希望用户提供什么样的信息-任何指出用户该输入何种信息的提示都行,
# name=input("Please enter your name: ")
# print("Hello, "+name+"!")
prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your first name?" #创建了一种多行字符串的方式,通过运行费+=在存储在prompt中的字符串末尾附加一个字符串.
# 最终的提示横跨两行,并在问号后面包含一个空格,这也是出于清晰考虑
# name=input(prompt)
# print("\nHello, "+name+"!")

#使用int()来获取数值输入:使用函数input()时,Python将用户输入解读为字符串.
# age=input("How old are you?")
# print(type(age))  #input输入类型为:str
# height=input("How tall are you,in incches?")
# height=int(height) #将数值输入用于计算和比较前,无比将其转换为数值表示.
# if height>=36:
#     print("\nYou are tall enouth to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
#***************求模运算符******************
#处理数值信息时,求模运算符(%)是一个很有用的工具,它将两个数相除并返回余数;
print(4%3)
print(6%3)
#求模运算符不会指出一个数是另一个数的多少倍,而只指出余数是多少.
# 如果一个数可被另一个数整除,余数就是0,因此求模运算符将返回0,可以利用这一点来判断一个数是奇数还是偶数:
# number=input("Enter a number, and I'll tell you if it's even or odd: ")
# number=int(number)
# if number%2==0:  #偶数都能倍2整除,因此对一个数和2执行求模运算符的结果为零,那么这个数就是偶数;否则就是奇数.
#     print("\nThe number "+str(number)+" is even.")
# else:
#     print("\nThe number "+str(number)+" is odd.")

#如果使用的是Python2.7,应使用函数raw_input()来提示用户输入.这个函数与Python3中的input()一样,也将输入解读为字符串.

# ****************while循环简介****************
# for循环用于针对集合中的每个元素的一个代码块,而while循环不断地运行,直到指定的条件不满足为止,
# a.使用while循环:可以使用while循环来数数
current_number=1
while current_number<=5:  #只要current_number小于或等于5,就接着运行这个循环
    print(current_number) #循环中的代码运行current_number的只,
    current_number+=1  #将其值+1
# b.让用户选择何时退出:可使用while循环让程序在用户愿意时不断地运行,如下面的程序,只要用户输入的不是这个值,就接着运行
prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nEnter 'quit' to end the program."
# message=""  #首次执行while代码行时有可供检查的东西,因为需要将message值与quit进行比较,但此时用户还没有输入,所以必须指定一个初始值
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':  #程序在显示消息前将做简单的检查,仅在消息不是quit值才打印它:
#       print(message)
# c.使用标志:在要求很多条件都满足才继续运行的程序中,可定义一个变量,用于判断整个程序是否处于活动状态.这个变量被称为标志,充当了程序的信号灯,
# 你可让程序在标志为True时继续运行,并在任何事件导致标志值为False时让程序停止运行.这样,在while语句中就只需要检查一个条件-----标志的当前值是否是True,
# 并将所有测试(是否发送了应将标志设置为False的事件)都放在其他地方,从而让程序变得更为整洁.
# active=True   #让程序最初处于活动状态,这样做简化了while语句,因为不需要在其中做任何比较-相关的逻辑由程序的其他部分处理.
# while active:
#     message=input(prompt)  #用户输入
#     if message=='quit':  #在用户输入后,使用if语句来检查变量message的值
#         active=False    #如果用户输入的是quit,active的值将变成False,这将导致while循环不再继续执行.
#     else:
#         print(message)
#     print(active)  #可以在每次循环结束查看该值
# d.使用break退出循环:要立即退出while循环,不再运行循环中余下的代码,也不管条件测试的结果如何,可使用break语句,break语句用于控制程序流程,
# 可使用它来控制那些代码行将执行,哪些代码行不执行,从而让程序按你的要求执行你要执行的代码.
# prompt="If you tell us who you are, we can personalize the messages you see."
# prompt+="\nEnter 'quit' when you are finished."
# while True:
#     city=input(prompt)
#     if city=='quit':
#         break   #在任何Python循环中都可以使用break语句.例如,可使用break语句来退出遍历列表或字典的for循环.
#     else:
#         print("I'd love to go to "+city.title()+"!")
# e.在循环中使用continue:要返回到循环开头,并根据条件测试结果决定是否继续执行循环,可使用continue语句,
# 它不像break语句那样不再执行余下的代码并退出整个循环.
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:  #求1~10之间的奇数,能被2整除,则结束本次循环,跳出本次循环,继续执行下次循环.
        continue
    print(current_number)
# f.避免无限循环:每个while循环都必须有停止运行的途径,这样才不会没完没了地执行下去.
x=1
while x<=5:
    print(x)
    x+=1   #如果不小心遗漏该行代码,则循环将会没完没了的执行下去
#如果陷入无限循环,可按Ctrl+C,也可关闭显示程序输出的终端窗口.要避免编写无限循环,务必对每个while循环进行测试,确保它按预期那样结束.
# 如果你希望程序在用户输入特定值时结束,可运行程序并输入这样的值;如果在这种情况下程序没有结束,请检查程序处理这个值的方式,确认程序
# 至少有一个这样的地方能让循环条件为False或break语句得以执行.
#有些编辑器(如Sublime Text)内嵌了输出窗口,这可能导致难以结束无限循环,因此不得不关闭编辑器来结束无限循环.

#******************使用while循环来处理列表和字典***************
#for和while循环的区别:for循环是一种遍历列表的有效方式,但在for循环中不应修改列表,否则讲导致Python难以跟踪其中的元素.
# 要在遍历列表的同时对其进行修改,可使用while循环.通过将while循环同列表和字典结合起来使用,可收集,存储并组织大量输入,
# 供以后查看和现实.
# a.在列表之间移动元素:
unconfirmed_users=['alice','brian','candace'] #首先,创建一个待验证用户列表
confirmed_users=[]  #和一个用于存储已验证用户的空列表
while unconfirmed_users:
    current_user=unconfirmed_users.pop() #pon()以每次一个的方式从列表unconfirmed_users末尾删除未验证的用户.
    print("Verifying usre: "+current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# b.删除包含特定值的所有列表元素:在之前学习过remove()来删除列表中的特定值,这之所以可行,是因为要删除的值在列表中只出现
# 一次.如果要删除列表中所有包含特定值的元素,如下:
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:  #不断删除cat,直到这个值不再包含在列表中,然后退出循环并再次打印列表:
    pets.remove('cat')

print(pets)
# c.使用用户输入来填充字典:可使用while循环提示用户输入任意数量的信息.
responses={}
polling_active=True #设置一个标志,指出调查是否继续

while polling_active:
    name=input("\nWhat is your name ?")
    response=input("Whice mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/no)")
    if repeat=='no':
        polling_active=False
print("\n-----Poll Results ----")

for name,response in responses.items():
    print(name+" Would like to climb "+response+" .")