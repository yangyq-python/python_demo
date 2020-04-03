#encoding=utf-8
import csv
import requests
import json
import pygal
import math
from itertools import groupby
from prettytable import PrettyTable
from datetime import datetime
from matplotlib import pyplot as plt
# from __future__ import (absolute_import,division,print_function,unicode_literals)
import json
from urllib.request import urlopen
# 在本章中，你将从网上下载数据，并对这些数据进行可视化。我们将访问并可视化以两种常见格式存储的数据：CSV和JSON。
# 我们将使用Python模块csv来处理以CSV(逗号分隔的值)格式存储的数据，使用模块json来访问以JSON格式存储的交易收盘价
# 数据，并使用Pygal绘制图形以探索价格变化的周期性。
# filename='sitka_weather_07-2014.csv'
# filename='sitka_weather_2014.csv'
filename= '../basic/death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader) #返回文件头

    dates,highs,lows=[],[],[]  #用于存储从文件中提取的日期和最高气温

    # print(header_row)
    # for index,colum_header in enumerate(header_row): #对列表调用了enumerate()来获取每个元素的索引及其值
    #     print(index,colum_header)
    #从文件中获取最高气温、最低气温和日期
    for row in reader: #遍历文件中余下的各行，阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。
        # 由于我们已经读取了文件头行，这个循环将从第二行开始---从这行开始包含的是实际数据。每次执行该循环时，我们都将索引从1处
        # （第2列）的数据附加到highs末尾
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])  # 将字符串转换为数字，再将其附加到列表末尾，转换为数字方便matplotlib能够读取它们
            low = int(row[3])  # 获取最低气温
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    #根据数据绘制图形
    fig=plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)#实参alpha指定颜色的透明度。Alpha值为0表示完全透明，1（默认设置）表示完全不透明。
    # 通过将alpha设置为0.5，可让红色和蓝色折线的颜色看起来更浅。
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)  #我们向fill_between()传递了一个x值系列：列表dates,还传递了
    # 两个y值系列：highs和lows.实参facecolor指定了填充区域的颜色，


    #设置图形的格式
    plt.title("Daily high and low temperatures-2014\nDeath Valley,CA",fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()  #绘制斜的日期标签，以免它们重叠
    plt.ylabel("Temperatur (F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    # plt.show()
    # print(highs)

print("********模块datetime**********")
# 读取数据时，获得的是一个字符串，因为我1们需要想办法将字符串‘2014-7-1转换为一个表示相应日期的对象。为创建表示2014年7月1日的对象，
# 可使用模块datetime中的方法strptime().
first_date=datetime.strptime('2014-7-1','%Y-%m-%d')
# print(first_date)
# 我们首先导入了模块datetime中的datetime类，然后调用方法strptime()，并将包含所需日期的字符串作为第一个实参。第二个实参告诉Python
# 如何设置日期的格式。在这个示例中，'%Y'让Python将字符串第一个连字符前面的部分视为四位的年份；以此类推，方法strptime()可接受各种
# 实参,模块datetime中设置日期和时间格式的实参
table=PrettyTable(['实参','含义'])
a={"%A":"星期的名称，如Monday","%B":"月份名，如January","%m":"用数字表示的月份（）01~12","%d":"用数字表示月份中的一天（01~12）",
   "%Y":"四位的年份，如2015","%y":"两位的年份，如15","%H":"24小时制的小时数（00~23）","%I":"12小时制的小时数（01~12）",
   "%p":"am或pm","%M":"分钟数（00~59）","%S":"秒数（00~61）"}
for key,value in a.items():
    table.add_row([key,value])
# table.add_row(["%A","星期的名称，如Monday"])
# table.add_row(["%B","月份名，如January"])
# table.add_row(["%m","用数字表示的月份（01~12）"])
# print(table)

print("制作交易收盘价走势图：JSON格式")
json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response=urlopen(json_url)
req=response.read()  #读取文件
#将数据写入文件
# with open('btc_close_2017_urllib.json','wb') as f:
#     f.write(req)
# file_urllib=json.loads(req)
# print(file_urllib)
# PS:函数urlopen的代码稍微复杂一些，第三方模块requests封装了许多常用的方法，让数据下载和读取方式变得非常简单：
# req=requests.get(json_url) #请求
# with open('requests_btc_close_2017_urllib.json','w') as f:
#     f.write(req.text)  #req.txt属性可以直接读取文件数据，返回格式是字符串，可以像之前一样保存为文件
# file_requests=req.json()#直接用req.json()就可以将生成的文件的数据转换成Python列表file_requests,与之前的file_urllib内容相同。
#
# print(file_urllib==file_requests)
print("提取相关的数据")
#将数据加载到一个列表中
file_name= '../basic/btc_close_2017_urllib.json'
with open(file_name) as f:
    btc_data=json.load(f)

#绘制折线图之前，需要获取x轴与y轴数据，因此需要创建几个列表来存储数据。
dates,months,weeks,weekdays,close,=[],[],[],[],[]
#打印每一天的信息：
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))#Python不能直接将包含小数点的字符串转换为整数。为了消除这种错误，
    # 需要先将字符串转换为浮点数（float），再将浮点数转换为整数（int）
    # print("{} is month {} week,{},{},the close price is {} RMB".format(date,month,week,weekday,close))
