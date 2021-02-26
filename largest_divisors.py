def largestDivisor(arr):
  lst = []
  for i in arr:
    if i%2 == 0:
      lst.append(int(i/2))
    else:
      n = smallestDivisor(i)
      N = int(i/n)
      lst.append(N)
  return lst

def smallestDivisor(num):
  for i in range(3,int(math.sqrt(num)+1),2):
    if num%i == 0:
      return i
  return num
