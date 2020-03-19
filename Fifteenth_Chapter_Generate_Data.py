#encoding=utf-8
import matplotlib.pyplot as plt
import pygal

from random import randint
from random import choice
# 数据可视化指的是通过可视化表示来探索数据，它与数据挖掘紧密相关，而数据挖掘指的是使用代码来探索数据集的规律和关联。
# 数据集可以是用一行代码就能表示的小型数据列表，也可以是数以吉字节的数据。
# 漂亮地呈现数据关乎的并非仅仅是漂亮的图片。以引人注目的简洁方式呈现数据，让观看者能够明白其含义，发现数据集中原本未
# 意识到的规律和意义。
# 所幸即便没有超级计算机，也能够可视化复杂的数据。鉴于Python的高效性，使用它在笔记本电脑上就能够快速地探索由数百万个数据点组成的
# 数据集。数据点并非必须是数字，利用本书前半部分介绍的基本知识，也可以对非数字数据进行分析。
# 在基因研究、天气研究、政治经济分析等众多领域，大家都使用Python来完成数据密集型工作。数据科学家使用Python编写了一系列令人印象深刻的
# 可视化和分析工具，其中很多也可供你使用.最流行的工具之一是matplotlib，它是一个数学绘图库，我们将使用它来制作简单的图表，如折线图
# 和散点图。然后，我们将基于随机漫步概念生成一个更有趣的数据集----根据一系列随机决策生成的图表。
# 我们还将使用Pygal包，它专注于生成适合在数字设备上显示的图表。通过使用Pygal，可在用户与图表交互时突出元素以及调整其大小，还可轻松
# 地调整整个图表的尺寸，使其适合在微型智能手表或巨型显示器上显示。我们将使用Pygal以各种方式探索掷骰子的结果。
# 安装matplotlib(可以直接PyCharm或者去网上下在来进行安装)
squares=[1,4,9,16,25] #创建一个列表，存储平方数
# plt.plot(squares)  #将列表传递给函数plot()，根据这些数字绘制出有意义的图形。
# plt.show()  #打开matplotlib查看器，并显示绘制的图形
# 修改标签文字和线条粗细
# plt.plot(squares,linewidth=5) #参数linewidth决定了plot()绘制的线条的粗细。
input_values=[1,2,3,4,5] #plot()输入值
# plt.plot(input_values,squares,linewidth=5)
# #设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)  #函数title()给图表指定标题，而fontsize指定了图表中文字的大小。
# plt.xlabel("Value",fontsize=14)  #函数xlabel()和ylabel()为每条轴设置标题
# plt.ylabel("Square of Value",fontsize=14)
#
# #设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14) #函数tick_params()设置刻度的样式
# ，其中指定的实参将影响x轴和y轴上的刻度（axis='both'），并将刻度标记的字号设置为14（labelsize=14）
# plt.show()
# 校正图形
# 当你向plot()提供一系列数字时，它假设第一个数据点对应的x坐标值为0，但我们的第一个点对应的x值为1.
# 为改变这种默认行为，我们可以给plot()同时提供输入值和输出值：
# 使用plot()时可指定各种实参，还可使用众多函数对图形进行定制。
print("使用scatter()绘制散点图并设置其样式")#有时候，需要绘制散点图设置各个数据点的样式，例如，你可能想以一种颜色显示较小的值，
# 而用另一种颜色显示较大的值。绘制大型数据集时，你还可以对每个点都设置同样的样式，再使用不同的样式选项重新绘制某些点，以突出它们。
# 要绘制单个点，可使用函数scatter(),并向它传递一对x和y坐标，它将在指定位置绘制一个点：
# plt.scatter(2,4,s=200) #实参s设置了绘制图形时使用的点的尺寸
#设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
# #设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()
print("使用scatter()绘制一系列点")#要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]
# plt.scatter(x_values,y_values,s=100)#将两个列表传递给scatter()时，matplotlib依次从每个列表中读取一个值来绘制一个点。
# #设置图表标题并给坐标轴指定标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
# #设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()
print("自动计算数据")
#手工计算列表要包含的值可能效率低下，需要绘制的点很多时尤其如此。可以不必手工计算包含点坐标的列表，用循环来完成这种计算。
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values] #列表解析
# plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)  #自定义颜色
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40)#使用RGB颜色模式自定义颜色
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
#设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Values",fontsize=14)
# plt.ylabel("Square of Values",fontsize=14)
# #设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])#函数axis()要求提供四个值：x和y坐标轴的最小值和最大值
# PS:在这里，我们将x坐标轴的取值范围设置为0~1100，并将y坐标轴的取值范围设置为0~1100000
# plt.show()
# plt.savefig('squares_plot.png',bbox_inches='tight')
print("删除数据点的轮廓")
#matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的数据点不多时效果很好，但绘制很多点时，黑色轮廓
# 可能跟会粘连在一起，要删除数据点的轮廓，可在调用scatter时传递实参edgecolor='none'(默认值为none)
# plt.scatter(x_values,y_values,edgecolors='none',s=40)
print("自定义颜色")#要修改数据点的颜色，可想scatter()传递参数c，并将其设置为要使用的颜色的名称
# plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)
# 还可以使用RGB颜色模式自定义颜色。要制定自定义颜色，可传递参数c，并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示
# 红色、绿色和蓝色分量。
# plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40) #值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
print("使用颜色映射")
#颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律，例如，
# 你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。模块pyplot内置了一组颜色映射。要使用这些颜色映射，需要告诉pyplot该如何
# 设置数据集中每个点的颜色。
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
# 我们将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色。
print("自动保存图表")#要让程序自动将图表保存到文件中，可将对plt.show()的调用替换成plt.savefig()的调用
# plt.savefig('squares_plot.png',bbox_inches='tight')
# 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到本程序运行的目录中；第二个实参指定将图表多余的空白区域裁剪掉。
# 如果要保留图表周围多余的空白区域，可省略这个实参。

