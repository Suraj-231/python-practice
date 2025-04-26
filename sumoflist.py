#using for loop
mylist= [1,7,9,8,15,77] #variables to be used as list
total=0
#loop through index 0 tp nth number int the list and then add current element to the total
for i in range(0, len(mylist)):
    total=total+ mylist[i]
print("sum of all elements in the list: ",total)#print sum after end of loop
