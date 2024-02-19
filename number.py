def largest_number(number, n):
    number.sort()
    
    return number[-n:]


nums  = [1,23,33,44,33,22,55,66]

print(nums)
largest = largest_number(nums, 2)
print(nums)



a= [[j for j in range(5)] for i in range(10)]
print(a)




def compilcated_fuction(*args, **kwargs):
    print(args, kwargs)
    pass


compilcated_fuction(2,5 , 1,24,5,6,346,3, b=34, c= True, d="hello")


def compilcated_fuction(a, b, c=True, d=4):
    print(a, b)
    pass


compilcated_fuction(*[1,3])

def com(a,b, c=True, d=4):
    print(a,b,c,d)
    pass

com(*[1,3], **{"c":"hello", "d": "cool"})