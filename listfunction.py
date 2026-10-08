num=[11,23,18,45,78,76,92,14,15,54]
#create the list of 10 num and print the sum of last 4 num
sum_last4=sum(num[-4:])
print("sum of last : ",sum_last4)

#find the difeer betn max and min number in list 
diff=sorted(num)[-1]- sorted(num)[0]
print("differnce of min and last num of list : ",diff)
#insert a num in list at 6th position this num must be 1/3 rd num stored at 4th position  
num.insert(5,num[3]/3)
print("number at inseted at 6th positon ",num)
