import os

clear = lambda: os.system('clear')
clear()


class bcolors:
    blue = '\33[34m'
    end = '\033[0m'


placed_blue = 0
placed_red = 0

#                     +1  +2  +3  +4  +5  +6  +7  +8  +9  +10
player_input_blue = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +0
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +10
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +20
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +30
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +40
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +50
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +60
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +70
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",  # +80
                     "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ]  # +90

player_blue = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ]

player_input_red = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ]

player_red = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", ]


def print_board_red():
    line = 0

    höhe = 1
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        print(str(höhe) + " " + player_red[line] + " " + player_red[line + 1] + " " + player_red[line + 2] + " " +
              player_red[line + 3] + " " + player_red[line + 4] + " " + player_red[line + 5] + " " + player_red[
                  line + 6] + " " + player_red[line + 7] + " " + player_red[line + 8] + " " + player_red[line + 9])
        höhe += 1
        line += 10


def print_bord_blue():
    line = 0

    höhe = 1
    print("   1 2 3 4 5 6 7 8 9 10")
    for i in range(9):
        print(str(höhe) + "  " + player_blue[line] + " " + player_blue[line + 1] + " " + player_blue[line + 2] + " " +
              player_blue[line + 3] + " " + player_blue[line + 4] + " " + player_blue[line + 5] + " " + player_blue[
                  line + 6] + " " + player_blue[line + 7] + " " + player_blue[line + 8] + " " + player_blue[line + 9])
        höhe += 1
        line += 10
    print(str(höhe) + " " + player_blue[line] + " " + player_blue[line + 1] + " " + player_blue[line + 2] + " " +
          player_blue[line + 3] + " " + player_blue[line + 4] + " " + player_blue[line + 5] + " " + player_blue[
              line + 6] + " " + player_blue[line + 7] + " " + player_blue[line + 8] + " " + player_blue[line + 9])


# def set_player_blue


# 0 not correct


def boot_blue():
    global placed_blue
    global player_blue
    print("Startposition:\n")
    cordinats = input()
    clear()
    print("Endpunkt")
    cordinats2 = input()
    cord = cordinats.split(",")
    cord2 = cordinats2.split(",")

    if int(cord[0]) - int(cord2[0]) == 0 and int(cord[1]) - int(cord2[1]) != 0:
        ent = abs(int(cord[1]) + int(cord2[1]))
        if cord[1] > cord2[1]:
            punkt = int(cord2[1]) * 10 - 10
        elif cord2[1] > cord[1]:
            punkt = int(cord[1]) * 10 - 10
        if ent > 5:
            print("prese Enter un fortzufahren")
            print("ungültige eingabe")
            return
        elif ent < 2:
            print("prese Enter un fortzufahren")
            print("ungültige eingabe")
            return
        elif ent == 2:
            placed_blue = placed_blue + 1
            for _ in range(1):
                punkt += 1
                player_blue[punkt + int(cord[0]) - 2] = "*"
        elif ent == 3:
            placed_blue = placed_blue + 1
            for _ in range(2):
                punkt += 1
                player_blue[punkt + int(cord[0]) - 2] = "*"
        elif ent == 4:
            placed_blue = placed_blue + 1
            for _ in range(3):
                punkt += 1
                player_blue[punkt + int(cord[0]) - 2] = "*"
        elif ent == 5:
            for _ in range(4):
                punkt += 1
                player_blue[punkt + int(cord[0]) - 2] = "*"
    elif int(cord2[1]) - int(cord[1]) == 0 and int(cord2[0]) - int(cord[0]) != 0:
        ent = abs(int(cord[0]) + int(cord2[0]))
        if cord[0] > cord2[0]:
            punkt = int(cord2[0])
            punkt += -2
        elif cord2[0] > cord[0]:
            punkt = int(cord[0])
            punkt += -2
        if ent > 5:
            print("prese Enter un fortzufahren")
            print("ungültige eingabe")
            return
        elif ent < 2:
            print("prese Enter un fortzufahren")
            print("ungültige eingabe")
            return
        elif ent == 2:
            placed_blue = placed_blue + 1
            for _ in range(1):
                punkt += 1
                player_blue[punkt + int(cord[1]) * 10 - 10] = "*"
        elif ent == 3:
            placed_blue = placed_blue + 1
            for _ in range(2):
                punkt += 1
                player_blue[punkt + int(cord[1]) * 10 - 10] = "*"
        elif ent == 4:
            placed_blue = placed_blue + 1
            for _ in range(3):
                punkt += 1
                player_blue[punkt + int(cord[1]) * 10 - 10] = "*"
        elif ent == 5:
            for _ in range(4):
                punkt += 1
                player_blue[punkt + int(cord[1]) * 10 - 10] = "*"

    print_bord_blue()
    boot_blue()


boot_blue()


def setup_board_blue():
    print(bcolors.blau + "Blau" + bcolors.end)
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

# def setup():
#    for rang in range(100):
#        player_red[rang]         = 0
#        player_blue[rang]        = 0
#        player_input_blue[rang]  = 0
#        player_input_red[rang]   = 0
#    return


# def main():
#    setup()
#    info()
#    setup_board()
#    play()

# */