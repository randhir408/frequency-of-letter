str=('mississippi')
i=0
for e in str:
    if str.index(e)==i:
        print(e,"---",str.count(e))
    i+=1
