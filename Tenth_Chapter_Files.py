import json
# 学习处理文件,让程序能够快速地分析大量的数据;你将学习错误处理,避免程序在面对意外情形时崩溃;你将学习异常,它们是Python创建的特殊对象,
# 用于管理程序运行时出现的错误;你还将学习模块json,它让你能够保存用户数据,以免在程序停止运行后丢失.
# 学习处理文件和保存数据可让你的程序使用起来更容易;用户将能够选择输入什么样的数据,以及在什么时候输入;用户使用你的程序做一些工作后,可将程序关闭,
# 以及再接着往下做.学习处理异常可帮助你应对文件不存在的情形,以及处理其他可能导致程序崩溃的问题.这让你的程序在面对错误的数据时更健壮-----不管这些
# 错误数据源自无意的错误,还是源自破坏性程序的恶意企图.你在本章学习的技能可提高程序的实用性/可用性和稳定性.
# ******************************************从文件中读取数据******************************************
# 文本文件可存储的数据量多得难以置信:天气数据/交通数据/社会经济数据/文学作品等.每当需要分析或修改存储在文件中的信息时,读取文件都很有用,对数据分
# 析应用程序来说尤其如此,
# 要使用文本文件的信息,首先需要将信息读取到内存中.为此,你可以一次性读取文件的全部内容,也可以以每次一行的方式逐步读取.
# a.读取整个文件
with open('pi_digits.txt') as file_object:  # txt文件保存到本章程序所在的目录中.
    contents=file_object.read()  #函数read()读取这个文件的全部内容,并将其作为一个长长的字符串存储在变量contents中.read()到达文件末尾时返回
    # 一个空字符串,而将这个空字符串显示出来时就是一个空行.要删除末尾的空行,可在print语句中使用rstrip()
    print(contents.rstrip())
# 要以任何方式使用文件--哪怕仅仅是打印其内容,都得先打开文件,这样才能访问它.函数open()接受一个参数:要打开的文件的名称.Python在当前执行
# 的文件所在的目录中查找指定的文件.关键字with在不再需要访问文件后将其关闭.在则会个程序中,我们注意到调用了open(),但没有调用close();你也可以调用
# open()和close()来打开和关闭文件.但这样做时,如果程序存在bug,导致close()语句未执行,文件将不会关闭.这看似微不足道,但未妥善地关闭文件可能会导致
# 数据丢失或受损.如果在程序中过早地调用close(),你会发现需要使用文件时它已关闭(无法访问),这回导致更多的错误.并非在任何情况下都能轻松确定关闭文件的
# 恰当时机,但通过使用前面所示的结构,可让Python去确定:你只管打开文件,并在需要时使用它,Python自会在合适的时候自动将其关闭.
# b.文件路径:
# 1.相对路径:让Python到指定的位置去查找,而该位置是相对于当前运行的程序所在目录的.
# linux/OS X中,可以这样编写代码:with open('text_files/filename.txt') as file_boject:
# 在Windows系统中的写法:with open('text_files\filename.txt') as file_object:[PS:在文件路径中使用反斜杠(\)而不是斜杠(/)]
# 2.绝对路径:将文件在计算机中的准确位置告诉Python,这样就不用关心当前运行的程序存储在什么地方了.在相对路径不通时,可使用绝对路径.绝对路径通常比
# 相对路径更长,因此将其存储在一个变量中,再将该变量传递给open()会有所帮助.
# Linux和OS X中,绝对路径如:file_path='/home/ehmattes/other_files/text_files/filename.txt'
#   with open(file_path) as file_object
# 而在Windows系统中,则是:file_path='C:\Users\ehmattes\other_files\text_files\filename.txt'
#      with open(file_path) as file_object
# PS:通过使用绝对路径,可读取系统任何地方的文件.就目前而言,最简单的做法是,要么将数据文件存储在程序文件所在的目录,要么将其存储在程序文件所在目录下的一个文件夹中.
# Windows系统有时能够正确地解读文件路径中的斜杠.如果你使用的是Windows系统,且结果不符合预期,请确保在文件路径中使用的是反斜杠.另外,
# 由于反斜杠在Python中被视为转义标记,为在Windows中确保万无一失,应以原始字符串的方式指定路径,即在开头的单引号前加上r.
# c.逐行读取:读取文件时,常常需要检查其中的每一行:你可能要在文件中查找特定的信息,或者要以某种方式修改文件中的文本.要以每次一行的方式检查文件,可对文件对象使用for循环
file_name='pi_digits.txt'
with open(file_name) as file_object:  #关键字with,让Python负责妥善地打开和关闭文件.
    for line in file_object:
        print(line.rstrip())  #print语句会加上一个换行符.rstrip()函数的作用就是消除多余的空白行,
