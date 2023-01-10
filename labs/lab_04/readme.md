# APSC-5984 Lab 4: File system

Due: 2023-02-13 (Monday) 23:59:59

- [APSC-5984 Lab 4: File system](#apsc-5984-lab-4-file-system)
  - [0. Overview](#0-overview)
  - [1. File system](#1-file-system)
    - [1.1 Command overview](#11-command-overview)
    - [1.2 `pwd` and `cd`](#12-pwd-and-cd)
    - [2. Interacting with files](#2-interacting-with-files)

## 0. Overview

In this lab, you will learn basic Unix commands to navigate the file system and manipulate files in the command line interface (CLI). These commands can also be implemented in Python using the `os` library. Coupling the basic knowledge of interacting with the file system, you will be able to read and write data from/to files through Python.

## 1. File system

### 1.1 Command overview

- `pwd`: print working directory
- `cd`: change directory
- `ls`: list files in the current directory
- `mkdir`: make a new directory
- `rm`: remove a file
- `cp`: copy a file
- `mv`: move a file

### 1.2 `pwd` and `cd`

To know where your current location, which is formally known as working directory (WD), is in the file system, you can use `pwd` command to print the path of the WD. `pwd` is an abbreviation of "print working directory". To do this, enter the command in the `terminal`:

```bash
$ pwd
/home/niche
```

It should print out your WD as an output. If you want to change your current WD, you can use the command `cd`, which is an abbreviation of `change directory`:

```bash
$ cd /home/niche/project_1
$ pwd
/home/niche/project_1
```

In this example, we changed our WD from to `home/niche/project_1` 



```bash 



### 2. Interacting with files

- `cat`: print the content of a file
- `head`: print the first few lines of a file
- `tail`: print the last few lines of a file
- `wc`: count the number of lines, words, and characters in a file
- `grep`: search for a pattern in a file

