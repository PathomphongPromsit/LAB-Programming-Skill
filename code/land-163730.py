x, y, x_i, y_i, x_ii, y_ii =[int (i) for i in input().split()]
sum_x = x_i + x_ii 
sum_y = y_i + y_ii
area_one = (x - sum_x) * y 
area_two = (y - sum_y) * x 

area_three = (y - y_ii) * (x - x_i)
area_four = (y - y_i) * (x - x_ii)

if area_one > area_two:
    if area_three > area_four:
        if area_three > area_one:
            print(area_three)
        else:
            print(area_one)
    else: 
        if area_four > area_one:
            print(area_four)
        else:
            print(area_one)
else:
    if area_three > area_four:
        if area_three > area_two:
            print(area_three)
        else:
            print(area_two)
    else: 
        if area_four > area_two:
            print(area_four)
        else:
            print(area_two)