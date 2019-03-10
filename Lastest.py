import random


visible_bot_grid = []
bot_grid = []
visible_player_grid = []
player_grid = []
ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", ""]
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", ""]
killed = 1
ship_quantity = 0
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

prev_a = 1
prev_b = 0
prev_shot_hited = 0
finding_part_of_ship = 0
ship_offset = 0

def add_bot_ship(c):
    if c == 1:
        b1 = 1
        while b1 == 1:
            x1 = random.randint(1, 10)
            y1 = random.randint(0, 9)
            if bot_grid[y1][x1] == "[ ]":
                b1 = 0
        if x1 == 1 and y1 == 0:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1 - 1][x1 + 1] = "[R]"
        elif x1 == 1 and y1 == 9:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1 - 1][x1 + 1] = "[R]"
        elif x1 == 10 and y1 == 0:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 - 1] = "[R]"
        elif x1 == 10 and y1 == 9:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1 - 1][x1 - 1] = "[R]"
        elif x1 == 10:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1 + 1][x1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 - 1] = "[R]"
            bot_grid[y1 + 1][x1 - 1] = "[R]"
        elif y1 == 9:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 + 1] = "[R]"
        elif x1 == 1:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1 - 1][x1 + 1] = "[R]"
        elif y1 == 0:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1] = "[R]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 + 1][x1 - 1] = "[R]"
        else:
            bot_grid[y1][x1] = "[B]"
            bot_grid[y1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1 + 1] = "[R]"
            bot_grid[y1 + 1][x1] = "[R]"
            bot_grid[y1 - 1][x1] = "[R]"
            bot_grid[y1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 - 1] = "[R]"
            bot_grid[y1 + 1][x1 - 1] = "[R]"
            bot_grid[y1 - 1][x1 + 1] = "[R]"
    elif c == 2:
        b2 = 1
        while b2 == 1:
            x21 = random.randint(1, 10)
            y21 = random.randint(1, 9)
            z21 = random.randint(1, 2)
            z22 = random.randint(1, 3)
            z23 = random.randint(1, 4)
            if x21 == 1 and y21 == 0:
                if z21 == 1:
                    y22 = y21 + 1
                    x22 = x21
                else:
                    y22 = y21
                    x22 = x21 + 1
            elif x21 == 10 and y21 == 9:
                if z21 == 1:
                    y22 = y21 - 1
                    x22 = x21
                else:
                    y22 = y21
                    x22 = x21 - 1
            elif y21 == 0:
                if z22 == 1:
                    y22 = y21 + 1
                    x22 = x21
                elif z22 == 2:
                    y22 = y21
                    x22 = x21 - 1
                elif z22 == 3:
                    y22 = y21
                    x22 = x21 + 1
            elif x21 == 1:
                if z22 == 1:
                    y22 = y21
                    x22 = x21 + 1
                elif z22 == 2:
                    y22 = y21 - 1
                    x22 = x21
                elif z22 == 3:
                    y22 = y21 + 1
                    x22 = x21
            elif x21 == 10:
                if z22 == 1:
                    y22 = y21
                    x22 = x21 - 1
                elif z22 == 2:
                    y22 = y21 + 1
                    x22 = x21
                elif z22 == 3:
                    y22 = y21 - 1
                    x22 = x21
            elif y21 == 9:
                if z22 == 1:
                    y22 = y21 - 1
                    x22 = x21
                elif z22 == 2:
                    y22 = y21
                    x22 = x21 + 1
                elif z22 == 3:
                    y22 = y21
                    x22 = x21 - 1
            else:
                if z23 == 1:
                    y22 = y21 - 1
                    x22 = x21
                elif z23 == 2:
                    y22 = y21
                    x22 = x21 - 1
                elif z23 == 3:
                    y22 = y21
                    x22 = x21 + 1
                elif z23 == 4:
                    y22 = y21 + 1
                    x22 = x21
            try:
                if bot_grid[y21][x21] == "[ ]" and bot_grid[y22][x22] == "[ ]":
                    b2 = 0
            except IndexError:
                b2 = 1
        try:
            if bot_grid[y21 + 1][x21] == "[ ]":
                bot_grid[y21 + 1][x21] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21][x21 + 1] == "[ ]":
                bot_grid[y21][x21 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21 + 1][x21 + 1] == "[ ]":
                bot_grid[y21 + 1][x21 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21 - 1][x21] == "[ ]":
                bot_grid[y21 - 1][x21] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21][x21 - 1] == "[ ]":
                bot_grid[y21][x21 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21 - 1][x21 - 1] == "[ ]":
                bot_grid[y21 - 1][x21 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21 - 1][x21 + 1] == "[ ]":
                bot_grid[y21 - 1][x21 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y21 + 1][x21 - 1] == "[ ]":
                bot_grid[y21 + 1][x21 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 + 1][x22] == "[ ]":
                bot_grid[y22 + 1][x22] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22][x22 + 1] == "[ ]":
                bot_grid[y22][x22 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 + 1][x22 + 1] == "[ ]":
                bot_grid[y22 + 1][x22 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 - 1][x22] == "[ ]":
                bot_grid[y22 - 1][x22] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22][x22 - 1] == "[ ]":
                bot_grid[y22][x22 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 - 1][x22 - 1] == "[ ]":
                bot_grid[y22 - 1][x22 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 - 1][x22 + 1] == "[ ]":
                bot_grid[y22 - 1][x22 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y22 + 1][x22 - 1] == "[ ]":
                bot_grid[y22 + 1][x22 - 1] = "[R]"
        except IndexError:
            k = 0
        bot_grid[y21][x21] = "[B]"
        bot_grid[y22][x22] = "[B]"
    elif c == 3:
        b3 = 1
        while b3 == 1:
            x31 = random.randint(1, 10)
            y31 = random.randint(1, 9)
            z31 = random.randint(1, 2)
            z32 = random.randint(1, 3)
            z33 = random.randint(1, 4)
            if x31 == 1 and y31 == 0 or x31 <= 3 and y31 <= 2:
                if z31 == 1:
                    y32 = y31 + 1
                    x32 = x31
                    y33 = y32 + 1
                    x33 = x32
                elif z31 == 2:
                    y32 = y31
                    x32 = x31 + 1
                    y33 = y32
                    x33 = x32 + 1
            elif x31 == 10 and y31 == 9 or x31 >= 8 and y31 >= 7:
                if z31 == 1:
                    y32 = y31 - 1
                    x32 = x31
                    y33 = y32 - 1
                    x33 = x32
                elif z31 == 2:
                    y32 = y31
                    x32 = x31 - 1
                    y33 = y32
                    x33 = x32 - 1
            elif y31 <= 2:
                if z32 == 1:
                    y32 = y31 + 1
                    x32 = x31
                    y33 = y32 + 1
                    x33 = x32
                elif z32 == 2:
                    y32 = y31
                    x32 = x31 + 1
                    y33 = y32
                    x33 = x32 + 1
                elif z32 == 3:
                    y32 = y31
                    x32 = x31 - 1
                    y33 = y32
                    x33 = x32 - 1
            elif x31 <= 3:
                if z32 == 1:
                    y32 = y31
                    x32 = x31 + 1
                    y33 = y32
                    x33 = x32 + 1
                elif z32 == 2:
                    y32 = y31 + 1
                    x32 = x31
                    y33 = y32 + 1
                    x33 = x32
                elif z32 == 3:
                    y32 = y31 - 1
                    x32 = x31
                    y33 = y32 - 1
                    x33 = x32
            elif x31 >= 8:
                if z32 == 1:
                    y32 = y31
                    x32 = x31 - 1
                    y33 = y32
                    x33 = x32 - 1
                elif z32 == 2:
                    y32 = y31 + 1
                    x32 = x31
                    y33 = y32 + 1
                    x33 = x32
                elif z32 == 3:
                    y32 = y31 - 1
                    x32 = x31
                    y33 = y32 - 1
                    x33 = x32
            elif y31 >= 7:
                if z32 == 1:
                    y32 = y31 - 1
                    x32 = x31
                    y33 = y32 - 1
                    x33 = x32
                elif z32 == 2:
                    y32 = y31
                    x32 = x31 + 1
                    y33 = y32
                    x33 = x32 + 1
                elif z32 == 3:
                    y32 = y31
                    x32 = x31 - 1
                    y33 = y32
                    x33 = x32 - 1
            else:
                if z33 == 1:
                    y32 = y31 - 1
                    x32 = x31
                    y33 = y32 - 1
                    x33 = x32
                elif z33 == 2:
                    y32 = y31
                    x32 = x31 - 1
                    y33 = y32
                    x33 = x32 - 1
                elif z33 == 3:
                    y32 = y31
                    x32 = x31 + 1
                    y33 = y32
                    x33 = x32 + 1
                elif z33 == 4:
                    y32 = y31 + 1
                    x32 = x31
                    y33 = y32 + 1
                    x33 = x32

            try:
                if bot_grid[y31][x31] == "[ ]" and bot_grid[y32][x32] == "[ ]" and bot_grid[y33][x33] == "[ ]":
                    b3 = 0
            except IndexError:
                b3 = 1
        try:
            if bot_grid[y31 + 1][x31] == "[ ]":
                bot_grid[y31 + 1][x31] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31][x31 + 1] == "[ ]":
                bot_grid[y31][x31 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31 + 1][x31 + 1] == "[ ]":
                bot_grid[y31 + 1][x31 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31 - 1][x31] == "[ ]":
                bot_grid[y31 - 1][x31] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31][x31 - 1] == "[ ]":
                bot_grid[y31][x31 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31 - 1][x31 - 1] == "[ ]":
                bot_grid[y31 - 1][x31 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31 - 1][x31 + 1] == "[ ]":
                bot_grid[y31 - 1][x31 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y31 + 1][x31 - 1] == "[ ]":
                bot_grid[y31 + 1][x31 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 + 1][x32] == "[ ]":
                bot_grid[y32 + 1][x32] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32][x32 + 1] == "[ ]":
                bot_grid[y32][x32 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 + 1][x32 + 1] == "[ ]":
                bot_grid[y32 + 1][x32 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 - 1][x32] == "[ ]":
                bot_grid[y32 - 1][x32] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32][x32 - 1] == "[ ]":
                bot_grid[y32][x32 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 - 1][x32 - 1] == "[ ]":
                bot_grid[y32 - 1][x32 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 - 1][x32 + 1] == "[ ]":
                bot_grid[y32 - 1][x32 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y32 + 1][x32 - 1] == "[ ]":
                bot_grid[y32 + 1][x32 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 + 1][x33] == "[ ]":
                bot_grid[y33 + 1][x33] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33][x33 + 1] == "[ ]":
                bot_grid[y33][x33 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 + 1][x33 + 1] == "[ ]":
                bot_grid[y33 + 1][x33 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 - 1][x33] == "[ ]":
                bot_grid[y33 - 1][x33] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33][x33 - 1] == "[ ]":
                bot_grid[y33][x33 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 - 1][x33 - 1] == "[ ]":
                bot_grid[y33 - 1][x33 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 - 1][x33 + 1] == "[ ]":
                bot_grid[y33 - 1][x33 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y33 + 1][x33 - 1] == "[ ]":
                bot_grid[y33 + 1][x33 - 1] = "[R]"
        except IndexError:
            k = 0
        bot_grid[y31][x31] = "[B]"
        bot_grid[y32][x32] = "[B]"
        bot_grid[y33][x33] = "[B]"
    elif c == 4:
        b4 = 1
        while b4 == 1:
            x41 = random.randint(1, 10)
            y41 = random.randint(1, 9)
            z41 = random.randint(1, 2)
            z42 = random.randint(1, 3)
            z43 = random.randint(1, 4)
            if x41 == 1 and y41 == 0 or x41 <= 4 and y41 <= 3:
                if z41 == 1:
                    y42 = y41 + 1
                    x42 = x41
                    y43 = y42 + 1
                    x43 = x42
                    y44 = y43 + 1
                    x44 = x43
                elif z41 == 2:
                    y42 = y41
                    x42 = x41 + 1
                    y43 = y42
                    x43 = x42 + 1
                    y44 = y43
                    x44 = x43 + 1
            elif x41 == 10 and y41 == 9 or x41 >= 7 and y41 >= 6:
                if z41 == 1:
                    y42 = y41 - 1
                    x42 = x41
                    y43 = y42 - 1
                    x43 = x42
                    y44 = y43 - 1
                    x44 = x43
                elif z41 == 2:
                    y42 = y41
                    x42 = x41 - 1
                    y43 = y42
                    x43 = x42 - 1
                    y44 = y43
                    x44 = x43 - 1
            elif y41 <= 3:
                if z42 == 1:
                    y42 = y41 + 1
                    x42 = x41
                    y43 = y42 + 1
                    x43 = x42
                    y44 = y43 + 1
                    x44 = x43
                elif z42 == 2:
                    y42 = y41
                    x42 = x41 + 1
                    y43 = y42
                    x43 = x42 + 1
                    y44 = y43
                    x44 = x43 + 1
                elif z42 == 3:
                    y42 = y41
                    x42 = x41 - 1
                    y43 = y42
                    x43 = x42 - 1
                    y44 = y43
                    x44 = x43 - 1
            elif x41 <= 4:
                if z42 == 1:
                    y42 = y41
                    x42 = x41 + 1
                    y43 = y42
                    x43 = x42 + 1
                    y44 = y43
                    x44 = x43 + 1
                elif z42 == 2:
                    y42 = y41 + 1
                    x42 = x41
                    y43 = y42 + 1
                    x43 = x42
                    y44 = y43 + 1
                    x44 = x43
                elif z42 == 3:
                    y42 = y41 - 1
                    x42 = x41
                    y43 = y42 - 1
                    x43 = x42
                    y44 = y43 - 1
                    x44 = x43
            elif x41 >= 7:
                if z42 == 1:
                    y42 = y41
                    x42 = x41 - 1
                    y43 = y42
                    x43 = x42 - 1
                    y44 = y43
                    x44 = x43 - 1
                elif z42 == 2:
                    y42 = y41 + 1
                    x42 = x41
                    y43 = y42 + 1
                    x43 = x42
                    y44 = y43 + 1
                    x44 = x43
                elif z42 == 3:
                    y42 = y41 - 1
                    x42 = x41
                    y43 = y42 - 1
                    x43 = x42
                    y44 = y43 - 1
                    x44 = x43
            elif y41 >= 6:
                if z42 == 1:
                    y42 = y41 - 1
                    x42 = x41
                    y43 = y42 - 1
                    x43 = x42
                    y44 = y43 - 1
                    x44 = x43
                elif z42 == 2:
                    y42 = y41
                    x42 = x41 + 1
                    y43 = y42
                    x43 = x42 + 1
                    y44 = y43
                    x44 = x43 + 1
                elif z42 == 3:
                    y42 = y41
                    x42 = x41 - 1
                    y43 = y42
                    x43 = x42 - 1
                    y44 = y43
                    x44 = x43 - 1
            else:
                if z43 == 1:
                    y42 = y41 + 1
                    x42 = x41
                    y43 = y42 + 1
                    x43 = x42
                    y44 = y43 + 1
                    x44 = x43
                elif z43 == 2:
                    y42 = y41 - 1
                    x42 = x41
                    y43 = y42 - 1
                    x43 = x42
                    y44 = y43 - 1
                    x44 = x43
                elif z43 == 3:
                    y42 = y41
                    x42 = x41 + 1
                    y43 = y42
                    x43 = x42 + 1
                    y44 = y43
                    x44 = x43 + 1
                elif z43 == 4:
                    y42 = y41
                    x42 = x41 - 1
                    y43 = y42
                    x43 = x42 - 1
                    y44 = y43
                    x44 = x43 - 1
            try:
                if bot_grid[y41][x41] == "[ ]" \
                        and bot_grid[y42][x42] == "[ ]" \
                        and bot_grid[y43][x43] == "[ ]" \
                        and bot_grid[y44][x44] == "[ ]":
                    b4 = 0
            except IndexError:
                b4 = 1
        try:
            if bot_grid[y41 + 1][x41] == "[ ]":
                bot_grid[y41 + 1][x41] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41][x41 + 1] == "[ ]":
                bot_grid[y41][x41 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41 + 1][x41 + 1] == "[ ]":
                bot_grid[y41 + 1][x41 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41 - 1][x41] == "[ ]":
                bot_grid[y41 - 1][x41] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41][x41 - 1] == "[ ]":
                bot_grid[y41][x41 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41 - 1][x41 - 1] == "[ ]":
                bot_grid[y41 - 1][x41 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41 - 1][x41 + 1] == "[ ]":
                bot_grid[y41 - 1][x41 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y41 + 1][x41 - 1] == "[ ]":
                bot_grid[y41 + 1][x41 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 + 1][x42] == "[ ]":
                bot_grid[y42 + 1][x42] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42][x42 + 1] == "[ ]":
                bot_grid[y42][x42 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 + 1][x42 + 1] == "[ ]":
                bot_grid[y42 + 1][x42 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 - 1][x42] == "[ ]":
                bot_grid[y42 - 1][x42] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42][x42 - 1] == "[ ]":
                bot_grid[y42][x42 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 - 1][x42 - 1] == "[ ]":
                bot_grid[y42 - 1][x42 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 - 1][x42 + 1] == "[ ]":
                bot_grid[y42 - 1][x42 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y42 + 1][x42 - 1] == "[ ]":
                bot_grid[y42 + 1][x42 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 + 1][x43] == "[ ]":
                bot_grid[y43 + 1][x43] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43][x43 + 1] == "[ ]":
                bot_grid[y43][x43 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 + 1][x43 + 1] == "[ ]":
                bot_grid[y43 + 1][x43 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 - 1][x43] == "[ ]":
                bot_grid[y43 - 1][x43] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43][x43 - 1] == "[ ]":
                bot_grid[y43][x43 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 - 1][x43 - 1] == "[ ]":
                bot_grid[y43 - 1][x43 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 - 1][x43 + 1] == "[ ]":
                bot_grid[y43 - 1][x43 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y43 + 1][x43 - 1] == "[ ]":
                bot_grid[y43 + 1][x43 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 + 1][x44] == "[ ]":
                bot_grid[y44 + 1][x44] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44][x44 + 1] == "[ ]":
                bot_grid[y44][x44 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 + 1][x44 + 1] == "[ ]":
                bot_grid[y44 + 1][x44 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 - 1][x44] == "[ ]":
                bot_grid[y44 - 1][x44] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44][x44 - 1] == "[ ]":
                bot_grid[y44][x44 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 - 1][x44 - 1] == "[ ]":
                bot_grid[y44 - 1][x44 - 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 - 1][x44 + 1] == "[ ]":
                bot_grid[y44 - 1][x44 + 1] = "[R]"
        except IndexError:
            k = 0
        try:
            if bot_grid[y44 + 1][x44 - 1] == "[ ]":
                bot_grid[y44 + 1][x44 - 1] = "[R]"
        except IndexError:
            k = 0
        bot_grid[y41][x41] = "[B]"
        bot_grid[y42][x42] = "[B]"
        bot_grid[y43][x43] = "[B]"
        bot_grid[y44][x44] = "[B]"


