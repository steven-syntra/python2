myset = {"apple", "banana", "cherry"}
mylist = ["apple", "banana", "cherry"]
mylist.append("pineapple")
mylist.append("pineapple")
myset = set(mylist)
mysecondlist = list(myset)
mysecondlist.sort()
print(mysecondlist)