# *********************随机漫步*******************
# 在本节中，我们将使用Python来生成随机漫步数据，再使用matplotlib以引人瞩目的方式将这些数据呈现出来。随机漫步是这样行走得到的路径：
# 每次行走都完全是随机的，没有明确的方向，结果是一系列随机决策决定的。你可以这样认为，随机漫步就是蚂蚁在晕头转向的情况下，每次都沿
# 随机的方向前行所经过的路径。在自然界、物理学、生物学、化学和经济领域。例如，漂浮在水滴上的花粉因不断受到水分子的挤压而在水面上移动。
# 水滴中的分子运动是随机的，因此花粉在水面上的运动路径犹如随机漫步。
class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points=num_points
        #所有随机漫步都始于（0，0）
        self.x_values=[0]
        self.y_values=[0]
# 为做出随机决策，我们将所有可能的选择都存储在一个列表中，并在每次做决策时都使用choice()来决定使用哪种选择，
    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步，知道列表达到指定的长度
        while len(self.x_values)<self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_direction=choice([1]) #1表示向右走，-1则表示向左走
            x_distance=choice([0,1,2,3,4,5,6,7,8])  #随机地选择一个0~4之间的整数，告诉Python沿指定的方向走多远
            x_step=x_direction*x_distance  #确定沿x轴移动的距离，如果x_step为正，将向右移动，为负则向左移动

            y_direction=choice([1])
            y_distance=choice([0,1,2,3,4,5,6,7,8])
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
            #计算下一个点的x和y值
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
print("*************绘制随机漫步图************")
#创建一个RandowWalk实例，并将其包含的点都绘制出来
# rw=RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values,rw.y_values,s=15)
# plt.show()
print("****************模拟多次随机漫步****************")
# 每次随机漫步都不同，因此探索可能生成的各种模式很有趣。要在不多次运行程序的情况下使用前面的代码模拟多次随机漫步，
# 一种办法是将这些代码放在一个while循环种，如下
# #只要程序处于活动状态，就不断地模拟随机漫步
# while True:
#     #创建一个RandomWalk实例，并将其包含的点都绘制出来
#     rw=RandomWalk()
#     rw.fill_walk()
#     plt.scatter(rw.x_values,rw.y_values,s=15)
#
#     keep_running=input("Make another walk? (y/n): ")
#     if keep_running=='n':
#         break
# PS:这些代码模拟一次随机漫步，在matplotlib查看器中显示结果，再在不关闭查看器的情况下暂停。如果你关闭查看器，
# 程序将询问你是否要再模拟依次随机漫步。如果你输入y,可模拟多次随机漫步：这些随机漫步都在起点附近进行，大多沿
# 特定方向偏离起点，漫步点分布不均匀等。要结束程序，则输入n。
print("***************设置随机漫步图的样式***********")
# 在本节中，我们将定制图表，以突出每次漫步的重要特征，并让分散注意力的元素不那么显眼，为此，我们确定要突出的要素，如漫步的起点、
# 终点和经过的路径。接下来确定要使其不那么显眼的元素，如刻度标记和标签。最终的结果是简单的可视化表示，清楚地指出了每次漫步经过的路径。
# while True:
#     #创建一个RandomWalk实例，并将其包含的点都绘制出来
#     rw=RandomWalk()
#     rw.fill_walk()
#
#     #设置绘图窗口的尺寸,函数figure()用于指定图表的宽度、高度、分辨率和背景色。所以需要给形参figsize指定一个元组，
#     # 向matplotlib指出绘图窗口的尺寸，单位为英寸。Python假定屏幕分辨率为80像素/英寸，如果上述代码指定的图表尺寸不合适，
#     # 可根据需要调整其中的数字。如果你知道自己的系统的分辨率，可使用形参dpi向figure()传递该分辨率，以有效地利用可用的屏幕空间
#     plt.figure(dpi=128,figsize=(10,6))
#
#     point_numbers=list(range(rw.num_points))
#     plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)#给点着色
#
#     #突出起点和终点
#     plt.scatter(0,0,c='green',edgecolors='none',s=100)
#     plt.scatter(rw.y_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
#
#     #隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False) #为修改坐标轴，使用了函数plt.axes()来将每条坐标轴的可见性都设置为False.
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running=input("Make another walk? (y/n): ")
#     if keep_running=='n':
#         break
print("**********************使用Pygal模拟掷骰子***********************")
# 在本节中我们将使用Python可视化包Pygal来生成可缩放的矢量图形文件。对于需要在尺寸不同的屏幕上显示图表，很有用，因为它们将自动缩放，
# 以适合观看者的屏幕。如果你打算以在线方式使用图表，请考虑使用Pygal来生成它们，这样它们在任何设备上显示时都会很美观。
# 在这个项目中，我们将对掷骰子的结果进行分析。掷6面的常规骰子时，可能出现的结果为~6点，且出现每种结果的可能性相同。然后如果同时掷两个骰子，
# 某些点数出现的可能性将比其他点数大。为确定哪些点数出现的可能性最大，我们将生成一个表示掷骰子结果的数据集，并根据结果绘制一个图形。
# 在数学领域，常常利用掷骰子来解释各种数据分析，但它在赌场和其他博弈场景中也得到了实际应用。
class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides=num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides) #函数randint()返回一个1和面数之间的随机数。这个函数可能返回起始值1，终止值num_sides或这两个值之间的任何整数。

#创建一个D6，一个D10
die_1=Die()
die_2=Die(10)

#掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
#分析结果
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()
hist.title="Results of rolling two D6 50000 times."
# hist.x_labels=['1','2','3','4','5','6']
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Result"
hist._y_title="Frequency of Result"

hist.add("D6+D10",frequencies)
hist.render_to_file('die_visual.svg')
# print(results)
# print(frequencies)