def shot(a, b):
    kill = 0
    ships_near_shot = 0
    if bot_grid[a][b] == "[B]":
        try:
            if bot_grid[a + 1][b] == "[B]":
                ships_near_shot += 1
        except IndexError:
            k = 0
        try:
            if bot_grid[a - 1][b] == "[B]":
                ships_near_shot += 1
        except IndexError:
            k = 0
        try:
            if bot_grid[a][b + 1] == "[B]":
                ships_near_shot += 1
        except IndexError:
            k = 0
        try:
            if bot_grid[a][b - 1] == "[B]":
                ships_near_shot += 1
        except IndexError:
            k = 0
        if ships_near_shot == 1:
            try:
                if bot_grid[a][b - 1] == "[B]" and bot_grid[a][b - 2] == "[B]" and bot_grid[a][b - 3] == "[B]":
                    if visible_bot_grid[a][b - 1] == "[X]" and visible_bot_grid[a][b - 2] == "[X]" and visible_bot_grid[a][b - 3] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 2] == "[R]" and visible_bot_grid[a + 1][b - 2] == "[ ]":
                                visible_bot_grid[a + 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 2] == "[R]" and visible_bot_grid[a - 1][b - 2] == "[ ]":
                                visible_bot_grid[a - 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 3] == "[R]" and visible_bot_grid[a + 1][b - 3] == "[ ]":
                                visible_bot_grid[a + 1][b - 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 3] == "[R]" and visible_bot_grid[a - 1][b - 3] == "[ ]":
                                visible_bot_grid[a - 1][b - 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 4] == "[R]" and visible_bot_grid[a][b - 4] == "[ ]":
                                visible_bot_grid[a][b - 4] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 4] == "[R]" and visible_bot_grid[a + 1][b - 4] == "[ ]":
                                visible_bot_grid[a + 1][b - 4] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 4] == "[R]" and visible_bot_grid[a - 1][b - 4] == "[ ]":
                                visible_bot_grid[a - 1][b - 4] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b - 1] == "[B]" and bot_grid[a][b - 2] == "[B]" and bot_grid[a][b - 3] != "[B]":
                    if visible_bot_grid[a][b - 1] == "[X]" and visible_bot_grid[a][b - 2] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 2] == "[R]" and visible_bot_grid[a + 1][b - 2] == "[ ]":
                               visible_bot_grid[a + 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 2] == "[R]" and visible_bot_grid[a - 1][b - 2] == "[ ]":
                                visible_bot_grid[a - 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 3] == "[R]" and visible_bot_grid[a][b - 3] == "[ ]":
                                visible_bot_grid[a][b - 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 3] == "[R]" and visible_bot_grid[a + 1][b - 3] == "[ ]":
                                visible_bot_grid[a + 1][b - 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 3] == "[R]" and visible_bot_grid[a - 1][b - 3] == "[ ]":
                                visible_bot_grid[a - 1][b - 3] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b - 1] == "[B]" and bot_grid[a][b - 2] != "[B]":
                    if visible_bot_grid[a][b - 1] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 2] == "[R]" and visible_bot_grid[a][b - 2] == "[ ]":
                                visible_bot_grid[a][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 2] == "[R]" and visible_bot_grid[a - 1][b - 2] == "[ ]":
                                visible_bot_grid[a - 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 2] == "[R]" and visible_bot_grid[a + 1][b - 2] == "[ ]":
                                visible_bot_grid[a + 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b + 1] == "[B]" and bot_grid[a][b + 2] == "[B]" and bot_grid[a][b + 3] == "[B]":
                    if visible_bot_grid[a][b + 1] == "[X]" and visible_bot_grid[a][b + 2] == "[X]" and visible_bot_grid[a][b + 3] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 2] == "[R]" and visible_bot_grid[a - 1][b + 2] == "[ ]":
                                visible_bot_grid[a - 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 2] == "[R]" and visible_bot_grid[a + 1][b + 2] == "[ ]":
                                visible_bot_grid[a + 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 3] == "[R]" and visible_bot_grid[a - 1][b + 3] == "[ ]":
                                visible_bot_grid[a - 1][b + 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 3] == "[R]" and visible_bot_grid[a + 1][b + 3] == "[ ]":
                                visible_bot_grid[a + 1][b + 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 4] == "[R]" and visible_bot_grid[a][b + 4] == "[ ]":
                                visible_bot_grid[a][b + 4] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 4] == "[R]" and visible_bot_grid[a - 1][b + 4] == "[ ]":
                                visible_bot_grid[a - 1][b + 4] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 4] == "[R]" and visible_bot_grid[a + 1][b + 4] == "[ ]":
                                visible_bot_grid[a + 1][b + 4] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b + 1] == "[B]" and bot_grid[a][b + 2] == "[B]" and bot_grid[a][b + 3] != "[B]":
                    if visible_bot_grid[a][b + 1] == "[X]" and visible_bot_grid[a][b + 2] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 2] == "[R]" and visible_bot_grid[a + 1][b + 2] == "[ ]":
                                visible_bot_grid[a + 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                             if bot_grid[a - 1][b + 2] == "[R]" and visible_bot_grid[a - 1][b + 2] == "[ ]":
                                visible_bot_grid[a - 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 3] == "[R]" and visible_bot_grid[a][b + 3] == "[ ]":
                                visible_bot_grid[a][b + 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 3] == "[R]" and visible_bot_grid[a - 1][b + 3] == "[ ]":
                                visible_bot_grid[a - 1][b + 3] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 3] == "[R]" and visible_bot_grid[a + 1][b + 3] == "[ ]":
                                visible_bot_grid[a + 1][b + 3] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b + 1] == "[B]" and bot_grid[a][b + 2] != "[B]":
                    if visible_bot_grid[a][b + 1] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 2] == "[R]" and visible_bot_grid[a][b + 2] == "[ ]":
                                visible_bot_grid[a][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 2] == "[R]" and visible_bot_grid[a + 1][b + 2] == "[ ]":
                                visible_bot_grid[a + 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 2] == "[R]" and visible_bot_grid[a - 1][b + 2] == "[ ]":
                                visible_bot_grid[a - 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a + 1][b] == "[B]" and bot_grid[a + 2][b] == "[B]" and bot_grid[a + 3][b] == "[B]":
                    if visible_bot_grid[a + 1][b] == "[X]" and visible_bot_grid[a + 2][b] == "[X]" and visible_bot_grid[a + 3][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b - 1] == "[R]" and visible_bot_grid[a + 2][b - 1] == "[ ]":
                                visible_bot_grid[a + 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b + 1] == "[R]" and visible_bot_grid[a + 2][b + 1] == "[ ]":
                                visible_bot_grid[a + 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 3][b - 1] == "[R]" and visible_bot_grid[a + 3][b - 1] == "[ ]":
                                visible_bot_grid[a + 3][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 3][b + 1] == "[R]" and visible_bot_grid[a + 3][b + 1] == "[ ]":
                                visible_bot_grid[a + 3][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 4][b] == "[R]" and visible_bot_grid[a + 4][b] == "[ ]":
                                visible_bot_grid[a + 4][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 4][b - 1] == "[R]" and visible_bot_grid[a + 4][b - 1] == "[ ]":
                                visible_bot_grid[a + 4][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 4][b + 1] == "[R]" and visible_bot_grid[a + 4][b + 1] == "[ ]":
                                visible_bot_grid[a + 4][b + 1] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a + 1][b] == "[B]" and bot_grid[a + 2][b] == "[B]" and bot_grid[a + 3][b] != "[B]":
                    if visible_bot_grid[a + 1][b] == "[X]" and visible_bot_grid[a + 2][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b + 1] == "[R]" and visible_bot_grid[a + 2][b + 1] == "[ ]":
                                visible_bot_grid[a + 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b - 1] == "[R]" and visible_bot_grid[a + 2][b - 1] == "[ ]":
                                visible_bot_grid[a + 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 3][b] == "[R]" and visible_bot_grid[a + 3][b] == "[ ]":
                                visible_bot_grid[a + 3][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 3][b + 1] == "[R]" and visible_bot_grid[a + 3][b + 1] == "[ ]":
                                visible_bot_grid[a + 3][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 3][b - 1] == "[R]" and visible_bot_grid[a + 3][b - 1] == "[ ]":
                                visible_bot_grid[a + 3][b - 1] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a + 1][b] == "[B]" and bot_grid[a + 2][b] != "[B]":
                    if visible_bot_grid[a + 1][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b] == "[R]" and visible_bot_grid[a + 2][b] == "[ ]":
                                visible_bot_grid[a + 2][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b + 1] == "[R]" and visible_bot_grid[a + 2][b + 1] == "[ ]":
                                visible_bot_grid[a + 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b - 1] == "[R]" and visible_bot_grid[a + 2][b - 1] == "[ ]":
                                visible_bot_grid[a + 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a - 1][b] == "[B]" and bot_grid[a - 2][b] == "[B]" and bot_grid[a - 3][b] == "[B]":
                    if visible_bot_grid[a - 1][b] == "[X]" and visible_bot_grid[a - 2][b] == "[X]" and visible_bot_grid[a - 3][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b - 1] == "[R]" and visible_bot_grid[a - 2][b - 1] == "[ ]":
                                visible_bot_grid[a - 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b + 1] == "[R]" and visible_bot_grid[a - 2][b + 1] == "[ ]":
                                visible_bot_grid[a - 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 3][b - 1] == "[R]" and visible_bot_grid[a - 3][b - 1] == "[ ]":
                                visible_bot_grid[a - 3][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 3][b + 1] == "[R]" and visible_bot_grid[a - 3][b + 1] == "[ ]":
                                visible_bot_grid[a - 3][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 4][b] == "[R]" and visible_bot_grid[a - 4][b] == "[ ]":
                                visible_bot_grid[a - 4][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 4][b - 1] == "[R]" and visible_bot_grid[a - 4][b - 1] == "[ ]":
                                visible_bot_grid[a - 4][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 4][b + 1] == "[R]" and visible_bot_grid[a - 4][b + 1] == "[ ]":
                                visible_bot_grid[a - 4][b + 1] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a - 1][b] == "[B]" and bot_grid[a - 2][b] == "[B]" and bot_grid[a - 3][b] != "[B]":
                    if visible_bot_grid[a - 1][b] == "[X]" and visible_bot_grid[a - 2][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b - 1] == "[R]" and visible_bot_grid[a - 2][b - 1] == "[ ]":
                                visible_bot_grid[a - 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b + 1] == "[R]" and visible_bot_grid[a - 2][b + 1] == "[ ]":
                                visible_bot_grid[a - 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 3][b + 1] == "[R]" and visible_bot_grid[a - 3][b + 1] == "[ ]":
                                visible_bot_grid[a - 3][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 3][b - 1] == "[R]" and visible_bot_grid[a - 3][b - 1] == "[ ]":
                                visible_bot_grid[a - 3][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 3][b] == "[R]" and visible_bot_grid[a - 3][b] == "[ ]":
                                visible_bot_grid[a - 3][b] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
            try:
                if bot_grid[a - 1][b] == "[B]" and bot_grid[a - 2][b] != "[B]":
                    if visible_bot_grid[a - 1][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b] == "[R]" and visible_bot_grid[a - 2][b] == "[ ]":
                                visible_bot_grid[a - 2][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b - 1] == "[R]" and visible_bot_grid[a - 2][b - 1] == "[ ]":
                                visible_bot_grid[a - 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b + 1] == "[R]" and visible_bot_grid[a - 2][b + 1] == "[ ]":
                                visible_bot_grid[a - 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
            except IndexError:
                k = 0
        elif ships_near_shot == 2:

                try:
                    if bot_grid[a - 1][b] == "[B]" and bot_grid[a + 1][b] == "[B]"\
                            and visible_bot_grid[a - 1][b] == "[X]" and visible_bot_grid[a + 1][b] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a - 2][b] == "[B]" or bot_grid[a + 2][b] == "[B]":
                                if bot_grid[a - 1][b] == "[B]":
                                    try:
                                        if bot_grid[a - 3][b] == "[R]" and visible_bot_grid[a - 3][b] == "[ ]":
                                            visible_bot_grid[a - 3][b] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a - 3][b + 1] == "[R]" and visible_bot_grid[a - 3][b + 1] == "[ ]":
                                            visible_bot_grid[a - 3][b + 1] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a - 3][b - 1] == "[R]" and visible_bot_grid[a - 3][b - 1] == "[ ]":
                                            visible_bot_grid[a - 3][b - 1] = "[0]"
                                    except IndexError:
                                        k = 0
                                if bot_grid[a + 1][b] == "[B]":
                                    try:
                                        if bot_grid[a + 3][b] == "[R]" and visible_bot_grid[a + 3][b] == "[ ]":
                                            visible_bot_grid[a + 3][b] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a + 3][b + 1] == "[R]" and visible_bot_grid[a + 3][b + 1] == "[ ]":
                                            visible_bot_grid[a + 3][b + 1] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a + 3][b - 1] == "[R]" and visible_bot_grid[a + 3][b - 1] == "[ ]":
                                            visible_bot_grid[a + 3][b - 1] = "[0]"
                                    except IndexError:
                                        k = 0
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b + 1] == "[R]" and visible_bot_grid[a - 2][b + 1] == "[ ]":
                                visible_bot_grid[a - 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b - 1] == "[R]" and visible_bot_grid[a - 2][b - 1] == "[ ]":
                                visible_bot_grid[a - 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 2][b] == "[R]" and visible_bot_grid[a - 2][b] == "[ ]":
                                visible_bot_grid[a - 2][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b] == "[R]" and visible_bot_grid[a + 2][b] == "[ ]":
                                visible_bot_grid[a + 2][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b + 1] == "[R]" and visible_bot_grid[a + 2][b + 1] == "[ ]":
                                visible_bot_grid[a + 2][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 2][b - 1] == "[R]" and visible_bot_grid[a + 2][b - 1] == "[ ]":
                                visible_bot_grid[a + 2][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                except IndexError:
                    k = 0
                try:
                    if bot_grid[a][b - 1] == "[B]" and bot_grid[a][b + 1] == "[B]"\
                            and visible_bot_grid[a][b - 1] == "[X]" and visible_bot_grid[a][b + 1] == "[X]":
                        if visible_bot_grid[a][b] != "[X]":
                            kill = 1
                        else:
                            kill = 2
                        try:
                            if bot_grid[a][b - 2] == "[B]" or bot_grid[a][b + 2] == "[B]":
                                if bot_grid[a][b - 2] == "[B]":
                                    try:
                                        if bot_grid[a][b - 3] == "[R]" and visible_bot_grid[a][b - 3] == "[ ]":
                                            visible_bot_grid[a][b - 3] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a - 1][b - 3] == "[R]" and visible_bot_grid[a - 1][b - 3] == "[ ]":
                                            visible_bot_grid[a - 1][b - 3] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a + 1][b - 3] == "[R]" and visible_bot_grid[a + 1][b - 3] == "[ ]":
                                            visible_bot_grid[a + 1][b - 3] = "[0]"
                                    except IndexError:
                                        k = 0
                                if bot_grid[a][b + 2] == "[B]":
                                    try:
                                        if bot_grid[a][b + 3] == "[R]" and visible_bot_grid[a][b + 3] == "[ ]":
                                            visible_bot_grid[a][b + 3] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a - 1][b + 3] == "[R]" and visible_bot_grid[a - 1][b + 3] == "[ ]":
                                            visible_bot_grid[a - 1][b + 3] = "[0]"
                                    except IndexError:
                                        k = 0
                                    try:
                                        if bot_grid[a + 1][b + 3] == "[R]" and visible_bot_grid[a + 1][b + 3] == "[ ]":
                                            visible_bot_grid[a + 1][b + 3] = "[0]"
                                    except IndexError:
                                        k = 0
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b] == "[R]" and visible_bot_grid[a + 1][b] == "[ ]":
                                visible_bot_grid[a + 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 1] == "[R]" and visible_bot_grid[a][b + 1] == "[ ]":
                                visible_bot_grid[a][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 1] == "[R]" and visible_bot_grid[a + 1][b + 1] == "[ ]":
                                visible_bot_grid[a + 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b] == "[R]" and visible_bot_grid[a - 1][b] == "[ ]":
                                visible_bot_grid[a - 1][b] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 1] == "[R]" and visible_bot_grid[a][b - 1] == "[ ]":
                                visible_bot_grid[a][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 1] == "[R]" and visible_bot_grid[a - 1][b - 1] == "[ ]":
                                visible_bot_grid[a - 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 1] == "[R]" and visible_bot_grid[a - 1][b + 1] == "[ ]":
                                visible_bot_grid[a - 1][b + 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 1] == "[R]" and visible_bot_grid[a + 1][b - 1] == "[ ]":
                                visible_bot_grid[a + 1][b - 1] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b - 2] == "[R]" and visible_bot_grid[a - 1][b - 2] == "[ ]":
                                visible_bot_grid[a - 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b - 2] == "[R]" and visible_bot_grid[a + 1][b - 2] == "[ ]":
                                visible_bot_grid[a + 1][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b - 2] == "[R]" and visible_bot_grid[a][b - 2] == "[ ]":
                                visible_bot_grid[a][b - 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a][b + 2] == "[R]" and visible_bot_grid[a][b + 2] == "[ ]":
                                visible_bot_grid[a][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a - 1][b + 2] == "[R]" and visible_bot_grid[a - 1][b + 2] == "[ ]":
                                visible_bot_grid[a - 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                        try:
                            if bot_grid[a + 1][b + 2] == "[R]" and visible_bot_grid[a + 1][b + 2] == "[ ]":
                                visible_bot_grid[a + 1][b + 2] = "[0]"
                        except IndexError:
                            k = 0
                except IndexError:
                    k = 0
        else:
            print("else")
            if visible_bot_grid[a][b] != "[X]":
                kill = 1
            else:
                kill = 2
            try:
                visible_bot_grid[a + 1][b] = "[0]"
            except IndexError:
                k = 0
            try:
                visible_bot_grid[a - 1][b] = "[0]"
            except IndexError:
                k = 0
            try:
                visible_bot_grid[a][b + 1] = "[0]"
            except IndexError:
                k = 0
            try:
                if bot_grid[a][b - 1] == "[ ]" or bot_grid[a][b - 1] == "[R]":
                    visible_bot_grid[a][b - 1] = "[0]"
            except IndexError:
                k = 0
            try:
                visible_bot_grid[a - 1][b + 1] = "[0]"
            except IndexError:
                k = 0
            try:
                if bot_grid[a + 1][b - 1] == "[ ]" or bot_grid[a + 1][b - 1] == "[R]":
                    visible_bot_grid[a + 1][b - 1] = "[0]"
            except IndexError:
                k = 0
            try:
                if bot_grid[a - 1][b - 1] == "[ ]" or bot_grid[a - 1][b - 1] == "[R]":
                   visible_bot_grid[a - 1][b - 1] = "[0]"
            except IndexError:
                k = 0
            try:
                visible_bot_grid[a + 1][b + 1] = "[0]"
            except IndexError:
                k = 0
        visible_bot_grid[a][b] = "[X]"
        print("               YOUR SHIPS")
        show_visible_player_grid()
        print("             OPPONENT SHIPS")
        show_visible_bot_grid()
        global killed
        if kill == 1:
            if killed == 1:
                print("Killed ship! There are", 10 - killed, "ships left.")
            elif killed > 1:
                print("Killed", killed, "ships! There are", 10 - killed, "ships left.")
            killed += 1
        elif kill == 2:
            if killed == 1:
                print("Killed ship! There are", 10 - killed, "ships left.")
            elif killed > 1:
                print("Killed", killed, "ships! There are", 10 - killed, "ships left.")
        else:
            print("Hit! There are", 11 - killed, "ships left.")
    else:
        visible_bot_grid[a][b] = "[0]"
        print("               YOUR SHIPS")
        show_visible_player_grid()
        print("             OPPONENT SHIPS")
        show_visible_bot_grid()
        print("You missed.")


def put_ship(a, b, c):
    global err, ship_quantity
    err = 1
    if offset == "y" or offset == "x":
        err = 0
    if c == 4:
        if offset == "x":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 3] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 3] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 3] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 4] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b + 4] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 4] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a][b + 1] = "[B]"
                visible_player_grid[a][b + 2] = "[B]"
                visible_player_grid[a][b + 3] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a][b + 1] = "[B]"
                player_grid[a][b + 2] = "[B]"
                player_grid[a][b + 3] = "[B]"
        if offset == "y":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 3][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 3][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 3][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 4][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 4][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 4][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a + 1][b] = "[B]"
                visible_player_grid[a + 2][b] = "[B]"
                visible_player_grid[a + 3][b] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a + 1][b] = "[B]"
                player_grid[a + 2][b] = "[B]"
                player_grid[a + 3][b] = "[B]"
            else:
                err = 1
    if c == 3:
        if offset == "x":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 3] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b + 3] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 3] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a][b + 1] = "[B]"
                visible_player_grid[a][b + 2] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a][b + 1] = "[B]"
                player_grid[a][b + 2] = "[B]"
        if offset == "y":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 3][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 3][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 3][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a + 1][b] = "[B]"
                visible_player_grid[a + 2][b] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a + 1][b] = "[B]"
                player_grid[a + 2][b] = "[B]"
            else:
                err = 1
    if c == 2:
        if offset == "x":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 2] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 2] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a][b + 1] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a][b + 1] = "[B]"
        if offset == "y":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 2][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 2][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                visible_player_grid[a + 1][b] = "[B]"
                player_grid[a][b] = "[B]"
                player_grid[a + 1][b] = "[B]"
            else:
                err = 1
    if c == 1:
        if offset == "x":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                player_grid[a][b] = "[B]"
        if offset == "y":
            try:
                if player_grid[a][b] == "[B]":
                    err = 1
            except IndexError:
                err = 1
            try:
                if player_grid[a + 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a + 1][b - 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            try:
                if player_grid[a - 1][b + 1] == "[B]":
                    err = 1
            except IndexError:
                k = 0
            if err == 0:
                visible_player_grid[a][b] = "[B]"
                player_grid[a][b] = "[B]"
            else:
                err = 1
    show_visible_player_grid()
    if err == 1:
        print("Wrong answer! Try again!")
    else:
        print("Done")
        ship_quantity += 1


def bot_shot():
    global prev_shot_hited, prev_a, prev_b, finding_part_of_ship
    kill = 0
    ships_near_shot = 0
    shot_offset = 1

    if finding_part_of_ship == 1:
        #
    else:
        if prev_shot_hited == 1:
            #
        else:
            while new_num == 0:
                global a, b
                a = random.randint(1, 10)
                b = random.randint(0, 9)
                if visible_player_grid[a][b] == "[X]":
                    new_num = 0
                else:
                    new_num = 1
            if player_grid[a][b] == "[B]":
                visible_player_grid = "[X]"
                if player_grid[a + 1][b] == "[B]":
                    ships_near_shot += 1
                if player_grid[a - 1][b] == "[B]":
                    ships_near_shot += 1
                if player_grid[a][b + 1] == "[B]":
                    ships_near_shot += 1
                if player_grid[a][b - 1] == "[B]":
                    ships_near_shot += 1
                if ships_near_shot == 0:
                    try:
                        visible_player_grid[a + 1][b] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a - 1][b] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a][b + 1] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a][b - 1] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a - 1][b + 1] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a + 1][b - 1] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a - 1][b - 1] = "[0]"
                    except IndexError:
                        k = 0
                    try:
                        visible_player_grid[a + 1][b + 1] = "[0]"
                    except IndexError:
                        k = 0
                    prev_shot_hited = 1
                    finding_part_of_ship = 0
                    visible_player_grid[a][b] = "[X]"
                    print("               YOUR SHIPS")
                    show_visible_player_grid()
                    print("             OPPONENT SHIPS")
                    show_visible_bot_grid()
                elif ships_near_shot == 1:
                    try:
                        if player_grid[a][b - 1] == "[B]" and player_grid[a][b - 2] == "[B]" and player_grid[a][
                            b - 3] == "[B]":
                            if visible_player_grid[a][b - 1] == "[X]" and visible_player_grid[a][b - 2] == "[X]" and \
                                    visible_player_grid[a][b - 3] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 2] == "[ ]" and visible_player_grid[a + 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a + 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 2] == "[ ]" and visible_player_grid[a - 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a - 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 3] == "[ ]" and visible_player_grid[a + 1][
                                        b - 3] == "[ ]":
                                        visible_player_grid[a + 1][b - 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 3] == "[ ]" and visible_player_grid[a - 1][
                                        b - 3] == "[ ]":
                                        visible_player_grid[a - 1][b - 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 4] == "[ ]" and visible_player_grid[a][b - 4] == "[ ]":
                                        visible_player_grid[a][b - 4] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 4] == "[ ]" and visible_player_grid[a + 1][
                                        b - 4] == "[ ]":
                                        visible_player_grid[a + 1][b - 4] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 4] == "[ ]" and visible_player_grid[a - 1][
                                        b - 4] == "[ ]":
                                        visible_player_grid[a - 1][b - 4] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a][b - 1] == "[B]" and player_grid[a][b - 2] == "[B]" and player_grid[a][
                            b - 3] != "[B]":
                            if visible_player_grid[a][b - 1] == "[X]" and visible_player_grid[a][b - 2] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 2] == "[ ]" and visible_player_grid[a + 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a + 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 2] == "[ ]" and visible_player_grid[a - 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a - 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 3] == "[ ]" and visible_player_grid[a][b - 3] == "[ ]":
                                        visible_player_grid[a][b - 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 3] == "[ ]" and visible_player_grid[a + 1][
                                        b - 3] == "[ ]":
                                        visible_player_grid[a + 1][b - 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 3] == "[ ]" and visible_player_grid[a - 1][
                                        b - 3] == "[ ]":
                                        visible_player_grid[a - 1][b - 3] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a][b - 1] == "[B]" and player_grid[a][b - 2] != "[B]":
                            if visible_player_grid[a][b - 1] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 2] == "[ ]" and visible_player_grid[a][b - 2] == "[ ]":
                                        visible_player_grid[a][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 2] == "[ ]" and visible_player_grid[a - 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a - 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 2] == "[ ]" and visible_player_grid[a + 1][
                                        b - 2] == "[ ]":
                                        visible_player_grid[a + 1][b - 2] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a][b + 1] == "[B]" and player_grid[a][b + 2] == "[B]" and player_grid[a][
                            b + 3] == "[B]":
                            if visible_player_grid[a][b + 1] == "[X]" and visible_player_grid[a][b + 2] == "[X]" and \
                                    visible_player_grid[a][b + 3] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 2] == "[ ]" and visible_player_grid[a - 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a - 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 2] == "[ ]" and visible_player_grid[a + 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a + 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 3] == "[ ]" and visible_player_grid[a - 1][
                                        b + 3] == "[ ]":
                                        visible_player_grid[a - 1][b + 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 3] == "[ ]" and visible_player_grid[a + 1][
                                        b + 3] == "[ ]":
                                        visible_player_grid[a + 1][b + 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 4] == "[ ]" and visible_player_grid[a][b + 4] == "[ ]":
                                        visible_player_grid[a][b + 4] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 4] == "[ ]" and visible_player_grid[a - 1][
                                        b + 4] == "[ ]":
                                        visible_player_grid[a - 1][b + 4] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 4] == "[ ]" and visible_player_grid[a + 1][
                                        b + 4] == "[ ]":
                                        visible_player_grid[a + 1][b + 4] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a][b + 1] == "[B]" and player_grid[a][b + 2] == "[B]" and player_grid[a][
                            b + 3] != "[B]":
                            if visible_player_grid[a][b + 1] == "[X]" and visible_player_grid[a][b + 2] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 2] == "[ ]" and visible_player_grid[a + 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a + 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 2] == "[ ]" and visible_player_grid[a - 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a - 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 3] == "[ ]" and visible_player_grid[a][b + 3] == "[ ]":
                                        visible_player_grid[a][b + 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 3] == "[ ]" and visible_player_grid[a - 1][
                                        b + 3] == "[ ]":
                                        visible_player_grid[a - 1][b + 3] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 3] == "[ ]" and visible_player_grid[a + 1][
                                        b + 3] == "[ ]":
                                        visible_player_grid[a + 1][b + 3] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a][b + 1] == "[B]" and player_grid[a][b + 2] != "[B]":
                            if visible_player_grid[a][b + 1] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 2] == "[ ]" and visible_player_grid[a][b + 2] == "[ ]":
                                        visible_player_grid[a][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 2] == "[ ]" and visible_player_grid[a + 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a + 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 2] == "[ ]" and visible_player_grid[a - 1][
                                        b + 2] == "[ ]":
                                        visible_player_grid[a - 1][b + 2] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a + 1][b] == "[B]" and player_grid[a + 2][b] == "[B]" and player_grid[a + 3][
                            b] == "[B]":
                            if visible_player_grid[a + 1][b] == "[X]" and visible_player_grid[a + 2][b] == "[X]" and \
                                    visible_player_grid[a + 3][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b - 1] == "[ ]" and visible_player_grid[a + 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b + 1] == "[ ]" and visible_player_grid[a + 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 3][b - 1] == "[ ]" and visible_player_grid[a + 3][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 3][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 3][b + 1] == "[ ]" and visible_player_grid[a + 3][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 3][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 4][b] == "[ ]" and visible_player_grid[a + 4][b] == "[ ]":
                                        visible_player_grid[a + 4][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 4][b - 1] == "[ ]" and visible_player_grid[a + 4][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 4][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 4][b + 1] == "[ ]" and visible_player_grid[a + 4][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 4][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a + 1][b] == "[B]" and player_grid[a + 2][b] == "[B]" and player_grid[a + 3][
                            b] != "[B]":
                            if visible_player_grid[a + 1][b] == "[X]" and visible_player_grid[a + 2][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b + 1] == "[ ]" and visible_player_grid[a + 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b - 1] == "[ ]" and visible_player_grid[a + 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 3][b] == "[ ]" and visible_player_grid[a + 3][b] == "[ ]":
                                        visible_player_grid[a + 3][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 3][b + 1] == "[ ]" and visible_player_grid[a + 3][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 3][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 3][b - 1] == "[ ]" and visible_player_grid[a + 3][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 3][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a + 1][b] == "[B]" and player_grid[a + 2][b] != "[B]":
                            if visible_player_grid[a + 1][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b] == "[ ]" and visible_player_grid[a + 2][b] == "[ ]":
                                        visible_player_grid[a + 2][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b + 1] == "[ ]" and visible_player_grid[a + 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 2][b - 1] == "[ ]" and visible_player_grid[a + 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a - 1][b] == "[B]" and player_grid[a - 2][b] == "[B]" and player_grid[a - 3][
                            b] == "[B]":
                            if visible_player_grid[a - 1][b] == "[X]" and visible_player_grid[a - 2][b] == "[X]" and \
                                    visible_player_grid[a - 3][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b - 1] == "[ ]" and visible_player_grid[a - 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b + 1] == "[ ]" and visible_player_grid[a - 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 3][b - 1] == "[ ]" and visible_player_grid[a - 3][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 3][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 3][b + 1] == "[ ]" and visible_player_grid[a - 3][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 3][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 4][b] == "[ ]" and visible_player_grid[a - 4][b] == "[ ]":
                                        visible_player_grid[a - 4][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 4][b - 1] == "[ ]" and visible_player_grid[a - 4][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 4][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 4][b + 1] == "[ ]" and visible_player_grid[a - 4][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 4][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a - 1][b] == "[B]" and player_grid[a - 2][b] == "[B]" and player_grid[a - 3][
                            b] != "[B]":
                            if visible_player_grid[a - 1][b] == "[X]" and visible_player_grid[a - 2][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b - 1] == "[ ]" and visible_player_grid[a - 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b + 1] == "[ ]" and visible_player_grid[a - 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 3][b + 1] == "[ ]" and visible_player_grid[a - 3][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 3][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 3][b - 1] == "[ ]" and visible_player_grid[a - 3][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 3][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 3][b] == "[ ]" and visible_player_grid[a - 3][b] == "[ ]":
                                        visible_player_grid[a - 3][b] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0
                    try:
                        if player_grid[a - 1][b] == "[B]" and player_grid[a - 2][b] != "[B]":
                            if visible_player_grid[a - 1][b] == "[X]":
                                try:
                                    if player_grid[a + 1][b] == "[ ]" and visible_player_grid[a + 1][b] == "[ ]":
                                        visible_player_grid[a + 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b + 1] == "[ ]" and visible_player_grid[a][b + 1] == "[ ]":
                                        visible_player_grid[a][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b + 1] == "[ ]" and visible_player_grid[a + 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a + 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b] == "[ ]" and visible_player_grid[a - 1][b] == "[ ]":
                                        visible_player_grid[a - 1][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a][b - 1] == "[ ]" and visible_player_grid[a][b - 1] == "[ ]":
                                        visible_player_grid[a][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b - 1] == "[ ]" and visible_player_grid[a - 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 1][b + 1] == "[ ]" and visible_player_grid[a - 1][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 1][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a + 1][b - 1] == "[ ]" and visible_player_grid[a + 1][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a + 1][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b] == "[ ]" and visible_player_grid[a - 2][b] == "[ ]":
                                        visible_player_grid[a - 2][b] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b - 1] == "[ ]" and visible_player_grid[a - 2][
                                        b - 1] == "[ ]":
                                        visible_player_grid[a - 2][b - 1] = "[0]"
                                except IndexError:
                                    k = 0
                                try:
                                    if player_grid[a - 2][b + 1] == "[ ]" and visible_player_grid[a - 2][
                                        b + 1] == "[ ]":
                                        visible_player_grid[a - 2][b + 1] = "[0]"
                                except IndexError:
                                    k = 0
                    except IndexError:
                        k = 0


            else:
                visible_player_grid = "[0]"
                finding_part_of_ship = 0
                prev_shot_hited = 0






