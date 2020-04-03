# 6-1人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name、last_name，age和city。将
# 存储在该字典中的每项信息都打印出来。
friends={'first_name':'李','last_name':'明','age':30,'city':'shanghai'}
print("用字典名加键的方式打印字典的键-值对")
print('first_name: '+friends['first_name'])
print("用for循环打印字典的键-值对")
for key,value in friends.items():
    print(key+':'+str(value))
# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，
# 并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是否真实。
numbers={'lily':5,'joe':6,'ming':7,'ken':8,'pie':9}
for key,value in numbers.items():
    print(key+" loves number is: "+str(value))
# 6-3词汇表：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
#a.想出你在前面学会的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中
#b.以整洁的方式打印每个词汇以及含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；也可以在一行打印词汇，再使用
# 换行符（\n）插入一个空行，然后在下一行以缩进的方式打印词汇的含义。
#可以用for循环同上面两个例子，此处不再重复。
# 6-4 词汇表2：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
glossary={"list":"列表",'dict':"字典",'set':'集合','sotred':'排序','pop':'删除'}
for key,value in glossary.items():
    print(key+":"+value)
# 6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键-值对可能是'nile':'egypt'。
rivers={'yangtze river':'china','nile':'egypt','yalu river':'korea'}
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”
for name in rivers:
    print("The "+name.title()+" runs through "+rivers[name].title())
# 使用循环将该字典中每条河流的名字都打印出来。
for name in rivers.keys():
    print(name)
# 使用循环将该字典包含的每个国家的名字都打印出来。
for country in rivers.values():
    print(country)
# 6-6调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
print("列表和字典嵌套使用")
favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
users=['jen','edwarde','phil']
for user in users:
    if user in favorite_languages.keys():
        print(user+" Thank you!")
    else:
        print(user+" invite to participate in the survey!")
# 6-7人:在为完成6-1而编写的程序中,再创建两个表示人的字典,然后将这三个字典都存储在一个名为people的列表中.遍历这个列表,将其中每个人的所有信息都打印出来.
friends_1={'first_name':'李','last_name':'明','age':30,'city':'上海'}
friends_2={'first_name':'新','last_name':'明01','age':30,'city':'北京'}
friends_3={'first_name':'新','last_name':'明02','age':30,'city':'南京'}
people=[friends_1,friends_2,friends_3]
for friends in people:
    print(friends)
# 6-8宠物:创建多个字典,对于每个字典,都使用一个宠物的名称来给它命名;在每个字典中,包含宠物的类型及其主人的名字.将这些字典存储在一个名为pets的列表中,
# 再遍历该列表,并将宠物的所有信息都打印出来.
#同上,此处不再重复
# 6-9喜欢的地方:创建一个名为favorite_places的字典.在这个字典中,将三个人的名字用作键;对于其中的每个人,都存储他喜欢的1~3个地方.为让这个练习更有趣些,可让一些朋友
# 指出他们喜欢的几个地方.遍历这个字典,并将其中每个人的名字及其喜欢的地方打印出来.
favorite_places={
    '李明':['南京','天津','台湾'],
    '新明':['北京','香港'],
    '李东':['海南'],
}
for name,favorite_place in favorite_places.items():
    if len(favorite_place)>1:
       print(name.title()+" loves places are: ")
       for f_place in favorite_place:
              print("\t"+f_place.title())
    else:
        print("\n"+name.title() +" loves place is: "+ str(favorite_place[0].title()))
# 6-10喜欢的数字:修改为完成练习6-2而编写的程序,让每个人都可以有多个喜欢的数字,然后将每个人的名字及其喜欢的数字打印出来.
#不再重复
# 6-11城市:创建一个名为cities的字典,其中将三个城市名用作键;对于每座城市,都创建一个字典,并在其中包含该城市所属的国家,人口约数以及一个有关该城市的事实.在表示
# 每座城市的字典中,应包含country.population和fact等键.将每座城市的名字以及有关它们的信息都打印出来.
cities={
    '上海':{
        'country':'china',
        'population':'30 million people',
        'fact':'beautiful',
    },
    '巴黎':{
        'country':'france',
        'population':'25 million people',
        'fact':'romantic',
    },
    '纽约':{
        'country':'france',
        'population':'27 millio people',
        'fact':'develop',
    }
}
for city_name,city_infos in cities.items():
    city_info="所属国家: "+city_infos['country']+", 人口:"+city_infos['population']+", 特点:"+city_infos['fact']
    print("\n城市名字:"+city_name+" "+city_info)
# 6-12扩展:本章的示例足够复杂,可以以很多方式进行扩展了.请对本章的一个示例进行扩展;添加键和值,调整程序要解决的问题或改进输出的格式.