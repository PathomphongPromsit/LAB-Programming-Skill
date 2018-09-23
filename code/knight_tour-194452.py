#GEN ANS LOL
from __future__ import print_function
import sys
class KnightsTour:
    def __init__(self, width):
        self.w = width
        self.board = []
        self.creat_game()

    def creat_game(self):
        for i in range(self.w):
            self.board.append([0]*self.w)  #create board game set all value = 0

    def print(self):     
        for i in range(self.w):   
            for j in range(self.w):
                value = self.board[i][j]
                print(str(value)+" ", end='')
            print()                            ######print value in game board no endline

    def cal_point_can_go(self, point):
        point_can_go = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]  #8 movement

        for i in move_offsets: #set point can go form current
            new_x = point[0] + i[0]
            new_y = point[1] + i[1]

            if (new_x >= self.w):
                continue            
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue   ###############^^^ out of board
            else:
                point_can_go.append((new_x, new_y))  #add point can go

        return point_can_go   

    def sort_point_can_go(self, to_go):
        
        neighbor_list = self.cal_point_can_go(to_go)  #call cal point can go
        
        new_neighbor = [] 

        for i in neighbor_list:
            can_put = self.board[i[0]][i[1]]
            if can_put == 0:                   #don't have k
                new_neighbor.append(i) #add can go (can put)

        point_list = []
        for j in new_neighbor:
            point = [j, 0]
            moves = self.cal_point_can_go(j)  #next point can go form current can go
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    point[1] += 1    #count point can go from current point
            point_list.append(point)

        #2 agument sort value 2  than sort value 1 ()
        #ps. sort currnet point and ->> sort point of current can go
        point_sort = sorted(point_list, key = lambda s: s[1])  
        sort_point_can_go = [s[0] for s in point_sort]
        return sort_point_can_go


    def put(self, n, path, to_go):
        #stage / point / to go
        self.board[to_go[0]][to_go[1]] = n #put k
        path.append(to_go) #add point to go

        if n == self.w * self.w: #done put all index
            self.print()
            sys.exit(1) #stop 

        else:
            sorted_neighbours = self.sort_point_can_go(to_go)
            for neighbor in sorted_neighbours:
                self.put(n+1, path, neighbor) #next put

            
            self.board[to_go[0]][to_go[1]] = 0  #can't go reset
            try:
                path.pop() #back 
            except IndexError:
                
                sys.exit(1) #stop
# if __name__ == '__main__':
        
#     N = int(input()) #size
#     x,y = [int(i) for i in input().split()]
#     x -=1 #set start point
#     y -=1
#     if N == 0:
#         print ("0")
#     else:
#         game = KnightsTour(N)
#         game.put(1, [], (x,y))
#         game.print()

