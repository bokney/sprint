import os, time, sys
 
def sprint(*args):
    string = "".join(map(str,args))
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(4./120)

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def wait(length):
    time.sleep(length)