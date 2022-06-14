def s(a,*spisok):
    col = 0
    for i in spisok:
        if i>a:
            col+=1
    print(col)
s(3,5,4,1,2)
def mn(a,b):
    return a/b
print(mn(1,2))