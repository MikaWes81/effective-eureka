import os
clear = lambda: os.system('clear')
clear()

class bcolors:
    blue = '\33[34m'
    end = '\033[0m'

placed_blue = 0
placed_red = 0


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


#def set_player_blue






# 0 not correct

def blue_check():

    for i in range(2,6):
        if i == 2:
            placed_blue = placed_blue + 1
        elif i == 3:
            placed_blue = placed_blue + 1
        elif i == 4:
            placed_blue = placed_blue + 1
        elif i == 5:
            placed_blue = placed_blue + 1
    return




def boot_blue():
    print("Startposition:\n")
    cordinats = input()
    clear()
    print("Endpunkt")
    cordinats2 = input()
    cord = cordinats.split(",")
    cord2= cordinats2.split(",")
    if cordinats2 or cordinats == "":
        print("prese Enter un fortzufahren")
        print("ungültige eingabe")
        return
    else:
        if int(cord[0]) - int(cord2[0]) == 0 and int(cord[1]) - int(cord2[1]) !=0:
            ent = abs(int(cord[1]) - int(cord2[1]))
        elif int(cord2[1]) - int(cord[1]) == 0 and int(cord2[0]) - int(cord[0]) !=0:
            ent =abs(int(cord[0]) - int(cord2[0]))
        else:
            print("prese Enter un fortzufahren")
            print("ungültige eingabe")
            return



def setup_board_blue():
    print(bcolors.blau + "Blau" + bcolors.end )
    print("Prese enter um fortzufahren")
    input()
    clear()

    if placed_blue == 14:
        return 0
    else:
        boot_blue()





def info():
    print("die eingaben werden über Kordinaten gemacht")
    print("sie werden x,y geschrieben")
    print("x ist die Horizontale cordinate")
    print("y ist die Verticale cordinate")
    print("presse Enter um fortzufahren")
    input()
    clear()
    print("wärend der phase wo die schiffen gesetzt werden")
    print("darf nur der aktive spieler das gerät und den bildschirm benutzen")
    print("presse Enter um fortzufahren")
    input()
    clear()
    print("für das plazieren der schiffe")
    print("gibst du zuerst den Punkt ein wo das boot begint")
    print("danach gibst du die kordinaten wo das boot endet ein")
    print("presse enter um fortzufahren")
    input()
    clear()
    return



#def setup():
#    for rang in range(100):
#        player_red[rang]         = 0
#        player_blue[rang]        = 0
#        player_input_blue[rang]  = 0
#        player_input_red[rang]   = 0
#    return




#def main():
#    setup()
#    info()
#    setup_board()
#    play()

#*/