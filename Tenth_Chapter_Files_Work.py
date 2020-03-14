import  json

# 10-1Python学习笔记:在文本编辑器中新建一个文件,写几句话来总结一下你至此学到的Python知识,其中每一行都以"In Python you can "打头.将这个
# 文件命名为learning_python.txt,并将其存储到为完成本章练习而编写的程序所在的目录中.编写一个程序,它读取这个文件,并将你所写的内容打印三次:
print("第一次打印时读取整个文件");
file_name='learning_python.txt'
with open(file_name) as file_object:
    print(file_object.read())
print("\n第二次打印时遍历文件对象;")
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
print("\n第三次打印时将各行存储在一个列表中,再在with代码块外打印它们.")
with open(file_name) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
# 10-2C语言学习笔记:可使用方法replace()将字符串中的特定单词都替换为另一个单词.下面是一个简单的示例,演示了如何将句子中的'dog'替换为'cat':
message="I really like dogs."
message.replace('dog','cat')
print(message)
# 请读取你刚创建的文件learning_python.txt中的每一行,将其中的Python都替换为另一门语言的名称,如C.将修改后的各行都打印到屏幕上.
print("用replace()方法把其中的Python替换成C")
for line in lines:
    line=line.replace('Python','C')
    print(line.rstrip())
# 10-3 访客：编写一个程序，提示用户输入其名字；用户作出相应后，将其名字写入到文件guest.txt中。
# message=("please enter your name :")
# file_name='guest.txt'
# with open(file_name,'w') as file_object:
#     message=input(message)
#     file_object.write(message)
# 10-4 访客名单：编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt
# 中。确保这个文件中的每条记录都占一行。
file_name='guest_book.txt'
message = "Please enter your name: "
message += "\nEnter 'q' to end the program."
a=''
# with open(file_name,'a') as file_object:
#     while a != 'q':
#         a = input(message)
#         if a != 'q':
#             print("hello," + a)
#             file_object.write(a + " is comming\n")
# 10-5 关于编程的调查：编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
# file_name='reason.txt'
# message="Why you like programming: "
# reason=''
# with open(file_name,'a') as file_object:
#     while reason!='q':
#         reason=input(message)
#         if reason!='q':
#             file_object.write("喜欢编程的原因是："+reason+"\n")
# 10-6加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，
# 将引发ValueError异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获ValueError异常，
# 并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，在输入一些文本而不是数字。
message="please enter two numbers, enter 'q' will end programming"
# while True:
#     first_number=input("\nfirst_number: ")
#     if first_number=='q':
#         break
#     second_number=input("second_number: ")
#     if second_number=='q':
#         break
#     try:
#         answer=int(first_number)+int(second_number)
#     except ValueError:
#         print("请输入数字")
#     else:
#         print(answer)
# 10-7加法计算器：将你为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
# 同上
# 10-8猫狗：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，
# 尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并打印一条
# 友好的消息。将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。
catsfile_name='cats.txt'
dogsfile_name='dogs.txt'
def read_name(filename):
    """如果文件存在，则读取文件内容，否则报告文件不存在"""
    try:
        with open(filename) as animal_name:
           name=animal_name.read()
    except FileNotFoundError:
        # pass
        print("sorry,"+filename+" does not exist.")
    else:
        print(name)
read_name(catsfile_name)
read_name(dogsfile_name)
# 10-9沉默的猫和狗：修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发。
# 上面注释掉的代码
# 10-10常见单词：访问项目Gutenbery(http://gutenberg.org),并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row'在一个字符串中出现了多少次：
line='Row,row,row your boat'
print(line.count('row'))
print(line.lower().count('row'))
# 请注意，通过使用lower()将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管大小写格式如何。
# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。
message='the,hello,the,The hes'
print(message.count('the'))
print(message.lower().count('the'))
# 10-11喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，
# 并打印消息“I know your favorite number! It's_____.”
file_name='lovenumber.json'
message='Please enter favorite number: '
# with open(file_name,'w') as f:
#     number=input(message)
#     json.dump(number,f)
# with open(file_name) as f:
#     readnumber=json.load(f)
#     print("I know your favorite number! It's "+readnumber+".")
# 10-12记住喜欢的数字：将练习10-11中的两个程序合二为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将
# 其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。
try:
    with open(file_name) as f:
        readnumber=json.load(f)
except FileNotFoundError:
      username=("请输入你喜欢的数字：")
      with open(file_name,'w') as f:
          readnumber=input(username)
          json.dump(readnumber,f)
          # print("")
else:
    print("I know your favorite number! It's "+readnumber+".")
# 10-13 验证用户：最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。我们应修改这个程序，以应对这样的情形：
# 当前和最后一次运行该程序的用户并非同一个人。
#   为此，在greet_user()中打印欢迎用户回来的消息前，先询问他用户名是否是对的。如果不对，就调用get_new_username()让用户输入正确的用户名。
def get_stored_username():
    """如果存储了用户名，就获取它"""
    file_name='username.json'
    try:
        with open(file_name) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名"""
    username=input("What is your name?")
    file_name='username.json'
    with open(file_name,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    username=get_stored_username()
    if username:  #获取到用户名，为真，则执行
        ask="Is the"+username+"correct?"+"(yes or not)"
        if ask=='yes':
            print("Wellcome back, "+username+"!")
        else:
            username=get_new_username()
            print("We'll remember you when you come back, "+username+"!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+username+"!")

greet_user()
