
#尋找有哪幾個變數的function，並回傳變數的種類，若變數中包含X,Y,Z，則此函式回傳[X,Y,Z]
def filter1(f,l):
    result=[]
    for x in l:
        if f(x) and x not in result:
            result.append(x)
    return result
isalpha1=lambda a:a.isalpha()

#將多項式中的項分開的function，將每一項存放成一個LIST元素，輸入(X-2*Y)，則回傳[X,-2*Y]          
def split1(l):
    result=[]
    count=0
    index=0
    for x in l:
        if x=="+" or x=="-" or x==")":    #若遇到+，-，)，則分割成多項
            result.append(l[index:(count)])
            index=count
        count=count+1
    if result[0]=="":
        result=result[1:]
    return result

#尋找每一項係數的function，找出上個函式已經分開的每一項中的第一個值，也就是係數
#若輸入為X，則回傳1，若為-3*Y^2，則回傳-3
def findcof(x,i,var):
    cof=0
    con=1
    for a in x:
        if a.isalpha()==True:
            con=0
            break
    if con==1:
        return int(x)
    if i==0:
        if  x[0] in var:
            cof=1
        elif x[0]=="-" and x[1] in var:
            cof=-1
        else:
            j=0
            for s in x:
                if s.isdigit():
                    cof=int(x[0:j+1])
                    break
                j=j+1
        
    else:
        if "*" not in x and x[0]=="+":
            cof=1
        elif "*" not in x and x[0]=="-":
            cof=-1
        else:
            j=0
            for s in x:
                if s=="*":
                    cof=int(x[0:j])
                    break
                j=j+1
    return cof

#矩陣元素相加function，將矩陣元素對應的位置相加，輸入[1,2,3] [1,2,3]則回傳[2,4,6]
def list_add(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

#尋找每一項中各個變數的次方的function，輸入[X^2Y^2Z^2]，則回傳[2,2,2]
def findexp(l,var,num):
    exp=[]
    for i in range(num):
        var_offset=l.find(var[i])
        if var_offset==-1:          
            exp.append(0)           #若變數i不在項中，回傳0次方
        elif var_offset==len(l)-1:
            exp.append(1)           #若變數i在項中的最後一個位置且後面沒有^，回傳一次方
        elif l[var_offset+1]!="^":
            exp.append(1)           #若變數i後面沒有^，回傳一次方
        elif l[var_offset+1]=="^": #and l[var_offset+2]=="-":
            j=var_offset+1
            while j<len(l) and l[j] not in var:
                j=j+1
            exp.append(int(l[var_offset+2:j]))  #找到^後面開始算起後沒有數字的位置，回傳前面的數字
        """
        elif l[var_offset+1]=="^"and l[var_offset+2]=="-":
            j=var_offset+2
            while j<len(l) and l[j] not in var:
                j=j+1
            exp.append(int(l[var_offset+3:j]))
        """
    return exp

#處理兩項相乘的function，係數相乘，次方相加  
def multiply_of_item(item1,item2):
    result=[]
    for a in item1:
        if isinstance(a,Item):
            for l in item2:
                if isinstance(l,Item):      #係數相乘，次方相加，並建立新的物件
                    result.append(Item(a.cof*l.cof,list_add(a.exp,l.exp)))
    return result

#reduce function，自己定義的reduced function
def myreduce(f,l):
    reduced=l[0]
    for x in l[1:]:
        reduced=f(reduced,x)
    return reduced

#將項定義為Item物件
class Item:
    
    def __init__(self,cof,exp):
        self.cof=cof                #此物件包含係數
        self.exp=exp                #以及每一個變數的次方，存成List形式

    def show(self):                 #測試用函式
        print(self.cof,self.exp)

    def print_out(self,var,f):      #用於最後輸出的函式
        num=len(var)
        if self.cof!=0:
            if f==0:
                if self.cof!=1:
                    print(self.cof,"*",end="",sep="")
                elif self.cof==-1:
                    print("-",end="",sep="")
            else:
                if self.cof>0:
                    if self.exp==[0 for i in range(num)]:
                        print("+",self.cof,end="",sep="")
                    elif self.cof!=1:
                        print("+",self.cof,"*",end="",sep="")
                    else:
                        print("+",end="",sep="")
                else:
                    if self.exp==[0 for i in range(num)]:
                        print(self.cof,end="",sep="")
                    elif self.cof==-1:
                        print("-",end="",sep="")
                    else:
                        print(self.cof,"*",end="",sep="")
            for i in range(num):
                if self.exp[i]!=0:
                    if self.exp[i]==1:
                        print(var[i],end="",sep="")
                    else:
                        print(var[i],"^",self.exp[i],end="",sep="")

            

poly1=input("Input the polynomials: ")

var=list(filter1(isalpha1,poly1))   #var用來存放變數的種類，並存成list形式，ex: [X,Y,Z]

poly1=poly1[1:]
poly2=poly1.split("(")      #將多項式分開


poly=[]         #將各個多項式中的每一項分開
for line in poly2:
    
    poly.append(split1(line))

#算出多項式、變數、項數的個數
num_of_poly=len(poly)

num_of_var=len(var)

num_of_item=0

for n in range(num_of_poly):
    if len(poly[n])>num_of_item:
        num_of_item=len(poly[n])


item=[[0]*num_of_item for i in range(num_of_poly)]  #初始化項數矩陣


j=0
k=0
for n in range(num_of_poly):        #將項數的屬性放入Class Item中，每一個項都宣告成一個實體物件
    k=0
    i=0
    for x in poly[n]:
        item[j][k]=Item(findcof(x,i,var),findexp(x,var,num_of_var))
        i=i+1
        k=k+1
    j=j+1


result=myreduce(multiply_of_item,item)    #使用Reduce function處理多項式中的項相乘

type_exp=[]         #尋找總共有幾種次方的組合
for a in result:
    type_exp.append(a.exp)
    


final_result=[]     #初始化最後結果的列表

for exp in type_exp:    #將次方組合一樣的項係數兩兩相加
    tem_cof=0
    i=0
    for a in result:
        if a.exp==exp:
            tem_cof=tem_cof+a.cof
    for a in final_result:
        if a.exp==exp:
            i=1
    if i!=1:    
        final_result.append(Item(tem_cof,exp))
        
f=0
print("Output Result: ",end="")     #輸出
for a in final_result:
    a.print_out(var,f)
    f=1
