import Ninth_Chapter_Class as nc
from random import randint

# 9-1餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。创建一个名为describe_restaurant()
# 的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。根据这个类创建一个名为restaurant
# 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        """餐馆的名称和经营类型"""
        self.restaurant_name=restaurant_name
        self.restaurant_tpye=restaurant_type
        self.number_served=0

    def describe_restaurant(self):
        """餐馆的描述"""
        print(self.restaurant_name.title()+"，欢迎您光临！")
        print("我们是一家特色鲜明的"+self.restaurant_tpye)

    def open_restaurant(self):
        """该餐馆正在营业"""
        print(self.restaurant_name.title()+"餐馆正在营业中。")

    def set_number_served(self,number):
        """设置就餐人数"""
        self.number_served=number

    def increment_number_served(self,increment):
        """设置递增人数"""
        self.number_served+=increment
        return self.number_served

    # def read_number_served(self):

restaurant=Restaurant('杨氏小面','面馆')
print("该餐馆名字是："+restaurant.restaurant_name+",经营的类型是："+restaurant.restaurant_tpye)
restaurant.describe_restaurant()
restaurant.open_restaurant()
# 9-2三家餐馆：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。
liming_restaurant=Restaurant('李明麻辣烫','麻辣烫')
lili_restaurant=Restaurant('丽丽饺子','饺子馆')
huahua_restaurant=Restaurant('花花—-水果批发','水果批发')
print("\n")
liming_restaurant.describe_restaurant()
print("\n")
huahua_restaurant.describe_restaurant()
print("\n")
lili_restaurant.describe_restaurant()
# 9-3用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。在类User中定义一个名为
# describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self,first_name,last_name,gender="",age=""):
        """用户属性定义"""
        self.firstname=first_name
        self.lastname=last_name
        self.gender=gender
        self.age=age
        self.login_attempts=0

    def describe_user(self):
        """打印用户信息摘要"""
        print("姓名："+self.firstname+self.lastname+",年龄："+str(self.age)+",性别："+self.gender)

    def greet_user(self):
        """个性化问候"""
        print("Hello,"+self.firstname.title()+self.lastname)

    def increment_login_attempts(self):
        """登录值增加1"""
        self.login_attempts+=1
        # return self.login_attempts

    def reset_login_attempts(self):
        """重置登录次数为0"""
        self.login_attempts=0
        return self.login_attempts

user01=User('朱','花','女',36)
user02=User('明','成','男',28)
user01.describe_user()
user01.greet_user()
print("\n")
user02.describe_user()
user02.greet_user()
# 9-4就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0，根据这个类创建一个名为restaurant的
# 实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
restaurant=Restaurant('本帮菜','炒菜')
print("\n一共有："+str(restaurant.number_served)+"人，在"+restaurant.restaurant_name+"餐馆用餐。")
restaurant.number_served=6
print("\n一共有："+str(restaurant.number_served)+"人，在"+restaurant.restaurant_name+"餐馆用餐。")
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
restaurant.set_number_served(9)
print("\n一共有："+str(restaurant.number_served)+"人，在"+restaurant.restaurant_name+"餐馆用餐。")
# 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
restaurant.increment_number_served(7)
print("\n预计在"+restaurant.restaurant_name+"餐馆用餐人数是："+str(restaurant.number_served))
# 9-5尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，它将属性
# login_attempts的值加1.再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0.
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attemps的值，确认它被正确地递增；然后，调用方法reset_login_attempts(),
# 并再次打印属性login_attempts的值，确认它被重置为0
user=User('朱','珠珠','女',33)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print("登录次数:"+str(user.login_attempts))
user.reset_login_attempts()
print("重置登录次数为："+str(user.reset_login_attempts()))
# 9-6冰淇淋小店:冰淇淋小店是一种特殊的餐馆.编写一个名为IceCreamStand的类,让它继承你为完成练习9-1或练习9-4而编写的Restaurant类.这两个版本的
# Restaurant类都可以,挑选你更喜欢的那个即可.添加一个名为flavors的属性,用于存储一个有各种口味的冰淇淋组成的列表.编写一个显示这些冰淇淋的方法.
# 创建一个IceCreamStand实例,并调用这个方法.
class IceCreamStand(Restaurant):
    """冰淇淋的独特处"""
    def __init__(self,restaurant_name,restaurant_type):
        """初始化父类的属性,再初始化冰淇淋特有的属性"""
        super().__init__(restaurant_name,restaurant_type)
        self.flavors=['牛奶','原味','巧克力']

    def read_icecreamstand(self):
        """显示冰淇淋的方法"""
        for flavor in self.flavors:
            print("This icecreamstand's flvaor is "+flavor)
