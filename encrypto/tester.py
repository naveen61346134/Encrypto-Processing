import random


def algo_num():
    num_array = []
    num = random.randint(1000, 9999)
    while num > 0:
        dig = num % 10
        num_array.append(dig)
        num //= 10
    num_array.reverse()
    n1 = int(num_array[0])
    n2 = int(num_array[1])
    n3 = int(num_array[2])
    n4 = int(num_array[3])
    p1 = int(n1 + n3)
    p2 = int(n2 + n4)
    p1_o = False
    p2_o = False
    if p2 % 2 == 0 or p1 % 2 == 0:
        if p1 % 2 == 0:
            pass
        else:
            p1_o = True
        if p2 % 2 == 0:
            pass
        else:
            p2_o = True

        while p1_o is not False:
            if n1 % 2 == 0 and n3 % 2 != 0:
                n3 = n3 + 1
                if n3 % 2 == 0:
                    p1_o = False
                    break
                else:
                    continue
            elif n3 % 2 == 0 and n1 % 2 != 0:
                n1 = n1 + 1
                if n1 % 2 == 0:
                    p1_o = False
                    break
                else:
                    continue
            elif n1 % 2 != 0 and n3 % 2 != 0:
                n1 = n1 + 1
                n3 = n3 + 1
                if n1 % 2 == 0 and n3 % 2 == 0:
                    p1_o = False
                    break
                else:
                    continue
            else:
                print("Error")
                os.system('exit')

        while p2_o is not False:
            if n2 % 2 == 0 and n4 % 2 != 0:
                n4 = n4 + 1
                if n4 % 2 == 0:
                    p2_o = False
                    break
                else:
                    continue
            elif n4 % 2 == 0 and n2 % 2 != 0:
                n2 = n2 + 1
                if n2 % 2 == 0:
                    p2_o = False
                    break
                else:
                    continue
            elif n2 % 2 != 0 and n4 % 2 != 0:
                n2 = n2 + 1
                n4 = n4 + 1
                if n2 % 2 == 0 and n4 % 2 == 0:
                    p2_o = False
                    break
                else:
                    continue
            else:
                print("Error")
                os.system('exit')

        p1 = n1 + n3
        p2 = n2 + n4
        if p1 > p2:
            diff = p1 - p2
            if n1 - diff > 0:
                n1 = n1 - diff
            else:
                n3 = n3 - diff

            if n2 + diff <= 9:
                n2 = n2 + diff
            else:
                n4 = n4 + diff

    elif p1 % 2 != 0 and p2 % 2 != 0:
        p1_O = True
        p2_O = True
        while p1_O is not False:
            if n1 % 2 != 0:
                n1 = n1 + 1
                if n1 % 2 == 0:
                    pass
                else:
                    continue
            if n3 % 2 != 0:
                n3 = n3 + 1
                if n3 % 2 == 0:
                    pass
                else:
                    continue
            if n1 % 2 == 0 and n3 % 2 == 0:
                p1_O = False
                break
            else:
                continue

        while p2_O is not False:
            if n2 % 2 != 0:
                n2 = n2 + 1
                if n2 % 2 == 0:
                    pass
                else:
                    continue
            if n4 % 2 != 0:
                n4 = n4 + 1
                if n4 % 2 == 0:
                    pass
                else:
                    continue
            if n2 % 2 == 0 and n4 % 2 == 0:
                p2_O = False
                break
            else:
                continue

        p1 = n1 + n3
        p2 = n2 + n4
        if p1 > p2:
            diff = p1 - p2
            if n1 - diff > 0:
                n1 = n1 - diff
            else:
                n3 = n3 - diff

            if n2 + diff <= 9:
                n2 = n2 + diff
            else:
                n4 = n4 + diff
        else:
            pass
        if p1 == p2:
            if n1 - 2 > 0 and n1 - 2 <= 9:
                n1 = n1 - 2
            else:
                n3 = n3 - 2
        else:
            pass

    else:
        print("ERROR")
    new_num = f"{n1}{n2}{n3}{n4}"
    return new_num


number = algo_num()

while len(number) != 4:
    number = algo_num()
    if len(number) == 4:
        break
    else:
        continue

print(f"NUMBER: {number}")
