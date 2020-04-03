#encoding=utf-8
# 11-1城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名，这个函数返回一个格式为City，Country的字符串，如Santiago,Chile.
# 将这个函数存储在一个名为city_functions.py的模块中。
# 创建一个名为test_cities.py的程序，对刚编写的函数进行测试（别忘了，你需要导入模块unittest以及要测试的函数）。编写一个名为
# test_city_country(）的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。运行test.cities.py，
# 确认测试test_city_country()通过了。
def city_functions(city,country,population=''):
    if population:
        city_country=city.title()+","+country.title()+"-population "+population
    else:
        city_country=city.title()+","+country.title()
    return city_country
# 11-2人口数量：修改前面的函数，使其包含第三个必不可少的形参population.并返回一个格式为City，Country-population xxx的字符串，如
# Santiage,Chile-population 5000000。运行test_cities.py，确认测试test_city_country()未通过。
# 修改上述函数，将形参population设置为可选的。再次运行test_cities.py，确认测试test_city_country()又通过了。
# 再编写一个名为test_city_country_population()的测试，核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用
# 这个函数。再次运行test_cities.py，确认测试test_city_country_population()通过了。
# def city_country_population(city,country,population):
#     city_country_population=city.title()+","+country.title()+"-population "+population
#     return city_country_population
# 11-3雇员：编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。编写一个名为give_raise()的方法，
# 它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
# 为Employee编写一个测试用例，其中包含两个测试方法；test_give_default_raise()和test_give_custom_raise().使用方法setUp()，以免在
# 每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
class Employee():
    """关于雇员的信息"""
    def __init__(self,name,family_name,annual_salary):
        """初始化名、姓和年薪"""
        self.name=name
        self.family_name=family_name
        self.salary=annual_salary

    def give_raise(self,increasement=5000):
        self.increasement=increasement
        self.salary+=increasement
        return self.salary
# 调用Employee类
# a=Employee('ming','li',0)
# print(a.give_raise())
# print(a.give_raise(30))