icecreamstand=IceCreamStand('梦之幻','冰淇淋')
print(icecreamstand.read_icecreamstand())
# icecreamstand.flavors=['牛奶','原味','巧克力']
# print(icecreamstand.restaurant_name+"是一家"+icecreamstand.restaurant_tpye+"店,口味主要有:"+str(icecreamstand.read_icecreamstand()))

# 9-7管理员:管理元是一种特殊的用户.编写一个名为Admin的类,让它继承你为完成练习9-3或练习9-5而编写的User类.添加一个名为privileges的属性,用于存储
# 一个由字符串(如"can add post"/"can delete post"/"can ban user"等)组成的列表.编写一个名为show_privileges()的方法,它显示管理员的权限.创建
# 一个Admin实例,并调用这个方法.
class Admin(User):
    def __init__(self,first_name,last_name):
        """初始化父类,在初始化字类的属性"""
        super().__init__(first_name,last_name)
        self.privileges=["can add post","can delete post","can ban user"]
    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("This admin "+privilege)
a=Admin('东南','西北')
a.describe_user()
a.show_privileges()
# 9-8权限:编写一个名Privileges的类,它只有一个属性-----privileges,其中存储了练习9-7所说的字符串列表.将方法show_privileges()移到这个类种.在
# Admin类种,将一个Privileges实例用作其属性.创建一个Admin实例,并使用方法show_privileges()来显示权限.
class Privileges():
    """展示权限"""
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("This admin "+privilege)
class New_Admin(User):
    def __init__(self,first_name,last_name):
        """初始化父类,在初始化字类的属性"""
        super().__init__(first_name,last_name)
        self.new_priviages=Privileges()
print("把权限类单独提出出来,在New_Admin类中,把实例Privelieges用作属性.")
new_admin=New_Admin('新东南','新西北')
new_admin.new_priviages.show_privileges()
# 9-9电瓶升级:在本节最后一个electric_car.py版本种,给Battery类添加一个名为upgrade_battery()的方法.这个方法检查电瓶容量,如果它不是85,就将它设
# 置为85.创建一辆电瓶容量为默认值的电动 汽车,调用方法get_range(),然后对电瓶进行升级,并再次调用get_range().你会看到这辆汽车的续航里程增加了.
new_car=nc.Electri_Car('new_tesla','model s',2020)
new_car.battery.get_range()
new_car.battery.update_battery()
new_car.battery.get_range()
# 9-13使用OrderedDict:在练习6-4中，你使用了一个标准字典来表示词汇表。请使用OrderedDict类来重写这个程序，并确认输出的顺序与你在字典中添加键-值对的顺序一致。
# 9-14骰子：模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
print(randint(1,6))
# 请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6.编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
# 创建一个6面的筛子，再掷10次。创建一个10面的骰子和一个20面的骰子，并将他们都掷10次。
class Die():
    """初始化属性"""
    def __init__(self):
        self.sides=10

    def roll_die(self):
        """打印位于1和骰子面数之间的随机数"""
        return randint(1,self.sides)
my_die=Die()
my_die.sides=20
a=[]
n=1
for n in range(10):
    if n<=10:
        a.append(my_die.roll_die())
        print("n的值："+str(n))
    else:
        print("掷骰子次数已用完")
print(a)

