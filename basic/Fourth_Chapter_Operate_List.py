#遍历整个列表：经常需要便利列表的所有元素，对每个元素执行相同的操作。可使用for循环
magicians=['alice','david','carolina']
for magician in magicians:  # 第一步：让Python获取列表magicians中的第一个值，并存储到变量magician中，
    print(magician)   #第二步：让Python打印magician的值，鉴于列表还包含其他值，则返回到循环的第一行：
#关于循环：让计算机自动完成重复工作的常见方式之一。对于列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素，
#另外对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大有帮助。
print("\n")
for magician in magicians:
    print(magician.title()+", that was a great tick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")
print("Thank you,everyone.That was a great magic show!")
#使用循环处理数据是一种对数据集执行整体操作的不错的方式。Python根据缩进来判断代码行与前一个代码行的关系。
print("*************创建数字列表*************")
#使用函数range()创建数字列表：函数range()能够生成一系列的数字。生成的数字集不包括第二个数字
for key in range(0,10):
    print(key)
#可以使用函数list()将range()的结果直接转换为列表。
numbers=list(range(1,5))
print(type(numbers))
print(numbers)
#使用函数range()时，还可指定步长。如打印1~10内的偶数：
even_numbers=list(range(2,11,2))
print(even_numbers)
print("*****************************")
squares=[]
for value in range(1,11):
    squares.append(value**2)
#   square=value**2  #使用临时变量会让代码更易读；视情况看
#   squares.append(square)
print(squares)
#对数字列表执行简单的统计计算
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))   #用函数min()找出列表中最小值
print(max(digits))   #用函数max()找出列表中最大值
print(sum(digits))   #用函数sum()统计列表的总和。
#列表解析：将for循环和创建新元素的代码合并成一行，并自动附加新元素。代码示例如下：
squares=[value**2 for value in range(1,11)]
print(squares)
#而要使用这种语法，首先指定一个描述性的列表名，如squares；然后，指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
#在这个示例中，就是表达式value**2，它是计算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
#************使用列表的一部分****************
#a.切片：要创建切片，可指定要使用的第一个元素的索引和最后一个元素的索引加1，与函数range()一样，Python在达到你指定的第二个索引前面的元
# 素后停止。要输出列表中的前三个元素，需要指定索引0~3，这将输出分别为0、1和2的元素。
players=['charles','martina','michael','florence','eli']
print(players[0:3])   #输出players列表前三个队员的名字
print(players[1:4])   #输出第2到4的运动员的名字。起始索引指定为1，终止索引指定为4.
print(players[:4])    #如果没有指定第一个索引，Python将自动从列表开头开始：
print(players[2:])    #要让切片终止于列表末尾，也可以使用类似的语法。
print(players[-3:])   #负数索引返回离列表末尾相应距离的元素。

print("Here are the first three players on my team:")
for player in  players[:3]:   #for循环中也可以使用切片
    print(player.title())
#在编写Web应用程序时，可使用切片来分页显示信息，并在每页显示数量合适的信息。
#列表的复制：要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让Python创建一个始于第一个元素，
# 终止于最后一个元素的切片，即复制整个列表。
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]   #将my_foods的副本存储到friend_foods，所以是两个列表，而不是单纯的把其中一个列表的值赋值给另外一个列表，
# friend_foods=my_foods    #赋值后，是一个列表，如果一个列表的值改变，则输出还是两个完全一样的列表。
print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)
my_foods.append('ice cream')
friend_foods.append('cannoli')
print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)
#元组:列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。然后，
# 有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
#元组的定义：元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表一样。
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0]=250  #元组是不能修改的列表，如果修改，则会报“TypeError: 'tuple' object does not support item assignment”
#遍历元组中的所有值：像列表一样，也可以使用for循环来遍历元组中的所有值：
for dimension in dimensions:
    print(dimension)
#修改元组变量：虽然不能修改元组的元素，但可以给存储元组的变量赋值，因此，如果要修改前述的元组，可重新定义整个元组：
print("\nOriginal dimensions: ")
for dimension in  dimensions:
    print(dimension)
dimensions=(400,100)
print("\nModified dimensions: ")
for dimension in  dimensions:
    print(dimension)
#相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不可变，可使用元组。

#关于设置代码格式：1.格式设置指南；2.缩进（建议缩进都使用四个空格，在字处理文档中，经常使用制表符而不是空格来缩进）；
# 3.行长（建议每行不超过80字符，在大多数计算机中，终端窗口每行只能容纳79字符，而对于注释的行长不超过72字符）；
# 4.空行（要将程序的不同部分分开，可使用空行，空行不会影响代码的运行，但会影响代码的可读性,Python解释器根据水平缩进情况来解读代码，但不关心垂直间距）；
# 5.其他格式设置指南（PEP8还有很多其他的格式设置建议。）