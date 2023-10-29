import os
import sys
import time
import serial
import random


def filter(input):
    num = []
    ch = ""
    if input == 0:
        pass
    else:
        for digit in input:
            if digit.isdigit():
                num.append(digit)
            else:
                pass
        ch = ch.join(num)
    return ch


def processing_data(ser, proc_ser):
    print("")
    int_x = 0
    int_x_in = 180
    while int_x <= 180:
        p_data = ser.readline().decode(encoding='utf-8')
        if p_data.__contains__(" "):
            rand_int = random.randint(560, 500)
            pro_out = f"{int_x},{rand_int}."
            print(f"sending to processing random data: {pro_out}")
            proc_ser.write(str.encode(pro_out))
            int_x += 1
        elif p_data.__len__() > 0:
            p_filtered = filter(p_data)
            p_out = f"{int_x},{p_filtered}."
            print(f"sending to processing: {p_out}")
            proc_ser.write(str.encode(p_out))
            int_x += 1
        else:
            pass

    while int_x_in > 0:
        p_data = ser.readline().decode(encoding='utf-8')
        if p_data.__contains__(" "):
            rand_out = random.randint(456, 500)
            pro_out = f"{int_x_in},{rand_out}."
            print(f"Sending to processing random data: {pro_out}")
            proc_ser.write(str.encode(pro_out))
            int_x_in -= 1
        elif p_data.__len__() > 0:
            p_filtered = filter(p_data)
            p_out = f"{int_x_in},{p_filtered}."
            print(f"sending: {p_out}")
            proc_ser.write(str.encode(p_out))
            int_x_in -= 1
        else:
            pass


def serialLoader():
    try:
        port = int(input("Enter COM Port: "))
        serial_port = f"COM{port}"
        ser = serial.Serial(serial_port, 9600, timeout=0.050)
    except serial.SerialException:
        os.system('cls')
        print(f"{serial_port} Port Not Found")
        time.sleep(2)
        os.system('exit')
    except ValueError:
        os.system('cls')
        print("Enter a valid com port int")
        time.sleep(2)
        os.system('exit')
    try:
        port_p = int(input("Enter processing com port: "))
        serial_port_p = f"COM{port_p}"
        proc_ser = serial.Serial(serial_port_p, 9600, timeout=0.050)
    except serial.SerialException:
        os.system('cls')
        print("processing port not found")
        time.sleep(2)
        os.system('exit')
    except ValueError:
        os.system('cls')
        print("Enter a valid com port int")
        time.sleep(2)
        os.system('exit')
    try:
        print("Processing Data Transmission Started")
        while True:
            processing_data(ser, proc_ser)
    except KeyboardInterrupt:
        os.system('cls')
        print("Serial communication stopped!")
        time.sleep(2)
        os.system('exit')


def id_auth_proc(rev_array):
    elements = []
    auth_id = ""
    if rev_array != 0:
        for i in rev_array:
            if i.isalpha() or i.isdigit():
                elements.append(i)
            else:
                return False
    else:
        return False
    auth_id = auth_id.join(elements)
    return auth_id


def script_id_auth(id):
    array = id.split("-")
    if len(array) != 6:
        print("Invalid authorization ID!")
        return False
    rev_arr = array[::-1]
    rev_arr.pop(0)
    main_key = array[5]
    proc_key = id_auth_proc(rev_arr)
    if proc_key == main_key:
        return True
    else:
        print("Invalid authorization ID!")
        return False


def check(key):
    for _ in range(2):
        inp_key = input("Enter key: ")
        if inp_key == key:
            print("Key is valid")
            return True
        else:
            print("Invalid key")
    print("Maximum attempts reached. Exiting...")
    time.sleep(2)
    os.system('exit')


def start():
    print("Starting Serial Application...")
    time.sleep(3)
    serialLoader()


def algo_num(): r8_R67ll00OIVfgW9Q033boEaGG5TvwoNU0eG8K4
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


def test_handshake(args):
    ele = args.split("-")
    if len(ele) != 2:
        return
    code = int(ele[1])
    len_check = str(code)
    hand_num = algo_num()
    while len(hand_num) != 4:
        hand_num = algo_num()
        if len(hand_num) == 4:
            break
        else:
            continue
    if ele[0] == "handshake" and len(len_check) == 4 and code % 2 == 0:
        fstring = f"handshake-nortxr-{hand_num}"
        print(fstring.strip(""))
        sys.stdout.flush()
    else:
        print("Handshake Error")


def hand_mem_check():
    status = False
    try:
        with open("C:\\Users\\willi\\LocalMem\\sharmem", "r") as f:
            data = int(f.readline())
            if data == 1:
                status = True
            else:
                status = False
    except FileNotFoundError:
        print("Handshake has not been established yet!\nExiting now...")
        time.sleep(2)
        os.system('exit')
    return status


try:
    if __name__ == "__main__":
        if len(sys.argv) == 2:
            test_handshake(sys.argv[1].strip())
            os.system('exit')
        elif len(sys.argv) == 3:
            mem_check = hand_mem_check()
            if mem_check is False:
                print("Handshake Memory Verification Failed\nExiting now....")
                time.sleep(2)
                os.system('exit')
            elif mem_check is True:
                print("\tHandshake Memory Verification Successful")
                time.sleep(2)
                arg = sys.argv[1].strip()
                id_auth = sys.argv[2].strip()
                if script_id_auth(id_auth):
                    print("\tScript verification successful\n")
                    if check(arg):
                        start()
                    else:
                        os.system('exit')
                else:
                    os.system('exit')
            else:
                print("Memory Handshake Failed\nExiting now...")
                time.sleep(2)
                os.system('exit')
        else:
            print("Invalid arguments!")
            os.system('exit')
except KeyboardInterrupt:
    os.system(0)
    print("Stopped Process")
    os.system('exit')