def show_visible_bot_grid():
    for r in range(10):
        if r == 0:
            print("  -" + str(ABC[r]) + "-", end="")
        else:
            print(" -" + str(ABC[r]) + "-", end="")
    print()
    for f in range(10):
        print(*visible_bot_grid[f])
    print()


def show_bot_grid():
    for r in range(10):
        if r == 0:
            print("  -" + str(ABC[r]) + "-", end="")
        else:
            print(" -" + str(ABC[r]) + "-", end="")
    print()
    for f in range(10):
        print(*bot_grid[f])
    print()


def show_visible_player_grid():
    for r in range(10):
        if r == 0:
            print("  -" + str(ABC[r]) + "-", end="")
        else:
            print(" -" + str(ABC[r]) + "-", end="")
    print()
    for f in range(10):
        print(*visible_player_grid[f])
    print()


def show_player_grid():
    for r in range(10):
        if r == 0:
            print("  -" + str(ABC[r]) + "-", end="")
        else:
            print(" -" + str(ABC[r]) + "-", end="")
    print()
    for f in range(10):
        print(*player_grid[f])
    print()


for h in range(11):
    visible_bot_grid.append([h])
    for x in range(10):
        visible_bot_grid[h].append("[ ]")

for i in range(11):
    bot_grid.append([i])
    for x in range(10):
        bot_grid[i].append("[ ]")

