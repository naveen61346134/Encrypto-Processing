import sys
import time


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
    rev_arr = array[::-1]
    rev_arr.pop(0)
    main_key = array[5]

    proc_key = id_auth_proc(rev_arr)
    if proc_key == main_key:
        return True
    elif proc_key is False:
        print("Key Error!!")
        return False
    else:
        print("Invalid Key")
        return False


def check(key):
    for _ in range(2):
        inp_key = input("Enter key: ")
        if inp_key == key:
            print("Key is valid")
            return True
        else:
            print("Invalid Key")


def start():
    time.sleep(5)
    exit(0)


def test_handshake(args):
    ele = args.split("-")
    code = int(ele[1])
    if ele[0] == "handshake" and code % 2 == 0:
        print("handshake-nortxr".strip(""))
        sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        test_handshake(sys.argv[1].strip(""))
        exit(0)
    elif len(sys.argv) > 1:
        arg = sys.argv[1].strip("")
        id_auth = sys.argv[2].strip("")
        script_id_checker = script_id_auth(id_auth)
        if script_id_checker is True:
            print("\tScript Verification Successful\n")
            check(arg)
            if check is True:
                start()
        else:
            print("\tScript Verification Failed!\n")
    else:
        print("You did not pass the key.")

    time.sleep(10)
