




player_input_blue  = ["0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",]
    
player_blue =        ["0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",
                      "0","0","0","0","0","0","0","0","0","0",]
    
    
player_input_red  = ["0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",
                     "0","0","0","0","0","0","0","0","0","0",]

player_red     =  ["0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",
                   "0","0","0","0","0","0","0","0","0","0",]

def print_board_player_red():
    number = 1
    print("    1 2 3 4 5 6 7 8 9 10")
    print("")
    print("1",end="   ")
    line = 2
    for x in range(10):
        for y in range(10):
            z = y + x - 2
            if(number == 10):
                print(player_red[z])
                number = 1
                if (line == 10):
                    print(line, end="  ")
                    line = line + 1

                if (line != 11):
                    print(line, end="   ")
                    line = line + 1

            else:
                print(player_red[z],end=" ")
                number = number + 1
            
def print_board_player_blue():
    number = 1
    print("    1 2 3 4 5 6 7 8 9 10")
    print("")
    print("1",end="   ")
    line = 2
    for x in range(10):
        for y in range(10):
            z = y + x - 2
            if(number == 10):
                print(player_blue[z])
                number = 1
                if (line == 10):
                    print(line, end="  ")
                    line = line + 1

                if (line != 11):
                    print(line, end="   ")
                    line = line + 1

            else:
                print(player_blue[z],end=" ")
                number = number + 1

def print_board_player_blue_input():
    number = 1
    print("    1 2 3 4 5 6 7 8 9 10")
    print("")
    print("1",end="   ")
    line = 2
    for x in range(10):
        for y in range(10):
            z = y + x - 2
            if(number == 10):
                print(player_input_blue[z])
                number = 1
                if (line == 10):
                    print(line, end="  ")
                    line = line + 1

                if (line != 11):
                    print(line, end="   ")
                    line = line + 1

            else:
                print(player_input_blue[z],end=" ")
                number = number + 1
def print_board_player_red_input():
    number = 1
    print("    1 2 3 4 5 6 7 8 9 10")
    print("")
    print("1",end="   ")
    line = 2
    for x in range(10):
        for y in range(10):
            z = y + x - 2
            if(number == 10):
                print(player_input_red[z])
                number = 1
                if (line == 10):
                    print(line, end="  ")
                    line = line + 1

                if (line != 11):
                    print(line, end="   ")
                    line = line + 1

            else:
                print(player_input_red[z],end=" ")
                number = number + 1


#def setup_board():
    





def setup():
    for rang in range(100):
        player_red[rang]         = 0
        player_blue[rang]        = 0
        player_input_blue[rang]  = 0
        player_input_red[rang]   = 0
    return




def main():
    setup()
    setup_board()
    #play()

print_board()