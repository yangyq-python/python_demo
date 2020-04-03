# 函数简介:函数是带名字的代码块,用于完成具体的工作.要执行函数定义的特定任务,可调用该函数.需要在程序中多次执行同一项任务时,
# 你无需反复编写完成该任务的代码,而只需要调用执行该任务的函数,通过使用函数,程序的编写、阅读、测试和修复都将更容易。
def greet_user():  #使用关键字def来告诉Python你要定义一个函数。这是函数定义，指出了函数名，还可能在括号内指出函数为完成
    # 其任务需要什么样的信息。最后，定义以冒号结尾。而紧跟在函数后面的所有缩进行构成了函数体
    """显示简单的问候语！"""   #文档字符串“docstring”的注释，描述了函数是做什么的，文档字符串用三引号括起，
    print("Hello!")  #函数体内的代码行
#要使用这个函数，可调用它。可依次指定函数名以及用括号括起的必要信息，当前这个函数不需要任何信息
greet_user() #调用函数

# a.向函数传递信息：
def greet_user(username): #可让函数接受指定的任何值
    """显示简单的问候语"""
    print("Hello, "+username.title()+" !")
#如果调用的时候，不传入参数，则出现“TypeError: greet_user() missing 1 required positional argument: 'username'”
greet_user('恬恬')
# b.实参和形参
#形参：上面的变量username就是一个形参：函数完成其工作所需的一项信息。
#实参：而调用函数输入的参数'恬恬'就是实参，调用函数时传递给函数的信息【通过函数的调用，将实参传递给函数，并存储在形参中】
#**********************传递实参***********************
# 鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可使用位置实参，则要求实参的顺序与形参
# 的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可以使用列表和字段。
# 1.位置实参：调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。
# 这种关联方式被称为位置实参。
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+" .")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
# 1.1 调用函数多次:可以根据需要调用函数任意次。
describe_pet('dog','willie')
# 调用函数多次是一种效率极高的工作方式。我们只需在函数中编写描述宠物的代码依次，然后每当需要描述新宠物时，都可以调用这个函数，并向它
# 提供新宠物的信息。即便描述宠物的代码增加到了10行，依然只需使用一行调用函数的代码，就可描述一个宠物
# 在函数中，可根据需要使用任意数量的位置实参，Python将按顺序将函数调用中的实参关联到函数定义中相应的形参
# 1.2 位置实参的顺序很重要：使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料：
describe_pet('harry','hamster') #结果与上面相反，不是想要的结果
#所以在位置实参的传递时，需要确认函数调用中实参的顺序与函数定义中形参的顺序一致。
# 2. 关键字实参：是传递给函数的名称-值对。可以直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆(不会出现上述一样的问题)。
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
describe_pet(pet_name='harry',animal_type='hamster')  #使用关键字实参时，务必准确地指定函数定义中的形参名。
describe_pet(animal_type='hamster',pet_name='harry') #两个函数调用结果等同
# 3. 默认值：在编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。
# 因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
def describe_pet(pet_name,animal_type='dog'):  #和前面的定义相比，修改了形参的排列顺序。由于给animal_type指定了默认值，无需通过实参来
    # 指定动物类型，因此在函数调用中只包含一个实参-宠物的名字。然后Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，
    # 这个实参将关联到函数定义的第一个形参。这就是需要将pet_name放在形参列表开头的原因所在。
    """显示宠物的信息"""
    print("\nI have a "+animal_type+" .")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('whille')  #函数中已经指定另外一个形参的值，
describe_pet(pet_name='harry',animal_type='hamster')  #由于显式地给animal_type提供了实参，因此Python将忽略这个形参的默认值。
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。
# 4. 等效的函数调用：鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式
describe_pet('whille')
describe_pet(pet_name='whi1le')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
#以上这些调用跟之前的例子输出结果都一样
#使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行，使用对你来说最容易理解的调用方式即可。
# 5. 避免实参错误：等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多于或少于函数完成其工作所需的信息时，将出现实参
# 不匹配错误。注意Traceback提示信息。
# describe_pet()
# Traceback (most recent call last):
#   File"Eighth_Chapter_Function.py", line 62, in < module >
#    describe_pet()
# TypeError: describe_pet() missing 1 required positional argument: 'pet_name'

