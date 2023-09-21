import sys
import subprocess
import os

def welcome():
    subprocess.run(["chmod", "400", "/flag*"])
    subprocess.run(["chown", "task0:task0", "/tmp/game/ret2text", "/flag1"])
    subprocess.run(["chown", "task1:task1", "/tmp/game/ret2text-rev", "/flag2"])
    subprocess.run(["chown", "task2:task2", "/tmp/game/ret2text-rev-rev", "/flag3"])
    subprocess.run(["chown", "task3:task3", "/tmp/game/ret2text-rev-rev-rev", "/flag4"])
    banner = r'''
     _____   ____  _____
    |  __ \ / __ \|  __ \
    | |__) | |  | | |__) |
    |  _  /| |  | |  ___/
    | | \ \| |__| | |
    |_|  \_\\____/|_|
    '''
    print("\033[1;31;2m")
    print(banner)
    print("\033[0m")

def main():
    welcome()
    choice = int(input("[*] Challenge:  "))
    if choice == 0:
        subprocess.run(["su", "task0", "-s", "/bin/bash", "-c", "/tmp/game/ret2text"])
    elif choice == 1:
        subprocess.run(["su", "task1", "-s", "/bin/bash", "-c", "/tmp/game/ret2text-rev"])
    elif choice == 2:
        subprocess.run(["su", "task2", "-s", "/bin/bash", "-c", "/tmp/game/ret2text-rev-rev"])
    elif choice == 3:
        subprocess.run(["su", "task3", "-s", "/bin/bash", "-c", "/tmp/game/ret2text-rev-rev-rev"])
    else:
        print("Invalid!")

    sys.stdout.flush()
    sys.stderr.flush()

if __name__ == '__main__':
    main()
