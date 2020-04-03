#coding=utf-8
from prettytable import PrettyTable
# 编写函数和类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。在本章中，将学习如何使用Python模块unittest
# 中的工具来测试代码。将学习编写测试用例，核实一系列输入都将得到预期的输出。
print("**************测试函数*************")
def get_formatte_name(first,last,middle=''):
    """生成整洁的姓名"""
    if middle:  #如果向这个函数传递了中间名，则执行如下
      full_name=first+' '+middle+" "+last
    else:
        full_name=first+" "+last
    return full_name.title()
# print("Enter 'q' at any time to quit.")
# while True:
#     first=input("\nPlease give me a first name: ")
#     if first=='q':
#         break
#     last=input("Please give me a last name: ")
#     if last=='q':
#         break
#     formatted_name=get_formatte_name(first,last)
#     print("\tNeatly formatted name: "+formatted_name+".")
# 单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求，良好的测试用例考
# 虑到了函数可能跟收到的各种输入，包含针对所有这些情形的测试。全覆盖式侧式用例包含一整套单元测试，涵盖了各种可能的函数的使用方式。
# 对于大型项目，要实现全覆盖式可能很难，通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
#在本章前半部分，编写了针对单个函数的测试，下面来编写针对类的测试。很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。
# 如果针对类的测试通过了，你就能够确信对类所做的改进没有意外地破坏其原有的行为。
print("各种断言方法")
# Python在unittest.TestCase类中提供了很多断言方法。前面说过，断言方法检查你认为应该满足的条件是否确实满足。如果该条件确实满足，你
# 对程序行为的假设就得到了确认，你就可以确信其中没有错误。如果你认为应该满足的条件实际上并不满足，Python将引发异常。
# 下表描述了6个常用的断言方法。使用这些方法可核实返回的值等于或不等于预期的值、返回的值为True或False、返回的值在列表中或不在列表中。
# 你只能继承unittest.TestCase的类中使用这些方法，下面来看看如何在测试类时使用其中的一个。
print("************unittest Module中的断言方法************")
table=PrettyTable(["方法","用途"])
table.add_row(["assertEqual(a,b)","核实a==b"])
table.add_row(["assertNotEqual(a,b)","核实a!=b"])
table.add_row(["assertTrue(x)","核实x为True"])
table.add_row(["assertFalse(x)","核实x为False"])
table.add_row(["assertIn(item,list)","核实item在list中"])
table.add_row(["assertNotIn(item,list)","核实item不在list中"])
print(table)

# 一个要测试的类：类的测试与函数的测试相似--你所做的大部分工作都是测试类中方法的行为，但存在一些不同之处，
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question=question
        self.responses=[]  #创建空的列表，用于存储答案。

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.responses:
            print("-"+response)

# question="What language did you first learn to speak?" #定义一个问题，并创建一个表示调查的AnonymousSurvey对象
# my_survey=AnonymousSurvey(question)
# #显示问题并存储答案
# my_survey.show_question()
# print("Enter 'q' an any time to quit.\n")
# while True:
#     response=input("Language:")
#     if response=='q':
#         break
#     my_survey.store_response(response)
# #显示调查结果
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()
# 方法setUp()：让我们只需创建这些对象一次，并在每个测试方法中使用它们。如果你在TestCase类中包含了方法setUp(),Python将先运行它，
# 再运行各个以test_打头的方法。这样，在你编写的每个测试方法中都可使用在方法setUp()中创建对象了。
