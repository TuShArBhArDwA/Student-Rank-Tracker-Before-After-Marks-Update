def highrank(names,marks,updates):
    Rank1=[]
    Rank2=[]
    d=len(names)
    list2=sorted(marks)
    list3=list2[::-1]
    print("Before Updates, Ranks are:-")
    for i in range(0,d):
        for j in range(0,d):
            if list3[i]==marks[j]:
                print("Rank:",(i+1),"---->",names[j])
            if marks[i]==list3[j]:
                Rank1.append(j+1)
    newlist=[]
    for i in range(0,d):
        newlist.append(marks[i]+updates[i])
    list1=sorted(newlist)
    list5=list1[::-1]
    for i in range(0,d):
        for j in range(0,d):
            if newlist[i]==list5[j]:
                Rank2.append(j+1)
    print("After Updates")
    print("Student with Highest marks is:")
    for i in range(0,d):
        if list5[0]==newlist[i]:
            print("Rank:","1","---->",names[i],"[Final Marks:",list5[0],"]"," ","@","Jump of Rank",Rank1[i]-Rank2[i])
    print("Additionaly Rank of other students:")
    for p in range(1,d):
        for q in range(0,d):
            if list5[p]==newlist[q]:
                print("Rank:",(p+1),"---->",names[q],"[Final Marks:",list5[p],"]"," ","@","Jump of Rank",Rank1[q]-Rank2[q])

a=input("Please Enter the list of Student's Names")
names=a.split(",")

b=input("Please Enter the list of marks obtained by students")
marks=b.split(",")

c=input("Please Enter the list of Updation of numbers")
updates=c.split(",")

d=len(names)
e=len(marks)
f=len(updates)
if d==e and d==f:
    for i in range(0,e):
      marks[i]=float(marks[i])

    for i in range(0,f):
      updates[i]=float(updates[i])

    highrank(names,marks,updates)
else:
    print("Sorry, Lists are of different lengths")
