import unittest
from Eleventh_Chapter_Testcode import get_formatte_name
from Eleventh_Chapter_Testcode_Work import city_functions
from Eleventh_Chapter_Testcode import AnonymousSurvey
from Eleventh_Chapter_Testcode_Work import Employee
# Python标准库中的模块unittest提供了代码测试工具.创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试
# 就很简单了。要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个基础unittest.TestCase的类，并编写一系列方法对
# 函数行为的不同方面进行测试。
class NamesTestCase(unittest.TestCase): #可随便给这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。这个类必须
    # 继承unittest.TestCase类，这样Python才知道如何运行你编写的测试。
    """测试Eleventh_Chapter_Testcode"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的性命吗？"""
        formatted_name=get_formatte_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #使用了unittest类最有用的功能之一：一个断言方法。

    def test_first_last_middle_name(self): #方法名必须以test_开头
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name=get_formatte_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
        # 断言方法用来核实得到的结果是否与期望的结果一致。

    def test_city_country(self):
        """能够正确地处理Santiago,Chile这样的字符串"""
        city_country_name=city_functions('santiago','chile')
        self.assertEqual(city_country_name,'Santiago,Chile')

    def test_city_country_population(self):
        """能够处理Santiago,Chile-population 5000000"""
        city_country_population=city_functions('santiago','chile','5000000')
        self.assertEqual(city_country_population,'Santiago,Chile-population 5000000')

class TestAnonymousSurver(unittest.TestCase):
    """针对AnonymousSurver类的测试"""
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善地存储"""
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        responses=['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

class TestAnonymousSurey(unittest.TestCase):
    """针对AnonymousSurey类的测试"""
    def setUp(self):# 方法setUp()做了两件事情：创建一个调查对象；创建一个答案列表。存储这两样东西的变量名包含前缀self（即存储在属性中），
        # 因此可在这个类的任何地方使用。这让两个测试方法都更简单，因为它们都不用创建调查对象和答案。
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question="What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])  #核实self.responses中的第一个答案，被妥善地存储
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:#核实self.responses中的全部答案都被妥善地存储。
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
# setUp()方法使用总结：测试自己编写的类时，方法setUp()让测试方法编写起来更容易：可在setUp()方法中创建一系列实例并设置它们的属性，
# 再在测试方法中直接使用这些实例。相比于在每个测试方法中都创建实例并设置属性，这要容易得多。
class TestEmployee(unittest.TestCase):
    """测试Employee类"""
    def setUp(self) :
        """创建雇员实例"""
        self.my_employee=Employee('hua','xiao',0)

    def test_give_deafult_rasie(self):
        """测试年薪默认增加值"""
        deafult_salary=self.my_employee.give_raise()
        self.assertEqual(5000,deafult_salary)

    def test_give_custom_rasie(self):
        custom_rasie=self.my_employee.give_raise(20)
        self.assertEqual(20,custom_rasie)

#PS:运行该文件的时候，所有以test_开头的方法都将自动运行。在TestCase类中使用很长的方法名是可以的；这些方法的名称必须是描述性的，
# 这才能让你明白测试未通过时的输出；这些方法由Python自动调用，你根本不哦那个编写调用它们的代码。
if __name__=="__main__":
    unittest.main()


# 如果测试未通过时怎么办呢？如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错。因此，
# 测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。

# 运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F。
# 这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。如果测试用例包含很多单元测试，需要运行很长时间，
# 就可通过观察这些结果来获悉有多少个测试通过了。