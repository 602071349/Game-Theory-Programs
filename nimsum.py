import math
def get_nimsum(games):
    nimsum=0
    for i in games:
        nimsum=nimsum^i
    return nimsum

def cal(lst,position):
    return calculate_g(lst,position,[-1 for x in range(position)])
def calculate_g(lst,position,lst_result):
    if position==0:
        return 0
    else:
        lst_g=[]
        for i in lst[position][1]:
            if lst_result[i]!=-1:
                lst_g+=[lst_result[i]]
            else:
                x=calculate_g(lst,i,lst_result)
                lst_result[i]=x
                lst_g+=[x]
        gvalue=0
        while(gvalue in lst_g):
            gvalue+=1
        return gvalue

def get_nimsum_games(lst_of_games):
    lstg=[]
    for i in lst_of_games:
        lstg+=[calculate_g(i,len(i)-1)]
    g=get_nimsum(lstg)
    return g

def create_list(chips,sub_set):
    lst=[(x,[x-y for y in sub_set if x>=y]) for x in range(0,chips+1)]
    return lst
def g_of_games(lst):
    lst1=[]
    for i in lst:
        lst1+=[create_list(i[0],i[1])]
    g=get_nimsum_games(lst1)
    return g
x=create_list(100,[1,3,5,7])
print(cal(x,100))
y=create_list(100,[1,3,6])
print(cal(y,100))
z=create_list(100,[2**i for i in range(int(math.log(100,2)))])
print(cal(z,100))


