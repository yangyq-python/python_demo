#encoding=utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
from operator import itemgetter
# 在本章中将学习如何编写一个独立的程序，并对其获取的数据进行可视化。这个程序将使用Web应用编程接口（API）自动请求网站的特定信息而不
# 是整个网页，再对这些信息进行可视化。由于这样编写的程序始终使用最新的数据来生成可视化，因此即便数据瞬息万变，它呈现的信息也是最新的。
# 使用Web API:Web API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。请求的数据将以易于处理的格式
# （如JSON或CSV）返回。依赖于外部数据源的大多数应用程序都依赖于API调用，如集成社交媒体网站的应用程序。


#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)  #响应对象包含一个名为status_code的属性，它让我们知道请求是否成功了（状态码200表示请求成功）
#将响应存储在一个变量中
response_dict=r.json()#使用方法json()将这些信息转换为一个Python字典，
print("Total repoositories:",response_dict['total_count'])
repo_dicts=response_dict['items']#探索有关仓库的信息
# print("Repositories returned:",len(repo_dicts))
# #概述最受欢迎的仓库
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print("\nName：",repo_dict['name'])
#     print("Owner:",repo_dict['owner']['login'])
#     print("Stars:",repo_dict['stargazers_count'])
#     print('Repository:',repo_dict['html_url'])
#     print('Description:',repo_dict['description'])
#
# #研究第一个仓库
# repo_dict=repo_dicts[0]
# print("\nSelected information about first repository:")
# print('Name:',repo_dict['name'])
# print('Owner:',repo_dict['owner']['login'])
# print('Stars:',repo_dict['stargazers_count'])
#
# print("\nKey:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
#
# #处理结果
# print(response_dict.keys())

print("使用Pygal可视化仓库")
# names,stars=[],[]
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    # 根据数据绘图
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink':repo_dict['html_url'], #在图表中添加可单击的链接，添加一个键为‘xlink’的键-值对
    }
    plot_dicts.append(plot_dict)

#可视化
my_style=LS('#333366',base_style=LCS)#使用LightenStyle类（别名LS）定义了一种样式，并将其基色设置为深蓝色，还传递了实参base_style,
# 以使用LightColorizedStyle类（别名LCS），
#改进Pygal图表
my_config=pygal.Config()#创建一个Pygal类Config的实例，通过修改my_config的属性，可定制图表的外观。
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)#创建Bar实例时，我们将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置。
# 我们可以通过my_config做任意数量的样式和配置修改
# chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)#然后，我们使用Bar()创建了一个简单的条形图，并向它传递了my_style，我们还传递了另外两个
# 样式实参;让标签绕x轴旋转45度（x_label_rotation=45），并隐藏了图例（show_legend=False）
chart._title='Most-Starred Python Projects on GitHub'  #给图表指定了标题
chart.x_labels=names #设置标题属性x_labels为列表names
chart._title='Python Projects'
# chart.x_labels=['httpie','django','flask']
# plot_dict=[
#     {'value':16101,'label':'Description of httpie'},
#     {'value':15028,'label':'Description of django'},
#     {'value':14798,'label':'Description of flask'}
#     ]


# chart.add('',plot_dict)
chart.add('',plot_dicts)
# chart.render_to_file('new_python_repos.svg')
# chart.add('',stars)  #由于我们不需要给这个数据系列添加标签，因此在添加数据时，将标签设置成了空字符串
# chart.render_to_file('new_python_repos.svg')


print("Hacker News API")
#执行API调用并存储响应
api_url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(api_url)
print("Status code:",r.status_code)

#处理有关每篇文章的信息
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个API调用
    api_url=('https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json')
    submission_r=requests.get(api_url)
    print(submission_r.status_code)
    response_dict=submission_r.json()

    submission_dict={
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(submission_id),
        'comments':response_dict.get('descendants',0)
    }
    submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

    for submission_dict in submission_dicts:
        print("\nTitle:",submission_dict['title'])
        print("Discussion link",submission_dict['link'])
        print("Comments:",submission_dict['comments'])