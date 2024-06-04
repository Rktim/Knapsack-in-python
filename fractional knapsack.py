def qs(a,l,h): #quicksort
    if l<h:
        pi=part(a,l,h)
        qs(a,l,pi-1)
        qs(a,pi+1,h)
        
def part(a,l,h):
    p=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=p:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[+1],a[h]=a[h],a[i+1]
    return i+1

arr = [29, 10, 14, 37, 13]
qs(arr, 0, len(arr) - 1)
print(arr)