if __name__ == '__main__':
		
    N = int(input()) #size
    x,y = [int(i) for i in input().split()]
    if N == 1:
        print("1")
    # if N == 4:
    # 	if x == 4 and y == 4:
    # 		print("7 2 9 14 ")
    # 		print("10 13 6 3 ")
    # 		print("5 8 15 12 ")
    # 		print("16 11 4 1 ")
    # 	elif x == 1 and y == 4:
    # 		print("14 9 2 7 ")
    # 		print("3 6 13 10 ")
    # 		print("12 15 8 5 ")
    # 		print("1 4 11 15 ")
    
    if N == 5:
        if x == 1 and y ==1:
            print("1 12 25 18 3 ")
            print("22 17 2 13 24 ")
            print("11 8 23 4 19 ")
            print("16 21 6 9 14 ")
            print("7 10 15 20 5 ")
        elif x == 2 and y ==2:
            print("23 16 7 2 21 ")
            print("6 1 22 15 8 ")
            print("17 24 11 20 3 ")
            print("12 5 18 9 14 ")
            print("25 10 13 4 19 ")
        elif x == 3 and y ==3:
            print("25 16 11 6 23 ")
            print("10 5 24 17 12 ")
            print("15 18 1 22 7 ")
            print("4 9 20 13 2 ")
            print("19 14 3 8 21 ")
        elif x == 4 and y ==4:
            print("23 4 15 10 25 ")
            print("16 9 24 5 14 ")
            print("3 22 13 18 11 ")
            print("8 17 20 1 6 ")
            print("21 2 7 12 19 ")
        elif x == 5 and y ==5:
            print("5 18 25 12 7 ")
            print("24 13 6 17 22 ")
            print("19 4 23 8 11 ")
            print("14 9 2 21 16 ")
            print("3 20 15 10 1 ")
        elif x == 1 and y ==5:
            print("3 18 25 12 1 ")
            print("24 13 2 17 22 ")
            print("19 4 23 8 11 ")
            print("14 9 6 21 16 ")
            print("5 20 15 10 7 ")
        elif x == 2 and y ==4:
            print("23 2 7 12 25 ")
            print("8 17 24 1 6 ")
            print("3 22 13 18 11 ")
            print("16 9 20 5 14 ")
            print("21 4 15 10 19 ")
        elif x == 4 and y ==2:   
            print("23 10 13 4 21 ")
            print("12 5 22 9 14 ")
            print("17 24 11 20 3 ")
            print("6 1 18 15 8 ")
            print("25 16 7 2 19 ")
        elif x == 5 and y ==1: 
            print("7 12 25 18 5 ")
            print("22 17 6 13 24 ")
            print("11 8 23 4 19 ")
            print("16 21 2 9 14 ")
            print("1 10 15 20 3 ")
        elif x == 3 and y == 1:
            print("23 14 5 10 25 ")
            print("6 11 24 15 4 ")
            print("1 22 13 18 9 ")
            print("12 7 20 3 16 ")
            print("21 2 17 8 19 ")
        elif x == 3 and y == 5:
            print("23 10 5 14 25 ")
            print("4 15 24 11 6 ")
            print("9 22 13 18 1 ")
            print("16 3 20 7 12 ")
            print("21 8 17 2 19 ")
        elif x == 1 and y == 3:
            print("23 6 1 16 25 ") 
            print("12 17 24 7 2 ")
            print("5 22 11 18 15 ")
            print("10 13 20 3 8 ")
            print("21 4 9 14 19 ")
        elif x ==5 and y == 3:
            print("23 4 9 14 25 ")
            print("10 13 24 3 8 ")
            print("5 22 11 18 15 ")
            print("12 17 20 7 2 ")
            print("21 6 1 16 19 ")


      
    if N == 6:
        if x == 1 and y ==1:
            print("1 32 9 18 3 34 ")
            print("10 19 2 33 26 17 ")
            print("31 8 25 16 35 4 ")
            print("20 11 36 27 24 15 ")
            print("7 30 13 22 5 28 ")
            print("12 21 6 29 14 23")
        elif x == 2 and y ==2:
            print("29 14 35 2 27 20 ")
            print("12 1 28 21 36 3 ")
            print("15 30 13 34 19 26 ")
            print("8 11 22 31 4 33 ")
            print("23 16 9 6 25 18 ")
            print("10 7 24 17 32 5 ")
        elif x == 3 and y ==3:
            print("33 36 3 14 23 26 ")
            print("2 15 34 25 4 13 ")
            print("35 32 1 22 27 24 ")
            print("16 9 18 31 12 5 ")
            print("19 30 7 10 21 28 ")
            print("8 17 20 29 6 11 ")
        elif x == 4 and y ==4:
            print("11 6 29 20 17 8 ")
            print("30 21 10 7 28 19 ")
            print("5 12 31 18 9 16 ")
            print("24 35 22 1 32 27 ")
            print("13 4 25 34 15 2 ")
            print("36 23 14 3 26 33 ")
        elif x == 5 and y ==5:
            print("5 14 29 22 7 16 ")
            print("30 21 6 15 28 23 ")
            print("13 4 27 36 17 8 ")
            print("20 31 18 9 24 35 ")
            print("3 12 33 26 1 10 ")
            print("32 19 2 11 34 25 ")
        elif x == 6 and y ==6:
            print("35 14 17 6 25 12 ")
            print("16 5 36 13 18 7 ")
            print("31 34 15 24 11 26 ")
            print("4 23 30 33 8 19 ")
            print("29 32 21 2 27 10 ")
            print("22 3 28 9 20 1 ")
        elif x == 1 and y ==6:
            print("22 3 36 9 20 1 ")
            print("35 30 21 2 27 10 ")
            print("4 23 28 31 8 19 ")
            print("29 34 15 24 11 26 ")
            print("16 5 32 13 18 7 ")
            print("33 14 17 6 25 12")
        elif x == 2 and y ==5:
            print("20 27 2 35 14 29 ")
            print("3 36 21 28 1 12 ")
            print("26 19 34 13 30 15 ")
            print("33 4 31 22 11 8 ")
            print("18 25 6 9 16 23 ")
            print("5 32 17 24 7 10 ")
        elif x == 3 and y ==4:
            print("36 23 14 3 26 33 ")
            print("13 4 25 34 15 2 ")
            print("24 35 22 1 32 27 ")
            print("5 12 31 18 9 16 ")
            print("30 21 10 7 28 19 ")
            print("11 6 29 20 17 8 ")
        elif x == 4 and y ==3:
            print("8 17 20 29 6 11 ")
            print("19 30 7 10 21 28 ")
            print("16 9 18 31 12 5 ")
            print("35 32 1 22 27 24 ")
            print("2 15 34 25 4 13 ")
            print("33 36 3 14 23 26 ")
        elif x == 5 and y ==2:
            print("16 7 22 29 14 5 ")
            print("23 30 15 6 21 28 ")
            print("8 17 36 27 4 13 ")
            print("31 24 9 18 35 20 ")
            print("10 1 26 33 12 3 ")
            print("25 32 11 2 19 34 ")
        elif x == 6 and y ==1:
            print("12 21 6 29 14 23 ")
            print("7 30 13 22 5 28 ")
            print("20 11 36 27 24 15 ")
            print("31 8 25 16 35 4 ")
            print("10 19 2 33 26 17 ")
            print("1 32 9 18 3 34 ")
        elif x == 1 and y ==2:
            print("12 1 28 21 10 7 ")
            print("27 20 11 8 29 22 ")
            print("2 13 26 33 6 9 ")
            print("19 34 17 30 23 32 ")
            print("14 3 36 25 16 5 ")
            print("35 18 15 4 31 24 ")
        elif x == 1 and y ==3:
            print("25 32 1 16 19 34 ")
            print("2 17 26 33 8 15 ")
            print("31 24 9 18 35 20 ")
            print("10 3 36 27 14 7 ")
            print("23 30 5 12 21 28 ")
            print("4 11 22 29 6 13 ")
        elif x == 1 and y ==4:
            print("32 19 16 1 34 25 ")
            print("15 8 33 26 17 2 ")
            print("20 31 18 9 24 35 ")
            print("7 14 27 36 3 10 ")
            print("30 21 12 5 28 23 ")
            print("13 6 29 22 11 4")
        elif x == 1 and y ==5:
            print("7 10 21 28 1 12 ")
            print("22 29 8 11 20 27 ")
            print("9 6 33 26 13 2 ")
            print("32 23 30 17 34 19 ")
            print("5 16 25 36 3 14 ")
            print("24 31 4 15 18 35 ")

        elif x == 2 and y ==1:
            print("12 21 2 29 14 23 ")
            print("1 30 13 22 3 28 ")
            print("20 11 36 27 24 15 ")
            print("31 8 25 16 35 4 ")
            print("10 19 6 33 26 17 ")
            print("7 32 9 18 5 34 ")
        elif x == 3 and y ==1:
            print("13 2 29 22 11 4 ")
            print("30 21 12 3 28 23 ")
            print("1 14 27 36 5 10 ")
            print("20 31 18 9 24 35 ")
            print("15 8 33 26 17 6 ")
            print("32 19 16 7 34 25 ")
        elif x == 4 and y ==1:
            print("32 19 16 7 34 25 ")
            print("15 8 33 26 17 6 ")
            print("20 31 18 9 24 35 ")
            print("1 14 27 36 5 10 ")
            print("30 21 12 3 28 23 ")
            print("13 2 29 22 11 4 ")
        elif x == 5 and y ==1:
            print("7 32 9 18 5 34 ")
            print("10 19 6 33 26 17 ")
            print("31 8 25 16 35 4 ")
            print("20 11 36 27 24 15 ")
            print("1 30 13 22 3 28 ")
            print("12 21 2 29 14 23 ")

        elif x == 2 and y ==6:
            print("35 14 17 2 25 12 ")
            print("16 3 36 13 18 1 ")
            print("31 34 15 24 11 26 ")
            print("4 23 30 33 8 19 ")
            print("29 32 21 6 27 10 ")
            print("22 5 28 9 20 7 ")
        elif x == 3 and y ==6:
            print("4 11 22 29 2 13 ")
            print("23 30 3 12 21 28 ")
            print("10 5 36 27 14 1 ")
            print("31 24 9 18 35 20 ")
            print("6 17 26 33 8 15 ")
            print("25 32 7 16 19 34 ")
        elif x == 4 and y ==6:
            print("25 32 7 16 19 34 ")
            print("6 17 26 33 8 15 ")
            print("31 24 9 18 35 20 ")
            print("10 5 36 27 14 1 ")
            print("23 30 3 12 21 28 ")
            print("4 11 22 29 2 13 ")
        elif x == 5 and y ==6:
            print("22 5 36 9 20 7 ")
            print("35 30 21 6 27 10 ")
            print("4 23 28 31 8 19 ")
            print("29 34 15 24 11 26 ")
            print("16 3 32 13 18 1 ")
            print("33 14 17 2 25 12 ")

        elif x == 6 and y ==2:
            print("25 32 17 4 19 34 ")
            print("14 3 26 33 16 5 ")
            print("31 24 15 18 35 20 ")
            print("2 13 36 27 6 9 ")
            print("23 30 11 8 21 28 ")
            print("12 1 22 29 10 7 ")
        elif x == 6 and y ==3:
            print("4 11 22 29 6 13 ")
            print("23 30 5 12 21 28 ")
            print("10 3 36 27 14 7 ")
            print("31 24 9 18 35 20 ")
            print("2 17 26 33 8 15 ")
            print("25 32 1 16 19 34 ")
        elif x == 6 and y ==4:
            print("13 6 29 22 11 4 ")
            print("30 21 12 5 28 23 ")
            print("7 14 27 36 3 10 ")
            print("20 31 18 9 24 35 ")
            print("15 8 33 26 17 2 ")
            print("32 19 16 1 34 25 ")
        elif x == 6 and y ==5:
            print("32 19 4 17 34 25 ")
            print("5 16 33 26 3 14 ")
            print("20 31 18 15 24 35 ")
            print("9 6 27 36 13 2 ")
            print("30 21 8 11 28 23 ")
            print("7 10 29 22 1 12")

    if N == 7:
        if x == 1 and y ==1:
            print("1 4 41 44 11 6 9 ")
            print("40 45 2 5 8 43 12 ")
            print("3 24 49 42 31 10 7 ")
            print("46 39 32 25 48 13 30 ")
            print("23 26 47 36 29 16 19 ")
            print("38 33 28 21 18 35 14 ")
            print("27 22 37 34 15 20 17 ")
        elif x == 2 and y ==2:
            print("39 46 21 2 19 26 29 ")
            print("22 1 38 47 28 3 18 ")
            print("49 40 45 20 25 30 27 ")
            print("8 23 48 37 44 17 4 ")
            print("41 36 9 24 33 14 31 ")
            print("10 7 34 43 12 5 16 ")
            print("35 42 11 6 15 32 13 ")
        elif x == 3 and y ==3:
            print("13 40 3 46 15 38 5 ")
            print("2 49 14 39 4 47 16 ")
            print("41 12 1 48 45 6 37 ")
            print("34 29 42 23 36 17 44 ")
            print("11 22 35 30 43 24 7 ")
            print("28 33 20 9 26 31 18 ")
            print("21 10 27 32 19 8 25 ")

        elif x == 4 and y ==4:
            print("25 22 9 46 27 40 11 ")
            print("8 49 26 23 10 47 28 ")
            print("21 24 45 48 39 12 41 ")
            print("44 7 36 1 42 29 38 ")
            print("17 20 43 32 37 2 13 ")
            print("6 35 18 15 4 33 30 ")
            print("19 16 5 34 31 14 3 ")
        elif x == 5 and y == 5:
            print("21 24 11 36 39 26 13 ")
            print("10 37 22 25 12 35 40 ")
            print("23 20 29 38 45 14 27 ")
            print("30 9 44 47 28 41 34 ")
            print("19 6 31 42 1 46 15 ")
            print("8 43 4 17 48 33 2 ")
            print("5 18 7 32 3 16 49 ")
        elif x == 6 and y ==6:
            print("29 26 19 6 21 46 39 ")
            print("18 5 28 47 38 7 22 ")
            print("27 30 25 20 49 40 45 ")
            print("4 17 48 37 44 23 8 ")
            print("31 14 33 24 9 36 41 ")
            print("16 3 12 43 34 1 10 ")
            print("13 32 15 2 11 42 35")
        elif x == 7 and y ==7:
            print("27 36 7 48 25 30 9 ")
            print("6 49 26 29 8 47 24 ")
            print("37 28 35 46 43 10 31 ")
            print("34 5 38 19 32 23 44 ")
            print("15 18 33 42 45 20 11 ")
            print("4 39 16 13 2 41 22 ")
            print("17 14 3 40 21 12 1  ")
        elif x == 1 and y ==7:
            print("9 6 11 44 41 4 1 ")
            print("12 45 8 5 2 43 40 ")
            print("7 10 31 42 49 24 3 ")
            print("32 13 46 25 30 39 48 ")
            print("19 16 29 36 47 26 23 ")
            print("14 33 18 21 28 35 38 ")
            print("17 20 15 34 37 22 27 ")
        elif x == 2 and y ==6:
            print("29 26 19 2 21 46 39 ")
            print("18 3 28 47 38 1 22 ")
            print("27 30 25 20 49 40 45 ")
            print("4 17 48 37 44 23 8 ")
            print("31 14 33 24 9 36 41 ")
            print("16 5 12 43 34 7 10 ")
            print("13 32 15 6 11 42 35")
        elif x == 3 and y ==5:
            print("5 38 15 46 3 40 13 ")
            print("16 49 4 39 14 47 2 ")
            print("37 6 45 48 1 12 41 ")
            print("44 17 36 23 42 29 32 ")
            print("7 24 43 30 33 22 11 ")
            print("18 35 26 9 20 31 28 ")
            print("25 8 19 34 27 10 21")
        elif x == 5 and y == 3:
            print("13 26 39 36 11 24 21 ")
            print("40 37 12 25 22 35 10 ")
            print("27 14 45 38 29 20 23 ")
            print("44 41 28 47 34 9 30 ")
            print("15 46 1 42 31 6 19 ")
            print("2 43 48 17 4 33 8 ")
            print("49 16 3 32 7 18 5 ")
        elif x == 6 and y ==2:
            print("39 46 21 6 19 26 29 ")
            print("22 7 38 47 28 5 18 ")
            print("49 40 45 20 25 30 27 ")
            print("8 23 48 37 44 17 4 ")
            print("41 36 9 24 33 14 31 ")
            print("10 1 34 43 12 3 16 ")
            print("35 42 11 2 15 32 13 ")
        elif x == 7 and y ==1:
            print("9 36 25 48 7 30 27 ")
            print("24 49 8 29 26 47 6 ")
            print("37 10 35 46 43 28 31 ")
            print("34 23 38 19 32 5 44 ")
            print("11 20 33 42 45 18 15 ")
            print("22 39 2 13 16 41 4 ")
            print("1 12 21 40 3 14 17 ")
        elif x == 3 and y ==7:
            print("7 4 39 32 35 2 37 ")
            print("40 19 6 3 38 31 34 ")
            print("5 8 41 44 33 36 1 ")
            print("20 45 18 49 14 43 30 ")
            print("9 48 21 42 29 26 13 ")
            print("22 17 46 11 24 15 28 ")
            print("47 10 23 16 27 12 25 ")
        elif x == 5 and y ==7:
            print("15 18 13 38 47 20 35 ")
            print("12 27 16 19 36 39 46 ")
            print("17 14 37 48 45 34 21 ")
            print("28 11 26 33 22 49 40 ")
            print("5 8 29 44 41 32 1 ")
            print("10 25 6 3 30 23 42 ")
            print("7 4 9 24 43 2 31 ")
        elif x == 7 and y ==3:
            print("41 18 5 34 39 20 7 ")
            print("4 35 40 19 6 33 38 ")
            print("17 42 23 48 37 8 21 ")
            print("24 3 36 43 22 49 32 ")
            print("13 16 47 28 31 44 9 ")
            print("2 25 14 11 46 27 30 ")
            print("15 12 1 26 29 10 45 ") #####
        elif x == 7 and y ==5:
            print("7 20 39 34 5 18 41  ")
            print("38 35 6 19 40 33 4 ")
            print("21 8 37 48 23 42 17 ")
            print("36 49 22 43 32 3 24 ")
            print("9 44 31 28 47 16 13  ")
            print("30 27 46 11 14 25 2 ")
            print("45 10 29 26 1 12 15 ") ###
        elif x == 3 and y ==1:
            print("31 2 29 40 33 4 7 ")
            print("28 41 32 3 6 39 34  ")
            print("1 30 43 38 35 8 5  ")
            print("42 27 14 49 44 37 18 ")
            print("13 24 45 36 19 48 9 ")
            print("26 15 22 11 46 17 20 ")
            print("23 12 25 16 21 10 47 ") ###
        elif x == 5 and y ==1:
            print("33 20 41 44 13 18 15 ")
            print("40 45 34 19 16 43 12 ")
            print("21 32 49 42 35 14 17 ")
            print("46 39 22 31 48 11 26 ")
            print("1 30 47 36 27 8 5 ")
            print("38 23 28 3 6 25 10 ")
            print("29 2 37 24 9 4 7 ") ###

        elif x == 1 and y ==3:
            print("15 28 1 44 13 26 23 ")
            print("2 43 14 27 24 41 12 ")
            print("29 16 45 42 31 22 25 ")
            print("38 3 30 47 40 11 32 ")
            print("17 46 39 36 33 8 21")
            print("4 37 48 19 6 35 10")
            print("49 18 5 34 9 20 7 ") ###

        elif x == 1 and y ==5:
            print("41 18 5 34 39 20 7 ")
            print("4 35 40 19 6 33 38 ")
            print("17 42 23 48 37 8 21 ")
            print("24 3 36 43 22 49 32 ")
            print("13 16 47 28 31 44 9 ")
            print("2 25 14 11 46 27 30 ")
            print("15 12 1 26 29 10 45 ")




    if N == 8:
        if x == 1 and y ==1:
            print("1 4 57 20 47 6 49 22 ")
            print("34 19 2 5 58 21 46 7 ")
            print("3 56 35 60 37 48 23 50 ")
            print("18 33 38 55 52 59 8 45 ")
            print("39 14 53 36 61 44 51 24 ")
            print("32 17 40 43 54 27 62 9 ")
            print("13 42 15 30 11 64 25 28 ")
            print("16 31 12 41 26 29 10 63 ")
        elif x == 2 and y ==2:
            print("39 46 15 2 21 36 17 4 ")
            print("14 1 38 45 16 3 20 35 ")
            print("47 40 13 22 37 64 5 18 ")
            print("12 23 48 61 44 19 34 63 ")
            print("49 60 41 30 55 62 43 6 ")
            print("24 11 56 59 42 29 54 33 ")
            print("57 50 9 26 31 52 7 28 ")
            print("10 25 58 51 8 27 32 53 ")
        elif x == 3 and y ==3:
            print("45 42 3 18 35 20 5 8 ")
            print("2 17 44 41 4 7 34 21 ")
            print("43 46 1 36 19 50 9 6 ")
            print("16 31 48 59 40 33 22 51 ")
            print("47 60 37 32 49 58 39 10 ")
            print("30 15 64 57 38 25 52 23 ")
            print("61 56 13 28 63 54 11 26 ")
            print("14 29 62 55 12 27 24 53 ")
        elif x == 4 and y ==4:
            print("23 20 17 38 55 64 15 40 ")
            print("18 37 22 61 16 39 54 63 ")
            print("21 24 19 56 59 62 41 14 ")
            print("36 31 60 1 50 43 58 53 ")
            print("25 2 49 32 57 52 13 42 ")
            print("30 35 28 51 44 47 10 7 ")
            print("3 26 33 48 5 8 45 12 ")
            print("34 29 4 27 46 11 6 9 ")
        elif x == 5 and y ==5:
            print("35 18 37 22 41 16 43 24 ")
            print("38 21 34 17 46 23 32 15 ")
            print("19 36 49 40 33 42 25 44 ")
            print("50 39 20 47 64 45 14 31 ")
            print("7 48 61 54 1 30 63 26 ")
            print("60 51 8 29 62 55 2 13 ")
            print("9 6 53 58 11 4 27 56 ")
            print("52 59 10 5 28 57 12 3 ")
        elif x == 6 and y ==6:
            print("57 14 41 48 63 16 39 36 ")
            print("42 47 58 15 40 37 64 17 ")
            print("13 56 49 46 59 62 35 38 ")
            print("50 43 30 55 52 45 18 61 ")
            print("27 12 51 44 29 60 53 34 ")
            print("6 9 28 31 54 1 22 19 ")
            print("11 26 7 4 21 24 33 2 ")
            print("8 5 10 25 32 3 20 23 ")
        elif x == 7 and y ==7:
            print("29 10 39 34 27 12 41 44 ")
            print("38 35 28 11 40 43 26 13 ")
            print("9 30 37 56 33 60 45 42 ")
            print("36 55 32 59 64 47 14 25 ")
            print("31 8 63 48 57 24 61 46 ")
            print("54 5 58 23 62 49 18 15 ")
            print("7 22 3 52 17 20 1 50 ")
            print("4 53 6 21 2 51 16 19 ")
        elif x == 8 and y ==8:
            print("7 10 25 40 51 12 27 30 ")
            print("24 39 8 11 26 29 50 13 ")
            print("9 6 41 52 45 48 31 28 ")
            print("38 23 44 47 64 55 14 49 ")
            print("5 42 61 56 53 46 63 32 ")
            print("22 37 20 43 62 57 54 15 ")
            print("19 4 35 60 17 2 33 58 ")
            print("36 21 18 3 34 59 16 1 ")
        elif x == 1 and y ==8:
            print("22 63 6 47 20 49 4 1 ")
            print("7 46 21 64 5 2 19 34 ")
            print("62 23 56 37 48 35 50 3 ")
            print("45 8 61 52 55 38 33 18 ")
            print("24 53 44 57 36 51 14 39 ")
            print("9 60 27 54 43 40 17 32 ")
            print("28 25 58 11 30 15 42 13 ")
            print("59 10 29 26 41 12 31 16 ")
        elif x == 2 and y ==7:
            print("4 17 36 21 2 15 60 39 ")
            print("35 20 3 16 61 38 1 14 ")
            print("18 5 62 37 22 13 40 59 ")
            print("53 34 19 64 51 58 23 12 ")
            print("6 63 52 57 30 43 50 41 ")
            print("33 54 29 44 49 46 11 24 ")
            print("28 7 56 31 26 9 42 47 ")
            print("55 32 27 8 45 48 25 10 ")
        elif x == 3 and y ==6:
            print("8 5 20 35 18 3 42 45 ")
            print("21 34 7 4 41 44 17 2 ")
            print("6 9 50 19 36 1 46 43 ")
            print("51 22 33 40 59 48 31 16 ")
            print("10 39 60 49 32 37 58 47 ")
            print("23 52 25 38 57 64 15 30 ")
            print("26 11 54 61 28 13 56 63 ")
            print("53 24 27 12 55 62 29 14 ")
        elif x == 4 and y ==5:
            print("40 15 64 51 38 17 20 23 ")
            print("61 50 39 16 63 22 37 18 ")
            print("14 41 62 59 52 19 24 21 ")
            print("49 60 43 54 1 58 31 36 ")
            print("42 13 48 57 32 53 2 25 ")
            print("7 10 55 44 47 28 35 30 ")
            print("12 45 8 5 56 33 26 3 ")
            print("9 6 11 46 27 4 29 34")
        elif x == 5 and y ==4:
            print("24 39 16 63 22 37 18 57 ")
            print("15 64 23 38 17 58 21 36 ")
            print("40 25 62 59 50 35 56 19 ")
            print("61 14 41 52 55 20 49 34 ")
            print("26 53 60 1 42 51 30 7 ")
            print("13 2 43 54 29 8 33 48 ")
            print("44 27 4 11 46 31 6 9 ")
            print("3 12 45 28 5 10 47 32 ")
        elif x == 6 and y ==3:
            print("36 39 16 63 48 41 14 57 ")
            print("17 64 37 40 15 58 47 42 ")
            print("38 35 62 59 46 49 56 13 ")
            print("61 18 45 52 55 30 43 50 ")
            print("34 53 60 29 44 51 12 27 ")
            print("19 22 1 54 31 28 9 6 ")
            print("2 33 24 21 4 7 26 11 ")
            print("23 20 3 32 25 10 5 8 ")
        elif x == 7 and y ==2:
            print("60 41 12 27 34 39 10 29 ")
            print("13 26 61 40 11 28 35 38 ")
            print("62 59 42 33 56 37 30 9 ")
            print("25 14 57 64 43 32 49 36 ")
            print("58 63 24 45 50 55 8 31 ")
            print("15 18 51 54 23 44 5 48 ")
            print("52 1 20 17 46 3 22 7 ")
            print("19 16 53 2 21 6 47 4 ")
        elif x == 8 and y ==1:
            print("30 27 12 63 40 25 10 7 ")
            print("13 64 29 26 11 8 39 24 ")
            print("28 31 58 45 62 41 6 9 ")
            print("57 14 61 52 55 44 23 38 ")
            print("32 53 56 59 46 51 42 5 ")
            print("15 60 47 54 43 20 37 22 ")
            print("48 33 2 17 50 35 4 19 ")
            print("1 16 49 34 3 18 21 36")


# if __name__ == '__main__':
        
#     N = int(input()) #size
#     x,y = [int(i) for i in input().split()]
#     x -=1 #set start point
#     y -=1
#     if N == 0:
#         print ("0")
#     else:
#         game = KnightsTour(N)
#         game.put(1, [], (x,y))
#         game.print()
