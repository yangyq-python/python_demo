from collections import OrderedDict
# 面向对象编程是最有效的然间编写方法之一。在面向对象编写中，你编写表示现实世界中的事务和情景的类，并基于这些类来创建对象。编写类时，
# 定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为。然后可根据需要赋予每个对象独特的个性。使用面向对象
# 编程可模拟现实情景，其逼真程度达到了令人惊讶的底部。
# 根据类来创建对象被称为实例化，这让你能够使用类的实例。在本章中，你将编写一些类并创建其实例。
# 理解面向对象编程有助于你像程序员那样看世界，还可以帮助你真正明白自己编写的代码；不仅是各行代码的作用，还有代码背后更宏大的概念。
# 了解类背后的概念可培养逻辑思维，让你能够通过编写程序来解决遇到的几乎任何问题。
# **************创建和使用类***********
# 创建Dog类
class Dog(): #首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类。
    """一次模拟小狗的简单尝试"""   #用一个文档字符串，对这个类的功能作了描述
    def __init__(self,name,age):  #类中的函数称为方法，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
        # 包含三个形参，形参self必不可少，还必须位于其他形参的前面。self是一个指向实例本身的引用，让实例能够访问类中的属性和方法。当我们通过
        # 实参向Dog类传递名字和年龄；self会自动传递，因此我们不需要传递它，只需要给后面两个形参提供值即可
        """初始化属性name和age"""
        self.name=name   #此处定义的两个变量都有前缀self，以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变
        # 量。self.name=name获取存储在形参name中的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例。
        self.age=age
#有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")
#在Python2中创建类时，需要作细微的修改---在括号内包含单词object:[class ClassName(object)]
# a.根据类创建实例：可将类视为有关如何创建实例的说明
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
#命名约定很有用：我们通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（my_dog）指的是根据类创建的实例
# 访问属性：要访问实例的属性，可使用句点表示法，句点表示法在Python中很常用，这种语法演示了Python如何获悉属性的值。
# 调用方法：可指定实例的名称（这里是my_dog）和要调用的方法，并用句点分隔它们。这种语法很有用，如果个属性和方法指定了合适的描述性名称，
# 即便是从未见过的代码块，我们也能够轻松地推断出它是做什么的。
my_dog.sit()  #Python在类Dog中查找方法sit()并运行其代码。Python以同样的方式解读代码my_dog.roll_over().
my_dog.roll_over()
# 创建多个实例：可按需求根据类创建任意数量的实例
your_dog=Dog('lucy',3)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()

print("\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()
#就算我们给第二条小狗指定同样的名字和年龄，Python依然会根据Dog类创建另一个实例。你可按需求根据一个类创建任意数量的实例，条件是将每个
# 实例都存储在不同的变量中，或占用列表或字典的不同位置。
# *********************使用类和实例***********************
# 你可以使用类来模拟现实世界中的很多情景。类编写好，你的大部分时间都将花在使用根据类创建的实例上。你需要只需一个重要任务是修改实例的属性。
# 你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def fill_gas_tank(self):
        """汽车有油箱"""
        print("This car  need a gas tank!")

my_new_car=Car('audi','a4',2016)
print("\n"+my_new_car.get_descriptive_name())
# 给属性指定默认值：类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__()内指定这种初始值
# 是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
class New_Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):  #通过方法修改属性的值
        """将里程表读数设置为指定的值"""
        # self.odometer_reading=mileage
        """
        将里程表读数据设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage>=self.odometer_reading:
            #在修改属性前检查指定的读数是否合理。如果新指定的里程(mileage)大于或等于原来的里程（self.odometer_reading），就将里程表读数改为新指定的里程；
            self.odometer_reading=mileage  #否则就发出警告，指出不能将里程表往回拨
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles>0:
           self.odometer_reading+=miles
        else:
            print("里程表读数增加值必须大于0")

my_car=New_Car('audi','a4',2016)
print(my_car.get_descriptive_name())
my_car.read_odometer()
# ***********************修改属性的值*************************
# a.直接修改属性的值：要修改属性的值，最简单的方式是通过实例直接访问它。
print("直接修改属性的值")
my_car.odometer_reading=23 #使用句点表示法来直接访问并设置汽车的属性odometer_reading。
my_car.read_odometer()
# b.通过方法修改属性的值：如果有替你更新属性的方法，将大有裨益。这样你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
print("通过update_odometer()方法来修改属性值")
my_car.update_odometer(56)
my_car.read_odometer()
print("对方法update_odometer()进行扩展，使其在修改里程表读数据时做些额外的工作")  #见上面的if-else语句的判断
# c.通过方法对属性的值进行递增:有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
my_used_car=New_Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# ****************************************继承***********************************************
# 编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；
# 原有的类称为父类，而新类成为字类。字类继承了其父的所有属性和方法，同时还可以定义自己的属性和方法。
# 字类的方法__init__():创建字类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，字类的方法__init__()需要父类施以援手。
class ElectricCar(Car):  #创建字类时，父类必须包含在当前文件中，且位于字类前面，定义字类时，必须在括号内指定父类的名称Car
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):  #方法__init__()接受创建Car实例所需的信息
        """初始化父类的属性"""
        super().__init__(make,model,year)  #super()是一个特殊的函数，帮助Python将父类和字类关联起来。这行代码让Python调用ElectricCar的父类的
        # 方法__init__()，让ElectricCar实例包含父类的所有属性。父类也称为超类(superclass)，名称super因此而得名。

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
# Python2.7中的继承：函数super()需要两个实参（子类名和对象self）,为帮助Python将父类和字类关联起来，这些实参必不可少，【务必在定义父类时在括号内指定object.】
# class Car(object):
#     def __init__(self,make,model,year):
#         --snip
#
# class ElectriCar(Car):
#     def __init__(self,make,model,year):
#         super(ElectricCar,self).__init__(make,model,year)
# a.给子类定义属性和方法：让一个字类继承另一个类后,可添加区分字类和父类所需的新属性和方法.
class New_ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """电动汽车的独特之类
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery_size=70  #添加了新属性self.battery_size,并设置其初始值,根据New_ElectricCar类创建的所有实例都将包含这个属性,
        # 但所有Car实例都不包含它,

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def fill_gas_tank(self): #重写了父类的方法,
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

