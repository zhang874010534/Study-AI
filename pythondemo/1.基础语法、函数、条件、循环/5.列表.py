from ast import List


lis = [1, 2, 4, 3]
print(len(lis))
print(max(lis))
print(min(lis))
print(sum(lis))
print(sorted(lis))
print(sorted(lis, reverse = True)) # 从大到小
print(list(reversed([1,2,3])))

lis.reverse()
print(lis)
# lis.sort()
# print(lis)

str = 'hello'
strList = list(str)
strList.reverse()
print('|'.join(strList))
