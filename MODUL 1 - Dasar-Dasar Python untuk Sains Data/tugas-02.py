list1=[3,1,2,5]
list2=[6,4,8,7]
list3=[]

def gabungList():
    global list1, list2, list3
    index = 1
    for i in range(len(list1)):
        if i%2 == 1:
            list3.append(list1[i])
    for i in range(len(list2)):
        if i%2 == 1:
            list3.append(list2[i])
    list3.sort(reverse=True)

gabungList()
print(list3)
