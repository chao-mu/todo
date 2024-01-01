# todo

Manages a TODO file in the current directory. Each line is considered a task. Offers abilities to add, remove (called pop here), and list the elements

Wrote just to be useful to myself, so the code is a 10 minute hack - hopefully you're not someone who I want to hire me.

Here's an example of its use.

```console
$ todo add 'write documentation'
$ todo add 'get a glass of water'
$ todo
0 write documentation
1 get a glass of water
$ todo pop 0
write documentation
$ todo
0 get a glass of water
$ cat TODO
get a glass of water
```

## Installation

Copy todo.py to somewhere included in your $PATH as "todo". Requires python, but no third party packages.