# d.创建一个包含文件各行内容的列表:使用关键字with时,open()返回的文件对象只在with代码块内可用.如果要在with代码块外访问文件的内容,
# 可在with代码块内将文件的各行存储在一个列表中,并在with代码块外使用该列表:可以立即处理文件的各个部分,也可推迟到程序后面再处理.
print("创建一个包含文件各行内容的列表")
file_name='pi_digits.txt'
with open(file_name) as file_object:
    lines=file_object.readlines()  #方法readlines()从文件中读取每一行,并将其存储在一个列表中;

for line in lines:
    print(line.rstrip())
# e.使用文件的内容:将文件读取到内存中后,就可以以任何方式使用这些数据了.
print("使用文件的内容")
file_name='pi_digits.txt'
with open(file_name) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()  #在变量pi_string存储的字符串中,包含原来位于每行左边的空格,为删除这些空格,可使用strip()而不是rstrip()
print(pi_string)
print(len(pi_string))
# PS:读取文本文件时,Python将其中的所有文本都解读为字符串.如果你读取的是数字,并要将其作为数字使用,就必须使用函数int()将其转换为整数,
# 或使用函数float()将其转换为浮点数.
# f.包含一百万位的大型文件:上一个示例代码无需更改,在这里,我们打印小数点后20位,如果太多可能会引起终端不断翻滚
print(pi_string[:22]+".....")  #包含了整数位和小数点
# PS:对于你可处理的数据量,Python没有任何限制;只要系统的内存足够多,你想处理多少都可以.
# g.圆周率值中包含你的生日吗?可将生日表示位一个由数字组成的字符串,再检查这个字符串是否包含在pi_string中;
file_name='pi_digits.txt'
with open(file_name) as file_object:
    lies=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.strip()

# birthday=input("Enter you birthday, in the form mmddy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
# ***********************写入文件***********************
# 保存数据最简单的方式之一是将其写入到文件中.通过将输出写入文件,即便关闭包含程序输出的终端窗口,这些输出也依然存在:你可以在程序结束
# 运行后查看这些输出,可与别人分享输出文件,还可编写程序来将这些输出读取到内存中并进行处理.
# a.写入空文件:要将文件写入文件,你在调用open()时需要提供另一个实参,告诉Python你要写入打开的文件.
file_name='programming.txt'
with open(file_name,'w') as file_object:  #如果文件不存在,则会在当前程序运行的目录下,自动创建一个文件
    file_object.write("I love programming") #在上面创建的文件中,写入内容
    # file_object.write("I love creating new games.")
