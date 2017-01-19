def minimum(data):
    n = []
    for num in data:
        if num < n:
            n = num
    return n
def large(data):
  n=[]
  for num in data:
    if num < n:
      n = num
    return n
    
data = [67,4,67,2,34,10]
print(minimum(data))
print(large(data))