#!/usr/bin/env python

import argparse

FILE_NAME = "TODO"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to run", choices=["add", "list", "pop"], default="list", nargs="?")
    parser.add_argument("task", help="Task to add/remove", nargs="?")
    args = parser.parse_args()

    if args.command == "add":
        add(args.task)
    elif args.command == "list":
        list()
    elif args.command == "pop":
        pop(int(args.task))
    else:
        print("Invalid command")

def add(task):
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")

def list():
    with open(FILE_NAME, "r") as f:
        for idx, line in enumerate(f):
            task = line.strip()
            print(f'{idx} {task}')


def pop(task_idx):
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    
    if len(lines) <= task_idx or task_idx < 0:
        print("Invalid task index")
        return

    task = lines[task_idx].strip()
    print(task)

    kept = lines[:task_idx] + lines[task_idx+1:]

    with open(FILE_NAME, "w") as f:
        f.write("".join(kept))

if __name__ == "__main__":
    main()
