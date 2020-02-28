#2-3个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric,would you like to learn some Python today?”
name="Eric"
print("Hello"+' '+name+','+'would you like to learn some Python today?')
#2-4调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name='tian tian'
print(name.lower())
print(name.upper())
print(name.title())
#2-5 名言：找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似下面这样（包括引号）：
# Albert Einstein once said，“A person who never made a mistake never tried anything new.”
name='Albert Einstein'
# mingyan='A person who never made a mistake never tried anything new.'
print(name+' '+'once said'+'，'+'“A person who never made a mistake never tried anything new.”')
#2-6 名言2：重复练习2-5，但将名人的姓名存储在变量famous_person中，再创建要显示的消息，并将其存储在变量message中，然后打印这消息。
famous_person='Albert Einstein'
message='A person who never made a mistake never tried anything new.'
print(famous_person+' '+'once said'+'，'+'“'+message+'”')
#2-7剔除名人中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip（）、rstrip()、strip()对人名进行处理，并将结果打印出来。
name=' tian tian  '
print('\t'+name)
print('\n'+name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#2-8 数字8：编写4个表达式，它们分别使用加法、减法、乘法、除法运算，但结果都是8.为使用print语句来显示结果，务必将这些表达式用括号括起来，
# 也就是说，你应该编写4行类似这样的代码：print(5+3),输出应为4行，其中每行都只包含数字8.
print(5+3)
print(9-1)
print(2*4)
print(int(8/1))
print(2**3)
#2-9 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
number=6
message='My favorite number is :'+str(number)
print(message)