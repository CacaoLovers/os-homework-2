import os
import sys
import time
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: child.py S")
        sys.exit(1)

    try:
        S = int(sys.argv[1])
    except ValueError:
        print("S must be an integer")
        sys.exit(1)

    pid = os.getpid()
    ppid = os.getppid()

    print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}. S is {S}.")

    time.sleep(S)

    print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}. Exit Status {random.randint(0, 1)}.")

if __name__ == '__main__':
    main()