for h in range(10):
    visible_player_grid.append([h])
    for x in range(10):
        visible_player_grid[h].append("[ ]")

for i in range(11): # (11) - to make put_ship() work right
    player_grid.append([i])
    for x in range(11): # (11) - to make put_ship() work right
        player_grid[i].append("[ ]")

for h in range(10):
    add_bot_ship(ships[h])

# --Playing--
'''
name = input("What's your name? ")
print("Welcome to Ship Wars, {}!".format(name))
show_visible_player_grid()
print("Place your ships on the battlefield, select the offset (y or x)"
      " and place the ship by printing the coordinates (print letter"
      " first and then number) of the upper left corner")
while ship_quantity <= 9:
    if ship_quantity <= 5:
        offset = input("Choose offset to place {} deck ship (x or y): "
            .format(ships[ship_quantity]))
    else:
        print("Choose offset to place 1 deck ship")
    Coordinates = input("Coordinates are: ")
    error_in_coordinates = 1
    for i in range(0, 11):
        for x in range(0, 10):
            if Coordinates == str(abc[i])+str(x) or Coordinates == str(ABC[i])+str(x)\
             or Coordinates == str(x)+str(ABC[i]) or Coordinates == str(x)+str(abc[i]):
                put_ship(x, i+1, ships[ship_quantity])
                error_in_coordinates = 0
    if error_in_coordinates != 0:
        show_visible_player_grid()
        print("Wrong answer! Try again!")
'''

