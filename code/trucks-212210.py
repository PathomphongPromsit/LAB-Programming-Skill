while True:
  

  quantity, limit_weight = [int(i) for i in input().split()]
  count = 1
  N = limit_weight
  if (quantity == 0) and (limit_weight == 0):
    break
  
  else:
    data = input().split()
    for i in data:
      value = int(i)
      if (N - value) >= 0:
        N -= value
      else:
        count += 1
        N = limit_weight
        N -= value
    print (count)
