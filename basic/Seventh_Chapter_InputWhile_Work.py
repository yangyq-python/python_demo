# 7-1汽车租赁:编写一个程序,询问用户要租赁什么样的汽车,并打印一条消息,如"Let me see if I can find you a Subaru".
# car_rental=input("Hello! what kind of car to rent?")
# print("Let me see if I can find you a "+car_rental.title())
# 7-2餐馆订位:编写一个程序,询问用户有多少人用餐.如果超过8人,就打印一条消息,指出没有空桌;否则指出有空桌.
# table_reservation=input("\nHow many people do you have?")
# if int(table_reservation)>8:
#     print("There is no empty table.")
# else:
#     print("There is free table!")
# 7-3 10的整数倍:让用户输入一个数字,并指出这个数字是否是10的整数倍.
# number=input("Please enter a number,I will tell you if it is an integral multiple 10?")
# if int(number)%10==0:
#     print(number+" is integral multiple 10.")
# else:
#     print(number+" is not integral multiple 10.")
# 7-4 披萨配料:编写一个循环,提示用户输入一系列的披萨配料,并在用户输入quit时结束循环.每当用户输入一种配料后,都打印一条消息,说我们会在
# # 披萨中添加这种配料.
# input_message=("please input pizza ingredients?")
# message=''
# while message!='quit':
#     message=input(input_message)
#     if message!='quit':
#         print("We will add this "+message+" into pizza!")
# 7-5电影票:有家电影院根据观众的年龄收取不同的票价:不到3岁的观众免费;3~12岁的观众为10美元;超过12岁的观众为15美元.请编写一个循环,在其中询问
# 用户的年龄,并指出其票价.
# inpu_message=("what is your age?")
# while True:
#     age = input(inpu_message)
#     if age=='quit':
#         break
#     elif int(age)<3:
#         print("免费")
#     elif int(age)>=3 and int(age)<12:
#         print("票价为10美元")
#     else:
#         print("票价为15美元")
# 7-6三个出口:以另一种方式完成练习7-4或练习7-5,在程序中采取如下所有做法.
# # a.在while循环中使用条件测试来结束循环.
# _message = "please input your age?"
# while True:
#     age=input(_message)
#     if age=='exit':
#         break
#     else:
#         age=int(age)
#         if age<3:
#             print("免费")
#         elif age<12:
#             print("10美元")
#         else:
#             print("15美元")
# b.使用变量active来控制循环结束的时机
# c.使用break语句在用户输入quit时退出循环
# 7-7无限循环:编写一个没完没了的循环,并运行它(要结束该循环,可按Ctrl+C,也可关闭显示输出的窗口)
#此处省略
# 7-8熟食店:创建一个名为sandwhich_orders的列表,在其中包含各种三明治的名字;再创建一个名为finished_sandwhiches的
# 空列表.遍历列表sandwhich_orders,对于其中的每种三明治,都打印一条消息,如I made your tuna sandwhich,并将其移到列表
# finished_sandwhiches.所有三明治都制作好后,打印一条消息,将这些三明治列出来.
sandwhich_orders=['a-san','b-san','c-san']
finished_sandwhiches=[]
while sandwhich_orders:
    curren_sandwhich=sandwhich_orders.pop()
    print("I made your "+curren_sandwhich.title() +" sandwhich")
    finished_sandwhiches.append(curren_sandwhich)

#打印移到finished_sandwhiche列表中的三明治
print("\nThe following sandwhich have been confirmed: ")
for finished_sandwhiche in finished_sandwhiches:
    print(finished_sandwhiche)
# 7-9五香烟熏牛肉(pastrami)卖完了:使用为完成练习7-8而创建的列表sandwhich_orders,并确定pastrami在其中至少出现了三次.
# 在程序开头附近添加这样的代码:打印一条消息,指出熟食店的五香烟熏牛肉卖完了;再使用一个while循环将列表sandwhich_orders
# 中的pastrami都删除.确认最终的列表finished_sandwiches中不包含pastrami.
n=1
while n<4:  #往列表中添加3此pastrami
     finished_sandwhiches.append('pastrami')
     n+=1
print(finished_sandwhiches)
print("\nI'm sorry,the spiced smoked beef is sold out")
while 'pastrami' in finished_sandwhiches:
    finished_sandwhiches.remove('pastrami')
print(finished_sandwhiches)
# 7-10梦想的度假胜地:编写一个程序,调查用户梦想的度假胜地.使用类似于"If you could visit one place in the world, where
#  would you go?"的提示,并编写一个打印调查结果的代码块.
resort_surveys=[]
message=("\nIf you could visit one place in the world, where would you go?")
while True:
    city=input(message)
    if city=='no':
        break
    else:
        resort_surveys.append(city)
        print("I'd love to go to "+city.title()+"!")
#打印最终的调查结果
print("\nsome of your favorite  resorts are: "+str(resort_surveys))