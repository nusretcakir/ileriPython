
# liste = [1,2,3,4,4,5]

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res

def carp(**kwargs):
    res=1
    for i in kwargs.values():
        res *= i
    return res

def karisik(*args,**kwargs):

    for i,j in kwargs.items():
        print(i,j)

    res = 0
    for i in args:
        res += i
    return res

print("sum func:",sum(1,2,3))
print("*"*10)
print("carp func:",carp(a=2,b=3,c=4))
print("*"*10)
print("karisik func:",karisik(1,2,isim="Linux",soyIsim="Tornvald"))
print("*"*30)

dict1 = {"name":"Denzel","surname":"Washington"}
dict2 = {"best_number":13,"job":"Actor"}

print({**dict1,**dict2})
