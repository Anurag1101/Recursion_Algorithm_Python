def count(n): #recursive function
    if(n==0): #base case
        return
    print(n)
    count(n-1)
count(5)

def fact(n): #factorial using recursion
    if(n==0 or n==1):
        return 1
    else:
        return  fact(n-1)*n
print(fact(6))

def sum(n): #sum of first n natural number using recursion
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(20))

def count(li,ind=0): #print element of list using recusrion
    if(ind==len(li)):
        return
    print(li[ind])
    count(li,ind+1)

fruits=["apple","mango","banana","guava"]
count(fruits)

