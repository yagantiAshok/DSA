



def merge(l1,s,m,e):
    
    i = s
    j= m+1
    ans = []

    while (i<=m) and (j<=e):

        if (l1[i]<l1[j]):

            ans.append(l1[i])
            i = i+1
        
        elif (l1[i]>l1[j]):

            ans.append(l1[j])

            j = j+1

        elif (l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i =  i + 1
            j = j + 1
        

    while (i<=m):
        ans.append(l1[i])
        i=i+1

    while (j<=e):
        ans.append(l1[j])
        j = j + 1

    startofmyANS= 0
    start0fmylist = s

    while (start0fmylist<=e):

        l1[start0fmylist] = ans[startofmyANS]

        startofmyANS+=1
        start0fmylist+=1
    
    return l1


def mergesort(l1,s,e):

    if (s>=e):
        return 
    
    middle = s + (e-s)//2

    mergesort(l1,s,middle)
    mergesort(l1,middle+1,e)

    ans = merge(l1,s,middle,e)

    return ans 


l1 = [2,0,3,1,10,8,7,6]

print(mergesort(l1,0,len(l1)-1))

# print(l1)

    