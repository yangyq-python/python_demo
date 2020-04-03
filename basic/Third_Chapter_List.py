#列表：由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系
#鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters、digits或names）是个不错的注意。
#在python中，用方括号[]来表示列表，并用逗号来分隔其中的元素。
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
#3-1列表元素的访问；PS索引是从0开始而不是1.对于最后一个元素，有一种特殊的语法，将索引指定为-1，即可,当然这种约定也适用于其他负数索引，-2则返回列表中倒数第二个元素
print(bicycles[0])
print(bicycles[0].title())  #title函数让字符串的首字母大写
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
#使用列表中的各个值：可像使用其他变量一样使用列表中的各个值。例如：可以使用拼接根据列表中的值类创建消息。
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)
#3-2 修改、删除、添加元素
#修改列表元素的语法与访问列表元素的语法类似，要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
#在列表中添加元素：
# a.在列表末尾添加元素，用append()函数给列表末尾添加元素；
motorcycles.append('ducati1')
print(motorcycles)
motorcycles0=[]
motorcycles0.append('honda')
motorcycles0.append('yamaha')
print(motorcycles0)
# b.在列表中插入元素，使用insert()方法可在列表的任何位置添加元素，需要指定新元素的索引和值
motorcycles0.insert(0,'suzuki')
print(motorcycles0)
#从列表中删除元素：可以根据位置或值来删除列表中的元素。有几种种方法：
#a. 使用del语句删除元素：如果知道要删除的元素在列表中的位置，可以使用该方法。
del motorcycles0[2]
print(motorcycles0)
#b. 使用pop()删除元素：可删除列表末尾的元素，并让你能够接着使用它【列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。】
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I Owned was a "+popped_motorcycle.title()+".")
#PS:弹出列表中任何位置处的元素，可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
print(motorcycles)
first_owned=motorcycles.pop(0)
print('The first motorcycle I Owned was a '+first_owned.title()+".")
#c. 使用remove()删除元素：根据值删除元素：使用该方法删除元素时，可接着使用它的值。【PS：只删除第一个指定的值，如果要删除的值可能在列表中出现多次，则需要循环来判断】
motorcycles=['honda','yamaha','suzuki','ducati']
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
#组织列表,以下是基于所有值都是小写时，如果在并非所有的值都是小写时，按字母顺序排列要复杂些。
#a.使用方法sort()对列表进行永久性排序：按字母顺序排列,PS:如果需要按字母顺序相反的顺序排列列表元素，为此，只需要向sort()方法传递参数reverse=True
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#b.使用函数sorted()对列表进行临时排序:不影响列表中的原始排序顺序。PS:如果需要按字母顺序相反的顺序排列列表元素，为此，只需要向函数sorted()方法传递参数reverse=True
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("\nHere is the reverse list： ")
print(sorted(cars,reverse=True))
#c.倒着打印列表：使用reverse()，可以反转列表元素的排列顺序。不是指与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。
cars1=['bmw','audi','toyota','subaru']
print(cars1)
cars1.reverse()
print(cars1)
#d.确定列表的长度：使用函数len()可快速获悉列表的长度。
print(len(cars))