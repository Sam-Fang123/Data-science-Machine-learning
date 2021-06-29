#第一題的Function
def question_1(dictlist):
    rating=[]
    for i in range(len(dictlist)):
        if dictlist[i].get('Year')=='2016': #如果年分是2016年，找出那一年的Rating，並assign成Tuple
            rating.append((dictlist[i].get('Title'),dictlist[i].get('Rating'))) 
    rating=sorted(rating,key=lambda x:x[1]) #根據Tuple的第二個元素sort
    ans=[]
    for i in range(3):                      #找出前三名
        ans.append(rating.pop())
    return ans

#第二題的Function
def question_2(dictlist):
    d1={}                               #初始化d1為字典，專門存放Actor:Revenue
    for i in range(len(dictlist)):
        key1=dictlist[i].get('Actors')
        value1=dictlist[i].get('Revenue')
        for a in key1:                  #將Actors一個一個用for取出來
            if a not in d1.keys():      #若a演員不在d1，則初始化將a放入d1的key 
                if value1=="":          #若值不存在，assign成0
                    d1[a]=0.0
                else:                   #存在則將value assign進去
                    d1[a]=float(value1)
            else:                       #若a已經在d1裡了，把revenue加上去 
                if value1!="":
                    d1[a]=d1[a]+float(value1)            
    result=dict(sorted(d1.items(),key=lambda item: item[1],reverse=True)[:1]) #找出第一名
    
    return  result

#第三題的Function
def question_3(dictlist):
    j=0                     #j為相加的筆數  
    rate=0.0                #rate為rating的累積
    for i in range(len(dictlist)):      #如果Emma Watson在演員名單內，rating相加
        if ' Emma Watson' in dictlist[i].get('Actors') or 'Emma Watson' in dictlist[i].get('Actors'):
            rate=rate+float(dictlist[i].get('Rating'))
            j=j+1           #筆數加一
    return rate/j           #rate的累積除上筆數

#第四題的Function
def question_4(dictlist):
    d1={}           #初始化d1字典
    result={}       #初始化result字典
    for i in range(len(dictlist)):
        key1=dictlist[i].get('Director')       #key1為director
        value1=dictlist[i].get('Actors')       #value1為actors名單
        if key1 not in d1.keys():              #如果導演不在d1字典中，初始化新的導演key
            d1[key1]=value1
        else:                                  #如果導演在d1字典中了
            for name in value1:                #將演員一個一個從演員名單中取出
                if name not in d1.get(key1):   #如果演員1不在導演合作過的名單中再相加，避免重複
                    d1[key1]=d1[key1]+[name]
    for key ,value in d1.items():
        result[key]=len(value)                 #result為每個導演合作過的演員數
    return dict(sorted(result.items(),key=lambda item: item[1],reverse=True)[:3])   #找出前三名

#第五題的Function
def question_5(dictlist):
    d1={}       #初始化d1字典
    result={}   #初始化result字典
    for i in range(len(dictlist)):
        key1=dictlist[i].get('Actors')      #key1為電影的演員名單
        value1=dictlist[i].get('Genre')     #value1為電影的Genre
        for a in key1:                      #將演員從key1中一個一個取出
            if a not in d1.keys():          #如果演員不在字典d1中，初始化
                d1[a]=value1                
            else:                           #如果演員在d1中了
                for g in value1:            #將種類一個一個從value1取出
                    if g not in d1.get(a):  #如果種類不在某演員的value中，再assign，避免重複
                        d1[a]=d1[a]+[g]
    for key,value in d1.items():        
        result[key]=len(value)              #求出每個演員演過的種類個數
    return dict(sorted(result.items(),key=lambda item: item[1],reverse=True)[:2])#找出前二多的

#第六題的Function
def question_6(dictlist):
    d1={}       #初始化d1字典
    result={}   #初始化result字典
    for i in range(len(dictlist)):
        key1=dictlist[i].get('Actors')      #key1為演員列表
        value1=dictlist[i].get('Year')      #value1為年份
        for a in key1:
            if a not in d1.keys():          #如果演員不在d1的key
                d1[a]=[int(value1)]         #初始化並給予年份值
            else:
                d1[a]=d1[a]+[int(value1)]   #如果演員在d1的key，將演過的年份串接成list
        for key,value in d1.items():
            result[key]=max(value)-min(value)   #最大值減最小值
    return dict(sorted(result.items(),key=lambda item: item[1],reverse=True)[:53])
    #有53個10年的，印出53筆

#第七題的Function
def question_7(actor,dictlist,actor_list):  #actor為要找的演員，dictlist為傳入的字典
    for i in range(len(dictlist)):          #actor_list為串接並輸出的資料
        value=dictlist[i].get('Actors')     #value=演員名單
        if actor in value:                  #如果要找的演員在演員名單內
            for a in value:                 
                if a not in actor_list:     #如果跟要找的演員合作過的演員不在actor_list中則串接
                    actor_list.append(a)
                    question_7(a,dictlist,actor_list)  #使用Recursion的方法，串接直到重覆
                else:
                    continue                #若重複了則不呼叫原函式
    return actor_list       

lineList=[]
with open("IMDB-Movie-Data.csv",mode="r") as file:
    for line in file:
        lineList.append(line.strip())
#print(lineList[3])

linelist=[]
for i in range(len(lineList)):
    linelist.append(lineList[i].split(","))     #將資料讀入，並用，分開

for i in range(len(linelist)):

    linelist[i][4]=linelist[i][4].split("|")    #將演員的名單用|分開
    linelist[i][2]=linelist[i][2].split("|")    #將種類名單用|分開
for i in range(len(linelist)):                  #消除演員名單中的空格
    j=0
    for l in linelist[i][4]:
        if l[0]==" ":                           #若有空格則消除
            linelist[i][4][j]=l[1:]
        j=j+1

dictlist={}
for i in range(1,len(linelist)):                #將資料存入字典
    dictlist[i-1]=dict(Title=linelist[i][1],Genre=linelist[i][2],Director=linelist[i][3],Actors=linelist[i][4],Year=linelist[i][5],Rating=linelist[i][7],Revenue=linelist[i][9])

#輸出最後解答
print("Top-3 movies with the highest ratings in 2016:")
print(question_1(dictlist))
print("\nThe actor generating the highest average revenue:")
print(question_2(dictlist))
print("\nThe average rating of Emma Watson’s movies: ")
print(question_3(dictlist))
print("\nTop-3 directors who collaborate with the most actors: ")
print(question_4(dictlist))
print("\nTop-2 actors playing in the most genres of movies:")
print(question_5(dictlist))
print("\nTop-3 actors whose movies lead to the largest maximum gap of years:")
print(question_6(dictlist))
actor_list=['Johnny Depp']         #第七題串接資料初始化
ans_7=question_7('Johnny Depp',dictlist,actor_list)  #第一次遞迴使用Johnny Depp
print("\nFind all actors who collaborate with Johnny Depp in direct and indirect ways: ")
print(ans_7)
print("There are",len(ans_7),"actors who collaborate with Johnny Depp in direct and indirect ways")   