#********************************返回值************************************
# 函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值称为返回值。在函数中，可使用return语句将值返回
# 到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。
# a.返回简单值:
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+' '+last_name   #将姓和名合二为一，中间加上一个空格，并将结果存储在变量full_name中
    return full_name.title()    #将full_name的值转换为首字母大写格式，并将结果返回到函数调用行

musician=get_formatted_name('jimi','hendrix')  #调用返回值的函数时，需要提供一个变量，用于存储返回的值
print(musician)
# b.让实参变成可选的：有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
def get_formatted_name(first_name,last_name,middle_name=''): #为了让middle_name变成可选的，需指定一个默认值(空字符串)，在用户没有
    # 提供中间名时不使用这个形参，并将其移到形参列表的末尾：
    """返回整洁的姓名"""
    if middle_name:  #在函数体中，我们检查是否提供了中间名。Python将非空字符串解读为True,
         full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('john','hooker','lee')#调用该函数的时候，再需要指定中间名时，就必须确保它是最后一个实参，这样Python
 # 才能正确地将位置实参关联到形参
musician1=get_formatted_name('li','ming')
print("\n"+musician)
print(musician1)
#可选值让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。
# c.返回字典：函数可返回任何类型的值，包括列表和字典等复杂的数据结构。
def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person={'first':first_name,'last':last_name} #该函数在接受名和姓，并将这些值封装到字典中，
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix')
# musician1=build_person('jimi','hendrix','27')
musician1=build_person('jimi','hendrix',age=27)
print(musician)
print(musician1)
# d.结合使用函数和while循环:
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+' '+last_name
    return full_name.title()
