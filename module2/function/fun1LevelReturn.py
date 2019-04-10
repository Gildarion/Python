function = {
        "max":maxFun,
        "min":minFun,
        "average":aveFun
        }

def maxFun(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for num in range(1, len(l)):
    	if num > m:
	    m = l[num]
    return m

def minFun(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for num in range(1, len(l)):
    	if num < m:
	    m = l[num]
    return m

def aveFun(*l):
    if len(l) == 0:
        return 0
    result = 0
    for num in l:
        result += num
    return result / len(l)
result = 0
for num in l:
    result += num
return result / len(l)

def returnFun(name):
    if name.lower() in function.keys():
        return function[name]
    return None