my_new_tesla=New_ElectricCar('tesla','model s',2016)
print(my_new_tesla.get_descriptive_name())
my_new_tesla.describe_battery()
# b.重写父类的方法：对于父类的方法,只要它不符合字类模拟的实物的行为,都可对其进行重写.为此,可在字类中定义一个这样的方法,即它与要重写的父类
# 方法同名.这样,Python将不会考虑这个父类方法,而只关注你在字类中定义的相应方法.
my_new_tesla.fill_gas_tank()  #Python将忽略Car类中该方法,转而运行字类中的代码,使用继承时,可让字类保留从父类那里继承而来的精华,并剔除不需要的糟粕.
# c.将实例用作属性:使用代码模拟实物时,你可能会发现自己给类添加的细节越来越多:属性和方法清单以及文件都越来越长.在这种情况下,可能需要将类的一部分作为一个
# 独立的类提出出来.可以将大型类拆分成多个协同工作的小类.
class Battery():   #定义一个新类,它没有继承任何类.
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=70): #形参battery_size为可选的,如果没有给它提供值,电瓶容量将被设置为70
        """初始化电瓶的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery.")

    def update_battery(self):
        if self.battery_size!=85:
            self.battery_size=85
        return self.battery_size

    def get_range(self):
        """打印一条消息,之处电瓶的续航里程
        """
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class Electri_Car(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性,再初始化电动汽车独有的属性
        """
        super().__init__(make,model,year)
        self.battery=Battery()  #添加一个属性,并创建了一个新的实例(Battery),并将该实例存储在属性self.battery中,每当方法__init__()被
        # 调用时,都将执行该操作;因此现在每个Electric_Car实例都包含一个自动创建的Battery实例.

