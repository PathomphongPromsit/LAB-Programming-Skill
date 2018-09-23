def tidy(data):
    if len(data) == 1:
        return data
    prev = "0"
    for i in range(len(data)):
        value = data[i] 
        if value < prev:
            left = str(int(data[:i])-1)
            right = "9" * (len(data) - i)
            return tidy(left + right)
        prev = value
    return int(data)
T = int(input())
for i in range(T):
    print("Case #" + str(i+1)+":",tidy(input()))