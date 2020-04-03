#编程时经常需要检查一系列条件，并据此决定采取什么措施。在Python中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':   #当汽车的名字是‘bmw’的是，就以全大写的方式打印，
        print(car.upper())
    else:  #否则就以首字母大写的方式打印
        print(car.title())
#每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。Python根据条件测试的值来决定是否执行if语句中的代码。
#如果条件测试的值为True,Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。
#a. 检查是否相等：检查变量的值是否与特定值相等
car='bmw'  #赋值
print(car=='bmw')  #检查是否与特定值'bmw'相等，相等则返回True,否则返回False
print(car=='audi')
#b. 检查是否相等时不考虑大小写:在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等：
car='Audi'
print(car=='audi')   #返回False
print(car.lower()=='audi')   #返回True,[lower()把字符串转换为小写]
#c. 检查是否不相等：要判断两个值是否不等，可结合使用惊叹号和等号（!=），其中的惊叹号标识不，在很多语言中都如此。
requested_topping='mushrooms'
if requested_topping!='anchovies':  #大多数条件表达式都检查两个值是否相等，但有时候检查两个值是否不等的效率更高
    print("Hold the anchovies!")
#d. 比较数字：条件语句中可包含各种数字比较，如小于、小于等于、大于、大于等于：
answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")

age=19
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)
#e. 检查多个条件:有的时候，可能需要同时检查多个条件，例如，有时候你需要在两个条件都为True时才执行相应的操作，而有时候只要求
 # 一个条件为True时就执行相应的操作。这些情况下，就需要关键字and和or
 #1.使用and检查多个条件：要检查是否两个条件都为True,可使用关键字and将两个条件测试合而为一；如果每个测试都通过了，整个表达式
   #就为True，否则为False。
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)  #False
age_1=22
print(age_0>=21 and age_1>=22)  #True
 #使用or检查多个条件：关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没通过时，
 #使用or的表达式才为False.
age_0=22
age_1=18
print(age_0>=21 or age_1>=21) #True
age_0=18
print(age_0>=21 or age_1>=21)  #False
#f. 检查特定值是否包含在列表中:可使用关键字in
print("检查特定值是否包含在列表中")
requested_topping=['mushrooms','onins','pineapple']
print('mushrooms' in requested_topping) #True
print('pepperoni' in requested_topping)  #False
#g. 检查特定值是否不包含在列表中:使用关键字not in
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:  #True
    print(user.title()+", you can post a response if you wish.")
#h. 布尔表达式:是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为True,要么为False；通常用于记录条件
game_active=True
can_endit=False

#----------------------------if 语句----------------------
#a.简单的if语句：最简单的if语句只有一个测试和一个操作：格式如下
# if conditional_test:
#     do somethine
age=19
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
#在if语句中，缩进的作用与for循环中相同，在紧跟在if语句后面的代码块中，可根据需要包含任意数量的代码行
#b.if-else语句：经常需要在条件测试通过了时执行一个操作，并在没有通过时执行另一个操作；在这种情况下，可使用
 #Python提供的if-else语句。if-else语句块类似于简单的if语句，但其中的else语句让你能够指定条件测试未通过时要执行的操作。
age=17
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
#if-else结构非常适合用于要让Python执行两种操作之一的情形。在这种简单的结构种，总是会执行两个操作种的一个。
#c.if-elif-else语句：需要检查超过两个的情形，依次检查每个条件测试，直到遇到通过了的条件测试，测试通过后，Python将执行
 #紧跟在它后面的代码，并跳过余下的测试。
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print("*********************")
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("You admission cost is $"+str(price)+".")
#d.使用多个elif代码块:可根据需要使用任意数量的elif代码块，如下：
print("***********多个elif代码块的使用****************")
age=10
if age<4:
    price=0
elif age<18:
    price=5
elif age<65: #同上一个案例不同的是，细化了一个条件
    price=10
else:
    price=0
print("Your admission cost is $"+str(price)+".")
#e.省略else代码块：Python并不要求if-else结构后面必须有else代码块。在有些情况下，else代码很有用；而在其他一些情况下，
 #使用一条elif语句来处理特定的情形更清晰：
print("**********省略else代码块***********")
age=56
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5
print("Your admission cost is $"+str(price)+".")
#else是一条包罗万象的语句，只要不满足任何if或elif的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终
#要测试的条件，应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。
#f.测试多个条件：if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python就跳过余下的测试。
#这种行为很好，效率很高，让你能够测试一个特定的条件。
 #然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True,
 #且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if  'pepperoni' in requested_toppings:
# elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if  'extra cheese' in requested_toppings:
# elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making you pizza!")

#使用if语句处理列表：可以对列表中特定的值做特殊处理，
#a.检查特殊元素
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out of green pepperrs right now.")
    else:
        print("Adding"+requested_topping+'.')
print("\nFinished making your pizza!")
#b.确定列表不是空的:列表为空的检查很重要
requested_toppings=[]
if requested_toppings:  #这句的作用：在列表至少包含一个元素时返回True，并在列表为空时返回False
    for requested_topping in requested_toppings:
        print("Adding"+requested_topping+'.')
    print("\nFinished making your pizza?")
else:
    print("Are you sure you want a plain npizza?")
#c.使用多个列表
print("使用多个列表")
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+'.')
    else:
        print("Sorry,we don't hava"+requested_topping+'.')
print("\nFinished making your pizza!")