my_tesla=Electri_Car('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  #在实例my_tesla中查找属性battery,并对存储在该属性中的Battery实例调用方法describe_battery().
my_tesla.battery.get_range()
# d.模拟实物:模拟较复杂的物件时,需要解决一些有趣的问题.续航里程是电瓶的属性还是汽车的属性呢?如果我们只需要描述一辆汽车,那么将方法get_range()
# 放在Battery类中也许是合适的但如果要描述一家汽车制造商的整个产品线,也许应该将方法get_range()移到Electri_Car类中.在这种情况下,get_range()
# 依然根据电瓶容量来确定续航里程,但报告的是一款汽车的续航里程.我们也可以这样做:将方法get_range()还留在Battery类中,但向它传递一个参数,如car_model;
# 在这种情况下,方法get_range()将根据电瓶容量和汽车型号报告续航里程.
# 这让你进入了程序员的另一个境界:解决上述问题时,你从较高的逻辑层面(而不是语法层面)考虑;你考虑的不是Py't'hon,而是如何使用代码来表示实物,到达这种
# 境界后,你经常会发现,现实世界的建模方法并没有对错之分.有些方法的效率更高,但要找出效率最高的表示法,需要经过一定的实践.只要代码像你希望的那样运行,
# 就说明你做得很好!即便你发现自己不得不多次尝试使用不同的方法来重写类,也不必气馁;要编写出高效,准确的代码,都得经过这样的过程.
# ***************************************导入类***************************************
# 随着你不断地给类添加功能,文件可能变得很长,即便你妥善地使用了继承亦如此.为遵循Python的总体理念,应让文件尽可能整洁.为在这方面提供帮助,Python允许你
# 将类存储在模块中,然后在主程序中导入所需的模块.
# a.导入单个类:需要在创建的每个模块都编写文档字符串,即在文档开头注释,格式:from car import Car
# 导入类是一种有效的编程方式.如果在这个程序中包含了整个Car类,那该有多长呀!通过将这个类移到一个模块中,并导入该模块,依然可以使用其所有功能,但主程序文件
# 变得整洁而易于阅读了.这还能让你将大部分逻辑存储在独立的文件中;确定类像你希望的那样工作后,你就可以不管这些文件,而专注了主程序的高级逻辑了.
# b.在一个模块中存储多个类:虽然同一个模块中的类之间应存在某种相关性,但可根据需要在一个模块中存储任意数量的类,如类Battery和ElectricCar都可以帮助模拟
# 汽车,因此将它们都加入模块car.py中.
# c.从一个模块中导入多个类:可根据需要在程序文件中导入任意数量的类.如果我们要在同一个程序中创建普通汽车和电动汽车,就需要Car和ElectricCar类都导入;
# 从一个模块中导入多个类时i,用逗号分隔了各个类.导入必要的类后,就可根据需要创建每个类的任意数量的实例:from car import Car,ElectricCar
# d.导入整个模块:还可以导入整个模块,再使用句点表示法访问需要的类.这种导入方法很简单,代码也易于阅读.由于创建实例的代码都包含模块名,因此不会与当前文件
# 使用的任何文件名称发生冲突:import Car,使用语法:module_name.class_name访问需要的类.
# e.导入模块中的所有类:要导入模块中的每个类,可使用语法:from module_name import *
# 不推荐使用这种导入方式,其原因有二.首先,如果只要看一下文件开头的import语句,就清楚地知道程序使用了哪些类,将大有裨益;但这种导入方式没有明确地指出你
# 使用了模块的哪些类.这种导入方式还可能引发名称方面的困惑.如果你不小心导入了一个与程序文件中其他东西同名的类,将引发难以诊断的错误.这里之所以介绍这种
# 导入方式,是因为虽然不推荐使用这种方式,但你可能会在别人编写的代码中见到它.
# 需要从一个模块中导入很多类时,最好导入整个模块,并使用module_name.class_name语法来访问类.这样做时,虽然文件开头并没有列出用到的所有类,但你清楚地知道
# 在程序的那些地方使用了导入的模块;你还避免了导入模块中的每个类可能引发的名称冲突.
# f.在一个模块中导入另一个模块:有时候,需要将类分散到多个模块中,以免模块太大,或在同一个模块中存储不相关的类.将类存储在多个模块中时,你可能会发现一个模块
# 中的类依赖于另一个模块中的类.在这种情况下,可在前面模块中导入必要的类.
# g.自定义工作流程:在组织大型项目的代码方面,Python提供了很多选项.熟悉所有这些选项很重要,这样你才能确定哪种项目组织方式是最佳的,并能理解别人开发的项目.
# 一开始应让代码结构尽可能简单.先尽可能在一个文件中完成所有的工作,确定一切都能正确运行后,再将类移到独立的模块中.如果你喜欢模块和文件的交互模式,可在项目
# 开始时就尝试将类存储到模块中.先找出让你能够编写出可行代码的方式,再尝试让代码更为组织有序.
# ********************Python标准库*************************
# Python标准库是一组模块,安装的Python都包含它.可使用标准库中的任何函数和类,为此只需在程序开头包含一条简单的import语句.
favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'
print("\n模块collections中的OrderedDict类的使用")
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

# 这是一个很不错的类，它兼具了列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。等你开始对关心的现实情形建模时，可能会发现有序字典正好能够
# 满足需求。随着你对标准库的了解越来越深入，将属性大量可帮助你处理常见情形的模块

# *************************类编码风格*******************************
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加下划线。
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模
# 块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
# 可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
# 需要同时导入标准库中的模块和你编写的模块时,先编写导入标准库模块的import语句,再添加一个空行,然后编写导入你自己编写的模块的import语句.在包含
# 多条import语句的程序中,这种做法让人更容易明白程序使用的各个模块都来自何方.