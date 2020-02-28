#在程序中可随时修改变量的值，而python将始终记录变量的最新值。
#变量的命名和使用：需要遵守一些规则，如下
#1.变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头。但不能以数字打头，例如，可将变量命名为message_1,但不能将其命名为1_message.
#2.变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
#3.不要将python关键字和函数名用作变量名，既不要使用Python保留用于特殊用途的单词，如print
#4.变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
#5.慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0.
#另外需保持变量名的拼写一致，定义了什么就要使用什么，否则会出现找不到变量："NameError:name 'xxxx' is not defined"【traceback】
message="Hello Python world！"
print(message)
message="Hello Python Crash Course world!"
print(message)
#-----------------------------数据类型--字符串------------------------------#
#数据类型----字符串：就是一系列字符。在Python中，用引号括起的都是字符串，PS：引号可以是单引号或者双引号，下面介绍字符串的操作
#1.修改字符串中每个单词的首字母大写：title（）
#2.修改字符串全部大写：upper（）
#3.修改字符串全部小写：lower()
#4.字符串拼接：Python中使用加号(+)来拼接/合并字符串
name="ada loVelace"
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(name.title())
print(name.upper())
print(name.lower())
print("Hello,"+full_name.title()+"!")
#使用制表符或换行符来添加空白，在编程中空白泛指任何非打印字符，如空格、制表符和换行符。你可使用空白来组织输出以使其更易读。
#1.要在字符串中添加制表符，可使用字符组合\t，
#2.要在字符串中添加换行符，可使用字符组合\n，
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Lanaguages:\n\tPython\n\tC\n\tJavaScript")
#-----------------------------删除空白------------------------------#
#1.删除字符串末尾的空白：rstrip()
#2.删除字符串头部的空白：lstrip()
#3.同时删除字符串头尾空白：strip()
favorite_language='python '
favorite_language1=' python'
favorite_language2=' python '
print(favorite_language,favorite_language1,favorite_language2)
print(favorite_language.rstrip())
print(favorite_language1.lstrip())
print(favorite_language2.strip())
#Python中单双引号在字符串使用时一些问题。转义字符【\】
message="One of Python's strengths is its diverse community."
print(message)
message='One of Python\'s strengths is its diverse community.'
print(message)
#在不同版本中print语句语法稍有不同：如在Python2中,有些print语句包含括号，有些不包含。
#-----------------------------数据类型--数字------------------------------#
# 整数：在Python中，可对整数执行加（+）、减（-）、乘（*）、除（/），PS：两个乘号表示乘方运算。
#Python运算优先级，可在同一个表达式中使用多种运算。可以使用括号来修改运算优先级，让Python按你制定的次序执行运行。
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(2**3)
print((2+3)*4)
#Python将带小数点的数字都成为浮点数。大多数编程语言都使用了这个术语，它指出了这样一个事实：小数点可出现在数字的任何位置。PS:结果包含的小数位数可能是不确定的：
print(0.2+0.1)
#函数str()的使用：避免类型错误
age=23
message="Happy "+str(age)+"rd Birthday!"   #str()函数将int类型的age转换为字符串类型
print(message)
#注释：在Python中，注释用井号（#）标识，井号后面的内容都会被Python解释器忽略。此处不再重复