#TEST BUILD FOR BOT
offset = "y"
put_ship(0, 1, 3)
offset = "x"
put_ship(1, 3, 3)
offset = "y"
put_ship(4, 7, 2)
offset = "x"
put_ship(8, 2, 2)
offset = "x"
put_ship(4, 4, 2)
offset = "y"
put_ship(4, 10, 1)
offset = "x"
put_ship(8, 9, 1)
offset = "x"
put_ship(1, 8, 1)
offset = "x"
put_ship(8, 6, 1)
offset = "x"
put_ship(6, 2, 1)

print("               YOUR SHIPS")
show_visible_player_grid()
show_player_grid()
print("             OPPONENT SHIPS")
show_visible_bot_grid()
show_bot_grid()
print("Choose where do you want to make shot and print letter first and then number")
while killed <= 10:
    error_in_coordinates = 1
    Coordinates = input("Coordinates are: ")
    for i in range(0, 11):
        for x in range(0, 10):
            if Coordinates == str(abc[i])+str(x) or Coordinates == str(ABC[i])+str(x)\
             or Coordinates == str(x)+str(ABC[i]) or Coordinates == str(x)+str(abc[i]):
                shot(x, i+1)
                error_in_coordinates = 0
    if Coordinates == "firewall" or Coordinates == "Firewall":
        print("             OPPONENT SHIPS")
        show_bot_grid()
        print("             OPPONENT SHIPS")
        show_visible_bot_grid()
    if error_in_coordinates != 0:
        print("               YOUR SHIPS")
        show_visible_player_grid()
        print("             OPPONENT SHIPS")
        show_visible_bot_grid()
        print("Wrong answer! Try again!")
    # bot_shot()
print("You win!")