#由于数据点比较多，x轴要i西安市346个日期，在有限的屏幕上显得十分拥挤。因此我们需要利用pygal的配置参数，对图形进行适当的调整
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False) #x_label_rotation=20让x轴上的日期标签顺时针旋转20°，
# 而show_minor_x_labels=False则告诉图形不用显示所有的x轴标签。
# line_chart.title='收盘价（￥）'
line_chart._title='收盘价对数变换（￥）'
line_chart.x_labels=dates
N=20 #x轴坐标每隔20天显示一次
line_chart.x_labels_major=dates[::N]
close_log=[math.log10(_) for _ in close]
# line_chart.add('收盘价',close)
line_chart.add('log收盘价',close_log)
# line_chart.render_to_file('收盘价折线图【￥】.svg')
# line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')
print("时间序列特征初探")
# PS：进行时间序列分析总是期望发现趋势（trend）、周期性（seasonality）、和噪声（noise），从而能够描述事实、预测未来、做出决策。
# 从收盘价的折线图可以看出，2017年的总体趋势是非线性的，而且增长幅度不断增大，似乎呈指数分布。但是我们还发现，在每个季度末似乎有一
# 些相似的波动。尽管这些波动被增长的趋势掩盖了，不过其中也许有周期性，为了验证周期性的加上，需要首先将非线性的趋势消除。
# 对数变换（log transformation）是常用的处理方法之一。让我们用Python标准库的数学模块math来解决这个问题。math里有许多常用的数学函数，
# 这里用以10为底的对数函数math.log10计算收盘价,日期仍然保持不变。这种方式被称为半对数（semi-logarithmic）变换，
print("收盘价均值")
# ps：下面再利用btc_close_2017.json文件中的数据，绘制2017年前11个月的日均值、前49周（2014-01-02~2017-12-10）的日均值，以及
# 每周中各天（Monday~Sunday）的日均值。虽然这些日均值的数值不同，但都是一段时间的均值，计算方法是一样的。因此，
# 可以将之前的绘图代码封装成函数，以便重复使用
def draw_line(x_data,y_data,title,y_legend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list=[v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique,y_mean=[*zip(*xy_map)]
    line_chart=pygal.Line()
    line_chart._title=title
    line_chart.x_labels=x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month=dates.index('2017-12-01')
# line_chart_month=draw_line(months[:idx_month],close[:idx_month],'收盘价月日均值（￥）','月日均值')
# line_chart_month

idx_week=dates.index('2017-12-11')
# line_chart_week=draw_line(weeks[1:idx_week],close[1:idx_week],'收盘价周日均值（￥）','周日均值')
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int=[wd.index(w)+1 for w in  weekdays[1:idx_week]]
line_chart_weekday=draw_line(weekdays_int,close[1:idx_week],'收盘价星期均值（￥）','星期均值')
line_chart_weekday.x_labels=['周一','周二','周三','周四','周五','周六','周日']
# line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')
print("收盘价数据仪表盘")
with open('收盘价Dashboard.html', 'w', encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head></body>\n')
    for svg in [
        '收盘价折线图（￥）.svg','收盘价对数变换折线图（￥）.svg','收盘价月日均值（￥）.svg',
        '收盘价周日均值（￥）.svg','收盘价星期均值（￥）.svg'
    ]:
        html_file.write(' <object tpye="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')