# 在这个示例中,调用open()时提供了两个实参.第一个实参也是要打开的文件的名称,第二个实参'w'告诉Python,我们要以写入模式打开这个文件.
# 打开文件时,可指定读取模式'r',写入模式'w',附加模式'a'或让你能够读取和写入文件的模式'r',如果你省略了模式实参,Python将以默认的只读模式打开.
# 如果你要写入的文件不存在,在函数open()将自动创建它.然后,以写入'w'模式打开文件时千万要小心,因为如果指定的文件已存在,Python将在返回文件对象前清空该文件.
# PS:Python只能将字符串写入文本文件.要将数值数据存储到文本文件中,必须先使用函数str()将其转换为字符串格式.
# b.写入多行：函数write()不会在你写入的文本末尾添加换行符，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样：
file_name='programming.txt'
with open(file_name,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")  #要让每个字符串都单独占一行，则需要在write()语句中包含换行符，否则两行内容挤在一起
# PS：像现实到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。
# c.附加到文件：如果你要给文件添加内容，而不是覆盖原有的内容，可以以附加模式（'a'）打开文件。你以附加模式打开文件时，Python不会在返回文件对象前清空文件，
# 而你写入到文件的行都将添加到文件末尾。如果指定的文件不存在，Python将为你创建一个空文件。
file_name='programming.txt'
with open(file_name,'a') as file_object:  #指定实参'a'，以便将内容附加到文件末尾，而不是覆盖文件原来的内容。
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in  a browser.\n")#最终的结果是，文件原来的内容还在，它们后面是我们刚添加的内容。
# ***********************异常***********************
# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误，每当发生让Python不知措施的错误时，它都会创建一个异常对象。如果你编写了处理
# 该异常的代码，程序将继续运行，如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
# 异常是使用try-except代码快处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。使用管理try-except代码块时，即便出
# 现异常，程序也将继续运行，现实你编写的友好的错误信息，而不是令用户迷惑的traceback.
# 处理ZeroDivisionError异常
# print(5/0)  #ZeroDivisionError: division by zero
# PS:在上述traceback中，指出的错误ZeroDivisionError是一个异常对象，Python无法按你的要求做时，就会创建这种对象。在这种情况下，Python将停止运行程序，
# 并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。下面我们将告诉Python，发生这种错误时该怎么办；
print("使用try-excep代码块")  #当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
try:
    print(5/0)  #将导致错误的代码块放在try代码块中，如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，
    # Python将查找这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
except ZeroDivisionError:
    print("You can't divide by zero!")
print("\n使用异常避免崩溃")#发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中；
# 如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_number=input("\nFirst number: ")
#     if first_number=='q':
#         break
#     second_number=input("Second number: ")
#     if second_number=='q':
#         break
#     try:
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)
# PS:try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。有时候，
# 有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else中。except代码块告诉Python，如果它尝试运行try代码块中的代码时引发
# 了指定的异常，该怎么办。
# 程序崩溃可不好，但让用户看到traceback也不是好主意。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望
# 他知道的消息。例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码。有时候，训练有素的攻击者可能根据这些信息判断出可对你的
# 代码发起什么样的攻击。
print("else代码块")#通过将可能引起错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。错误是执行除法运算的代码行导致的，
# 因此我们需要将它放到try-except代码块中。这个示例还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
# PS:通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。
print("处理FileNotFoundError异常")
# PS：使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。对于所有这些情形，
# 都可使用try-except代码块以直观的方式进行处理。
file_name='alice.txt'
# with open(file_name) as file_object:  #FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
#     contents=file_object.read()
try:
    with open(file_name) as file_object:
        contents=file_object.read()
except FileNotFoundError:  #如果文件不存在，这个程序什么都不做，
    msg="Sorry, the file "+file_name+" does not exist."
    print(msg)
print("分析文本")
title="Alice in Wonderland"
print(title.split())
#方法split():根据一个字符串创建一个单词列表，以空格为分隔符将字符串拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含字符
# 串中所有单词的列表。虽然有些单词可能包含标点。
file_name='alice.txt'
try:
    with open(file_name) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry,the file "+file_name+" does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words=contents.split()
    num_words=len(words)
    print("The file "+file_name+" has about "+str(num_words)+" words.")
print("使用多个文件")
def count_words(filename):  #定义函数，方便其他人的调用
    """计算一个文件大致包含多少个单词"""
    try:
        with open(file_name) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        # pass #失败时一声不吭
        print("Sorry ,the file "+file_name+" does not exist.")
    else:
        #计算文件大致包含多少个单词
        words=contents.split()  #words为列表
        num_words=len(words)
        print("The file "+file_name+" has about "+str(num_words)+" words.")
