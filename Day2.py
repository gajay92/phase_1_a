for i in range (11):
    print(i**2)
#temp1

myMatrix =[[1,2,3],
           [4,5,6],
           [7,8,9]]

for i in range(3):
    for j in range(3):
        tmp = myMatrix[i][j]**2
        myMatrix[i][j] = tmp
        print(myMatrix[i][j])
#temp1

myMatrix =[[1,2,3],
           [4,5,6],
           [7,8,9]]
for i in myMatrix:
    for j in i:
        print (j**2)
#temp2


myMatrix =[[1,2,3],
           [4,5,6],
           [7,8,9]]
len(myMatrix[0])
for i in range(len(myMatrix)):
    for j in range(len(myMatrix[i])):
        #print(myMatrix[i][j] **2)
        myMatrix[i][j] **= 2
print(myMatrix)

#FUNC
def prod_value(a,b):
    c= a*b
    return c


tt = areaCircle(5)
print(tt)


def prod(a, b):
    c = a * b
    return c


def areaCircle(r):
    r2 = prod(r, r)
    area = prod(3.1415, r2)
    return area

## done

##factorial program

def facto(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*facto(n-1)