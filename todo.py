#!/usr/bin/env python

import argparse

FILE_NAME = "TODO"

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Command to run", dest="command")
    subparsers.default = "list"

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("task", help="Task to add")

    subparsers.add_parser("list", help="List tasks")

    pop_parser = subparsers.add_parser("pop", help="Pop tasks")
    pop_parser.add_argument("tasks", help="Task to pop", type=int, nargs="*")

    shift_parser = subparsers.add_parser("shift", help="Shift tasks")
    shift_parser.add_argument("tasks", help="Task to shift", type=int, nargs="*")

    args = vars(parser.parse_args())
    command = args.pop("command")

    if command == "add":
        cmd_add(**args)
    elif command == "list":
        cmd_list(**args)
    elif command == "pop":
        cmd_pop(**args)
    elif command == "shift":
        cmd_shift(**args)
    else:
        print("Invalid command")

def cmd_add(task):
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")

def cmd_list():
    with open(FILE_NAME, "r") as f:
        for idx, line in enumerate(f):
            task = line.strip()
            print(f'{idx} {task}')

def cmd_shift(tasks):
    if not tasks:
        tasks = [0]

    cmd_pop(tasks)

def cmd_pop(tasks):
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    if not tasks:
        tasks = [len(lines) - 1]
    
    if any(task_idx >= len(lines) or task_idx < 0 for task_idx in tasks):
        print("Invalid task index listed")
        return

    kept = []
    for idx, line in enumerate(lines):
        if idx not in tasks:
            kept.append(line)
        else:
            print(line.strip())

    with open(FILE_NAME, "w") as f:
        f.write("".join(kept))

if __name__ == "__main__":
    main()
