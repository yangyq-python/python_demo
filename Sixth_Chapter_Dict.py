#:在Python中字典是一系列键-值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表
#乃至字典。事实上，可将任何Python对象用作字典的值。在Python中，用放在花括号{}的一系列键-值对表示
#键-值对是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔，而键-值对之间用逗号分隔。在字典中，你想存储
#多个少键-值对都可以。
alien_0={'color':'green','points':'5'}
print(alien_0['color'])
print(alien_0['points'])
#a.访问字典中的值：要获取与键相关联的值，可依次指定字典名和放在放括号内的键，
new_points=alien_0['points']
print("You just earned "+str(new_points) +" points!")
#b.添加键-值对:字典是一种动态结构，可随时在其中添加键-值对。要添加键-值对，可依次指定字典名、用方括号括起的键和相关联的值。
alien_0['x_position']=0  #往字典alien_0中添加键-值对
alien_0['y_position']=25
print(alien_0)
#c.创建一个空字典：有时候，在空字典中添加键-值对是为了方便，而有时候必须这样做。为此，可先使用一对空的花括号定义一个字典，
# 再分行添加各个键-值对。
alien_0={}
alien_0['color']='red'
alien_0['points']='10'
print(alien_0)
#d.修改字典中的值:要修改字典中的值，可依此指定字典名、方括号括起的键以及该键相关联的新值。
print("The alien is "+alien_0['color'] +".")
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+".")

alien_0={'x_position':0,'y_position':25,'speed':'fast'}
print("Original x_position: "+str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3
#新位置等于老位置加上增量
# alien_0['x_position']=alien_0['x_position']+x_increment
alien_0['x_position']+=x_increment
print("New x-position: "+ str(alien_0['x_position']))
print(alien_0)
#e.删除键-值对:对于字典不中不再需要的信息，可使用del语句将相应的键-值对彻底删除。使用del语句时，必须指定字典名和要删除的值。
# PS:删除的键-值对永远消失了。所以要慎重使用
alien_0={'color':'green','points':'5'}
print("未删除之前字典的内容：")
print(alien_0)
del  alien_0['points']
print('删除points键之后的内容：'+str(alien_0))
#f.由类似对象组成的字典:在前面的示例中，字典存储的是一个对象（游戏中的一个外星人），但你也可以使用字典来存储众多对象的同一种信息。
favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
print("Sarah's favorite language is " +favorite_languages['sarah'].title()+".")

# ***********************遍历字典**************************
# a.遍历所有的键-值对：可以用for循环和items()方法[返回一个键-值对列表]
user_0={'username':'efermi','first':'enrico','last':'fermi'}
for key,value in user_0.items():   #for循环中声明的两个变量，用于存储键-值对中的键和值，对于这两个变量，可使用任何名称。
    print("\nKey:"+key)  #注意：即便遍历字典时，键-值对的返回顺序也与存储顺序不同，Python不关心键-值的存储顺序，只跟踪键-值之间的关联关系。
    print("\nValue:"+value)
# b.遍历字典中的所有键：在不需要使用字典中的值时，方法keys()很有用。
# for name in favorite_languages.keys():  #提取字典中的所有键，并依次将它们存储到变量name中。
for name in favorite_languages:  #遍历字典时，会默认遍历所有的键，因此，如果将上述代码替换该行，输出将不变。
    print(name.title())
#如果显式地使用keys()可让代码更容易理解【即上面注释掉的for循环】，但如果你愿意，也可以省略它。
print("使用当前键来访问与之相关联的值。")
friends=['phil','sarah']  #创建一个列表
for name in favorite_languages.keys():  #遍历字典中所有的key
    print(name.title())
    if name in friends:  #检查当前的名字是否在列表中，如果在，则打印出一条特殊的问候语，
        print("Hi "+name.title()+", I see your favorite language is "+favorite_languages[name].title()+"!") #将变量name的当前值作为键

print("还可以使用keys()确定某个人是否在列表中")
if 'earn' not in favorite_languages.keys():  #keys()并非只用于遍历；实际上，它返回一个列表，其中包含字典中的所有键
    print("Erin,please take our poll!")
# c.按顺序遍历字典中的所有键：字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
# 这不是问题，因为通常你想要的只是获取与键相关联的正确的值。要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。
# 为此，可使用函数sorted()来获的按特定顺序排列的键列表的副本：
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")
# d.遍历字典中的所有值:可使用方法values()，它返回一个值列表，而不包含任何键。
print("The following languages have been mentioned:")
for language in favorite_languages.values(): #这条for语句提取字典中的每个值，并将它们依次存储到变量language中。【其实返回的是一个列表】
    print(language.title())
#这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但很多时，最终的列表可能包含大量的重复项。
# 为剔除重复项，可使用集合（set），集合类似于列表，但每个元素都必须是独一无二的：
print("剔除提取字典中重复的值")
for language in set(favorite_languages.values()):
    print(language.title())
# print(type(set(favorite_languages.values())))

# ****************嵌套************************
# 嵌套：有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
# a.字典列表:
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]  #把上面创建的三个字典都放在列表中
for alien in aliens:
    print(alien)
