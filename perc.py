math =int(input("enter maths marks: "))
science =int(input("enter science marks: "))
english =int(input("enter english marks: "))
hindi =int(input("enter hindi marks: "))
sst =int(input("enter sst marks: "))
sum=math+science+english+hindi+sst

perc = (sum/400)*100
print("total marks are: ",sum)
print("percentage obtained: ",perc)