# while True:
#     print("\nPlease tell me you name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name=input("First_name:")
#     if f_name=='q':
#         break
#     l_name=input("Last_name:")
#     if l_name=='q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print("\nHello, "+formatted_name+'!')
# ***********************传递列表**********************
# 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（字典），将列表传递给函数后，函数就能直接访问其内容
def greet_users(names):  #定义成一个接受名字的列表，存储在names中，
    """向列表中的每位用户都发出简单的问候"""
    for name in names:  #遍历列表
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)
# a.在函数中修改列表：将列表传递给函数后，函数就可对其进行修改，字函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。
unprinted_designs=['iphone case','robot pendant','dodecahedron']  #创建一个列表，其中包含一些要打印的设计
completed_models=[]
# 模拟打印每个设计，直到没有未打印的设计为止，打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     #模拟根据设计制作3D打印模型的过程
#     print("Printing model:"+current_design)
#     completed_models.append(current_design)
# #显示打印好的所有模型
# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)
#以下用两个函数来重新组织这些代码
def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
#调用上面两个函数
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
# 每个函数都应只负责一项具体的工作。第一个函数打印每个设计，第二个显示打印好的模型；这优于使用一个函数来完成两项工作。编写函数的时候，
# 会发现执行的任务太多，那么就尝试将这些代码划分到两个函数中，PS：总是可以在一个函数中调用另外一个函数，有助于将复杂的任务划分成一系列的步骤。
# b.禁止函数修改列表:有时候，需要禁止函数修改列表，比如上面的例子，需要保留原理的未打印的设计列表，以供备案。但是由于将所有的设计都移出
# 了，列表变为空的了，原来的列表没有了，为了解决这个问题，可向函数传递列表的副本而不是原件；这样函数的修改只影响副本，不影响原件。
# function_name(list_name[:]) #将列表的副本传递给函数，切片表示法[:]创建列表的副本
print_models(unprinted_designs[:],completed_models)
#虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免
# 花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。
# *********************传递任意数量的实参**********************
# 有时候，由于预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
def make_pizza(*toppings):  #形参名*toppings中的星号，让Python创建一个名为toppings的空元组，并将收到的所有值都封装到指责换个元组中
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#现在，将上述函数中的printy语句替换为一个循环，对配料列表进行遍历，并对顾客点的披萨进行描述：
def make_pizza_01(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza_01('pepperoni')
make_pizza_01('mushrooms','green peppers','extra cheese')
# a.结合使用位置实参和任意数量实参:如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位
# 置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza_02(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a "+str(size)+"-inch pizza with the following topping:")
    for topping in toppings:
        print("-"+topping)
make_pizza_02(16,'pepperoni')
make_pizza_02(12,'mushrooms','green peppers','extra cheese')
# b.使用任意数量的关键字实参。
# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键-值对---
# 调用语句提供了多少就接受多少。
def build_profile(first,last,**user_info):#要求提供名和姓，同时允许用户根据需要提供任意数量的名称-值对，形参**user_info的两个星号让
    # Python创建一个名为user_info的空字典，并将收到的所有名称-值对都封装到这个字典中，在这个函数中，可以像访问其他字典那样访问user_info中的名称-值对。
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={} #存储用户简介。
    profile['first']=first  #将名和姓加入到这个字典总，总是会从用户那里收到这两项信息
    profile['last']=last
    for key,value in user_info.items():  #遍历字典user_info中的键-值对，
        profile[key]=value  #将每个键-值对都加入到字典profile中。
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
#编写函数时，可以以各种方式混合使用位置实参、关键字实参和任意数量的实参。知道这些实参类型大有裨益，因为阅读别人编写的代码时经常会见到它们。
# 要正确地使用这些类型的实参并知道它们的使用时机，需要经过一定的练习。
# ******************将函数存储在模块中*********************
# 函数的优点之一是，使用它们可将代码与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以更进一步，将函数存储在被称为模块
# 的独立文件中。再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。
# 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑商。这还能让你在众多不同的程序中重用函数，将函数存储在独立文
# 件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。
# a.导入整个模块：要让函数是可导入的，得先创建模块，模块是扩展名为.py的文件，包含要导入到程序中的代码。要调用被导入的模块中的函数，可指定导入的
# 模块的名称和函数名，并用句点(.)分隔它们，
# 这是一种导入方法：只需编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果使用这种import语句导入了整个模块，就可使用
# 如下的语法来使用其中任何一个函数：
# module_name.function_name()
# b.导入特定的函数:还可以导入模块中的特定函数，这种导入方法的语法：
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import  function_0,function_1,function_2
# PS:若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显式地导入了函数，因此调用它时只需指定其名称。
# c.使用as给函数指定别名：如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的命名太长，可指定简短而独一无二的别名--函数的另一个名称，
# 类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。指定别名的语法如下：
# from module_name import function_name as fn
# d.使用as给模块指定别名:还可以给模块指定别名，通过给模块指定简短的别名（如给模块pizza指定别名p）,让你能够更轻松地调用模块中的函数。给模块指定
# 别名的通用语法如下：import module_name as mn
# e.导入模块中的所有函数:使用星号（*）运算符可让Python导入模块中的所有函数：from module_name import *
# import 语句中的幸好让Python将模块中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
# 然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法；如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python
# 可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。
# 这能让代码更清晰，更容易阅读和理解。
# **************函数编写指南***********
# 编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。
# 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它；
# 他们完全可以详细代码如描述的那样运行；只要知道函数的名称，需要的实参以及返回值的类型，就能在自己的程序中使用它。
# def function_name(parameter_0,parameter_1='default value')  #给形参指定默认值时，等号两边不要有空格；
# function_name(value_0,parameter_1='value')  #对于函数调用中的关键字实参，也应遵循这种约定：
# ps:如果形参很多，导致函数定义的长度超过了79个字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和只缩进一层的函数体区分开来。
# 大多数编辑器都会自动对齐后续参数列表行，使其缩进程度与你给第一个参数列表行指定的缩进程度相同：
# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。
# 所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。
