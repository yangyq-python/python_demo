# 4-1 披萨：想出至少三种你喜欢吃的披萨，将其名称存储在一个列表中，再使用for循环将每种披萨的名称都打印出来。
pizzas=['a-pizza','b-pizza','c-pizza','d-pizza']
for pizza in  pizzas:
    print(pizza)
#a. 修改这个for循环，使其打印包含披萨名称的句子，而不仅仅是披萨的名称。对于每种披萨，都显示一行输出，如“I like popperon pizza”。
#b. 在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢披萨。输出应包含针对每种披萨的消息，还有一个总结性句子，如“I really love pizza！”。
print("-----------------------------")
for pizza in pizzas:
    print("I like "+pizza.title())
print("I really love pizza!")
# 4-2 动物：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for循环将每种动物的名称都打印出来。
animals=['dog','sheep','horse','cattle']
for animal in animals:
    print(animal)
#a. 修改这个程序，将其针对每种动物都打印一个句子，如“A dog would make a great pet”
#b. 在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。
print("*************************")
for animal in animals:
    print("A "+animal+" would make a great pet.")
print("Any of these animals would make a great pet!")
#4-3 数到20：使用一个for循环打印数字1~20（含）
for a in range(1,21):
    print(a)
#4-4 一百万：创建一个列表，其中包含数字1~1000000，再使用一个for循环将这些数字打印出来（如果输出的时间太长，按Ctr+C停止输出，或关闭输出窗口）。
# for b in range(1,1000001):
#     print(b)
#4-5 计算1~1000000的总和：创建一个列表，其中包含数字1~1000000，再使用min()和max()核实该列表确实是从1开始，到1000000结束。另外，对这个列表调用函数sum(），
#看看Python将一百万个数字相加需要多长时间。
b=list(range(1,1000001))
print(min(b))
print(max(b))
print(sum(b))
#4-6奇数：通过给函数range()指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用有一个for循环将这些数字都打印出来。
for odd_number in range(1,21,2):
    print(odd_number)
#4-7 3的倍数：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for循环将这个列表中的数字都打印出来。
for multiple in range(3,31,3):
    print("3~30中是3的倍数的数字有："+str(multiple))
#4-8 立方：将同一个数字乘三次成为立方。例如，在Python中，2的立方用2**3表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for循环将这
# 些立方数都打印出来。
for cube in range(1,11):
    print(cube**3)
#4-9 立方解析：使用列表解析生成一个列表，其中包含前10个整数的立方。
cubes=[cube**3 for cube in  range(1,11)]
print(cubes)
# 4-10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
my_foods=['pizza','falafel','carrot cake','ice cream','dumplings']
#a. 打印消息"The first thres items in the list are:",再使用切片来打印列表的前三个元素。
a=my_foods[:3]
print("\nThe first thres items in the list are:")
print(a)
#b. 打印消息"Three items from the middle of the list are:",再使用切片来打印列表中间的三个元素。
b=my_foods[1:4]
print("\nThree items from the middle of the list are:")
print(b)
#c. 打印消息“The last three items in the list are:”,再使用切片来打印列表末尾的三个元素。
c=my_foods[-3:]
print("\nThe last three items in the list are:")
print(c)
#4-11 你的披萨和我的披萨：在你为完成练习4-1而编写的程序中，创建披萨列表的副本，并将其存储到变量friend_pizzas中，再完成如下任务：
#a. 在原来的披萨列表中添加一种披萨。
#b. 在列表friend_pizzas中添加另一种披萨。
#c. 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”,再使用一个for循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”,
#再使用一个for循环来打印第二个列表。核实新增的披萨被添加到了正确的列表中。
my_pizzas=['a-pizza','b-pizza','c-pizza','d-pizza']
friend_pizzas=my_pizzas[:]  #创建friend的副本
my_pizzas.append('e-pizza')
friend_pizzas.append('friend_pizza')
print("My favorite pizzas are: ")
print([my_pizza.title() for my_pizza in  my_pizzas])
print("My friend's favorite pizzas are:")
print([friend_pizza  for friend_pizza in friend_pizzas])
#4-12使用多个循环：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for循环来打印消息。请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表都打印出来。
#此处省略。
#4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
#a.使用一个for循环将该餐馆提供的五种食品打印出来。
#b.尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
#c.餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用for循环将新元组的每个元素都打印出来。
foods=('soybean milk','noodle','steamed rice','stir fry','coffee')
for food in foods:
    print(food)
# foods[0]='dumplings'  #TypeError: 'tuple' object does not support item assignment
foods=('orange juice','noodle','steamed rice','dumplings','coffee')
print([new_food for new_food in foods])