#而在现实中，代表外星人字典不止三个，且每个外星人都是使用代码自动生成的。
aliens=[]  #创建一个用于存储外星人的空列表
for alien_number in range(30): #创建30个绿色的外星人
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:    #修改前三个外星人为黄色的、速度为中等且值10个点：
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    if alien['color']=='yellow':  #将黄色外星人改为移动速度快且值15个点的红色外星人
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

for alien in aliens[:5]: #显示前五个外星人
    print(alien)
print(".....")
print("Total number of aliens: "+str(len(aliens))) #统计外星人的总数。
# b.在字典中存储列表：有时候，需要将列表存储在字典中，而不是将字典存储在列表中；可以使用字典名和键，就像访问字典中的其他值一样
pizza={  #存储缩点披萨的信息
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'], # 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
}
#概述所点的披萨
print("You ordered a "+pizza['crust']+"-crust pizza"+
      " with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages={  #与每个名字相关联的值都是一个列表
    'Jen' : ['python','ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby','go'],
    'phil': ['python','haskell'],
}

for name,languages in favorite_languages.items(): #遍历字典时，我们使用了变量languages来依次存储字典中的每个值，这些值都是列表
    if len(languages)>1:#通过查看len(languages)的值来确定当前的被调查者喜欢的语言是否有多种。然后分类打印
      print("\n"+name.title()+"'s favorite languages are: ")
      for language in languages:  # 在遍历字典的循环中，使用了一个for循环来遍历每个人喜欢的语言列表，现在，每个人想列出多少种喜欢的语言都可以：
          print("\t" + language.title())
    else:
        print("\n"+name.title()+"'s favorite languages is: "+str(languages[0]).title())
#列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决问题的方案。
# c.在字典中存储字典：可在字典种嵌套字典，但这样做时，代码可能很快复杂起来。
# 例如，如果有多个网站用户，每个都有独特的用户名，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。
# 在下面的程序中,对于每位用户,我们都存储了其三项信息:名,姓和居住地;为访问这些信息,我们遍历所有的用户名,并访问与每个用户名相关联的信息字典:
users={   #users字典包含两个键:用户名'aeinstein'和'mcurie',与每个键相关联的值都是一个字典,包含用户的名,姓和居住地
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princetion',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for  username,user_info in users.items():  #遍历字典users时,依次将每个键存储在变量username中,同时将与当前键相关联的字典存储在变量user_info中,
    print("\nUsername"+username)   #打印用户名
    full_name=user_info['first']+" "+user_info['last']
    location = user_info['location']

    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
#请注意,表示每位用户的字典的结构都相同,虽然Python并没有这样的要求,但这使得嵌套的字典处理起来更容易.倘若表示每位用户的字典都包含不同的键,则for循环内部的代码更复杂.
