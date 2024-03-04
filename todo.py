#!/usr/bin/env python

import argparse

from dataclasses import dataclass
from pathlib import Path

@dataclass
class Options:
    path: Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", "-r", help="Root directory wherein TODO resides", default=".", type=Path)
    parser.add_argument("--file-name", "-f", help="File name", default="TODO", type=Path)

    subparsers = parser.add_subparsers(help="Command to run", dest="command")
    subparsers.default = "list"

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("task", help="Task to add")
 
    subparsers.add_parser("list", help="List tasks")

    pop_parser = subparsers.add_parser("pop", help="Pop tasks")
    pop_parser.add_argument("tasks", help="Tasks to pop", type=int, nargs="*")

    shift_parser = subparsers.add_parser("shift", help="Shift tasks")
    shift_parser.add_argument("tasks", help="Tasks to shift", type=int, nargs="*")

    subparsers.add_parser("sort", help="Sort tasks")

    args = vars(parser.parse_args())
    command = args.pop("command")
    options = Options(path=Path(args.pop("root"), args.pop("file_name")))

    app = TodoApp(options)

    if command == "add":
        app.cmd_add(**args)
    elif command == "list":
        app.cmd_list(**args)
    elif command == "pop":
        app.cmd_pop(**args)
    elif command == "shift":
        app.cmd_shift(**args)
    elif command == "sort":
        app.cmd_sort(**args)
    else:
        print("Unsupported command")

class TodoApp:

    def __init__(self, options: Options):
        self.path = options.path

    def read_tasks(self):
        tasks = []
        with open(self.path, "r") as f:
            for line in f:
                tasks.append(line.strip())

        return tasks

    def write_tasks(self, tasks):
        tasks = [task for task in tasks if task]
        with open(self.path, "w") as f:
            f.write("\n".join(tasks))

    def append_task(self, task):
        with open(self.path, "a") as f:
            f.write(task + "\n")

    def cmd_add(task):
        self.append_task(task)

    def cmd_list(self):
        tasks = self.read_tasks()
        for idx, task in enumerate(tasks):
            print(f'{idx} {task}')

    def cmd_shift(self, tasks):
        if not tasks:
            tasks = [0]

        self.cmd_pop(self, tasks)

    def cmd_sort(self):
        tasks = self.read_tasks()

        tasks.sort()

        self.write_tasks(tasks)

    def cmd_pop(self, tasks):
        existing_tasks = self.read_tasks()

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

        self.write_tasks(tasks)

if __name__ == "__main__":
    main()
