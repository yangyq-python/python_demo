import pygal

from random import randint
from random import  choice


# 15-1立方：数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。
# x_values=list(range(1,5000))
# y_values=[x**3 for x in x_values]
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40) #颜色映射
# # plt.plot(x_values,y_values,linewidth=5)
# plt.title("Cube Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Cube of Value",fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=14)
# # plt.axis([0,1100,0,1100000])
# plt.show()
# 15-2彩色立方：给你前面绘制的立方图指定颜色映射。
# 见上述代码中的颜色映射
# 15-3分子运动：修改rw.visual.py，将其中的plt.scatter()替换成plt.plot()。为模拟花粉在水滴表面的运动路径，向plt.plot()传递rw.x_values
# 和rw.y_values，并指定实参值linewidth。使用5000个点而不是50000个点。
# rw=RandomWalk()
# rw.fill_walk()
# plt.plot(rw.x_values,rw.y_values,linewidth=20)
# plt.show()
# 15-4改进的随机漫步：在类RandomWalk中，x_step和y_step是根据相同的条件生成的：从列表[1,-1]中随机地选择方向，并从列表[0，1，2，3，4]
# 中随机地选择距离。请修改这些列表中的值，看看对随机漫步路径有何影响，尝试使用更长的距离选择列表，如0~8；或者将-1从x或y方向列表中删除。
# 15-5重构：方法fill_walk()很长。请新建一个名为get_step()的方法，用于确定每次漫步的距离和方向，并计算这次漫步将如何移动。然后，在
# fill_walk()中调用get_step()两次：
# x_step=self.get_step()
# y_step=self.get_step()
# 通过这样的重构，可缩小fill_walk()的规模，让这个方法阅读和理解起来更容易。
class NewRandomWalk():
    """一个生成随机漫步数据的表"""
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points=num_points
        #所有随机漫步都始于（0，0）
        self.x_values=[0]
        self.y_values=[0]

    def get_step(self):
        """用于确定每次漫步的距离和方向，并计算这次漫步将如何移动"""
        direction=choice([1,-1])
        distance=choice([0,1,2,3,4])
        step=direction*distance
        return step
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values)<self.num_points:
          #决定前进方向以及沿这个方向前进的距离
            x_step=self.get_step()
            y_step=self.get_step()
          #拒绝原地踏步
            if x_step==0 and y_step==0:
              continue
              #计算下一个点的x和y值
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

# rw1=NewRandomWalk()
# rw1.fill_walk()
# plt.plot(rw1.x_values,rw1.y_values,linewidth=20)
# plt.show()
# 15-6自动生成标签：请修改die.py和dice_visual.py，将用来设置hist.x_labels值的列表替换为一个自动生成这种列表的循环。
# 如果你熟悉列表解析，可尝试将die_visual.py和dice_visual.py中的其他for循环也替换为列表解析。
class NewDie():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides=num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)
#创建两个D6骰子
die01=NewDie()
die02=NewDie()
die03=NewDie()

results=[] #掷骰子多次，并将结果存储到一个列表中
for roll_num in range(1000):
    result=die01.roll()+die02.roll()+die03.roll()
    results.append(result)
#分析结果
frequencies=[]
max_result=die01.num_sides+die02.num_sides+die03.num_sides
for value in range(3,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#可视化结果
hist=pygal.Bar()
hist.title="Results of rolling three D6 dice 1000 times."
hist.x_labels=[str(x+1) for x in range(2,18)]
hist._x_title="Result"
hist._y_title="Frequency of Result"
hist.add("D6+D6+D6",frequencies)
hist.render_to_file('work_three_dice_visual.svg')
# 15-7两个D8骰子：请模拟同时掷两个8面骰子1000次的结果。逐渐增加掷骰子的次数，知道系统不堪重负为止。
# 15-8同时掷三个骰子：如果你同时掷三个D6骰子，可能得到的最小点数是3，而最大点数为18.请通过可视化展示同时掷三个D6骰子的结果。代码同上
# 15-9将点数相乘：同时掷两个骰子时，通常将它们的点数相加。请通过可视化展示将两个骰子的点数相乘的结果。
#创建两个D6的骰子
cheng_die_01=NewDie()
cheng_die_02=NewDie()

cheng_results=[] #掷骰子多次，将结果存储到一个列表中
for cheng_roll_num in range(1000):
    cheng_result=cheng_die_01.roll()*cheng_die_02.roll()
    cheng_results.append(cheng_result)

cheng_frequencies=[] #分析结果
cheng_max_result=cheng_die_01.num_sides*cheng_die_02.num_sides
for cheng_value in range(1,cheng_max_result+1):
    cheng_frequency=cheng_results.count(cheng_value)
    cheng_frequencies.append(cheng_frequency)
#可视化结果
cheng_hist=pygal.Bar()
z=[]#掷两个D6骰子面数相乘可能出现数字集合
# for x in range(1,7):
#     for y in range(1,7):
#         z.append(x*y)
cheng_hist.x_labels=[str(x+1) for x in range(0,cheng_max_result)]
# cheng_hist.x_labels=z

cheng_hist._x_title="Result"
cheng_hist._y_title="Frequency of Result"

cheng_hist.add("D6*D6",cheng_frequencies)
cheng_hist.render_to_file("work_cheng_dice_visual.svg")
# 15-10练习使用本章介绍的两个库：尝试使用matplotlib通过可视化来模拟掷骰子的情况，并尝试使用Pygal通过可视化来模拟随机漫步的情况。