a='alice.txt'
count_words(a)
# 例子：现在可以编写一个简单的循环，计算要分析的任何文本包含多少个单词了。为此，我们将要分析的文件的名称存储在一个列表中，然后对列表
# 中的每个文件都调用count_words()函数。
file_names=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for file_name in file_names:
    count_words(file_names)
# 加入siddhartha.txt没有放到程序运行目录下，则输出结果如下：
# The file alice.txt has about 29461 words.
# Sorry,the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 215136 words.
# The file little_women.txt has about 189079 words.
# PS:在这个示例中，使用try-except代码块提供了两个重要的优点：避免让用户看到traceback;让程序能够继续分析，能够找到其他的文件。如果
# 不捕获因找不到siddhartha.txt而引发的FileNotFoundError异常，用户将看到完整的traceback，而程序将在尝试分析siddhartha后停止运行--
# 根本不分析moby_dick.txt和little_women.txt
print("失败时一声不吭")#要让程序失败时一声不吭，可像通常那样编写try代码块，但在except代码块中明确地告诉Python什么都不要做。
# Python有一个pass语句，可在代码块中使用它来让Python什么都不要做；pass语句哎充当了占位符，它提醒你在程序的某个地方什么都没有做，
# 并且以后也要在这里做些什么。
# ************************存储数据************************
# 很多程序都要求用户输入某种信息，程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，你几乎总是要保存他们提供的信息：
# 一种简单的方式是使用模块json来存储数据。
# 模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用json在Python程序之间分享数据。
# 更重要的是,JSON数据格式并非Python专用的，这让你能够以JSON格式存储的数据与使用其他编程语言的人分享。这是一种轻便格式，很有用，也易于学习。
# PS：JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。
print("使用json.dump()和json.load()")
# 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
numbers=[2,3,5,7,11,13]
file_name='number.json'  #通常使用文件扩展名.json来指出文件存储的数据为JSON格式
with open(file_name,'w') as f_obj:
    json.dump(numbers,f_obj)
# 案例分析：我们先导入模块json，再创建一个数字列表。指定了要将该数字列表存储到其中的文件的名称。接下来，我们以写入模式打开这个文件，让json
# 能够将数据写入其中，最后使用函数json.dump()将数字列表存储到文件中。
print("使用json.load()将这个列表读取到内存中")
with open(file_name) as f_obj:
    new_number=json.load(f_obj)  #使用函数json.load()加载存储在numbers.json中的信息，作者是一种在程序之间共享数据的简单方式。
print(new_number)
print("保存和读取用户生成的数据")
# 对于用户生成的数据，使用json保存它们大有裨益，因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
# username=input("What is your name? ")
file_name='username.json'
# with open(file_name,'w') as f_obj:
#     json.dump(username,f_obj)
#     print("We'll remeber you when you come back, "+username+"!")
print("向其名字被存储的用户发出问候：")
with open(file_name) as f:
    username=json.load(f)
    print("Welcome back, "+username+"!")

print("我们将把上面两个程序合并到一个程序种")
try:
    with open(file_name) as f_obj:
        username=json.load(f_obj)  #程序一开始加载信息
except FileNotFoundError:#如果文件不存在，则会新创建这个文件，并让用户输入姓名
    username=input("What's your name? ")
    with open(file_name,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remeber you when you come back,"+username+"!")
else:
    print("Welcome back, "+username+"!")
print("***********************重构********************")
# 你经常会遇到这样的情况：代码能够正确地运行，但可做进一步的改进---将代码划分为一系列完成具体工作的函数。这样的过程被称为重构。
# 重构让代码更清晰、更易于理解、更容易扩展。
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
        print("Wellcome back, "+username+"!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+username+"!")

greet_user()
# PS:重构后的代码，每个函数都执行单一而清晰的任务。我们调用greet_user()，它打印一条合适的消息：要么欢迎老用户回来，要么问候新用户。