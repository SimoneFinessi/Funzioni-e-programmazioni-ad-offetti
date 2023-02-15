def convertitore(a):
    return [(a[i],i) for i in range(len(a)-1)]
print(convertitore([1,2,3,4,5,6]))