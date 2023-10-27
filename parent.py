#!/usr/bin/python
import os
import random
import sys

def child_process(N):
    S = random.randint(5, 10)
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}. N is {N}.")
    os._exit(random.randint(0, 1))

def main():
    if len(sys.argv) != 2:
        print("Usage: parent.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)

    parent_pid = os.getpid()
    child_pids = []

    for _ in range(N):
        child_pid = os.fork()
        if child_pid == 0:  # Child process
            child_process(N)
        else:
            print(f"Parent[{parent_pid}]: I ran children process with PID {child_pid}.")
            child_pids.append(child_pid)

    while child_pids:
        for child_pid in child_pids[:]:
            try:
                pid, status = os.waitpid(child_pid, os.WNOHANG)
                if pid != 0:
                    print(f"Parent[{parent_pid}]: Child with PID {pid} terminated. Exit Status {os.WEXITSTATUS(status)}.")
                    child_pids.remove(pid)
            except ChildProcessError:
                pass

if __name__ == '__main__':
    main()

