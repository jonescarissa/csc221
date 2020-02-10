# File Manipulation

## Making a Directory

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch5

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ ls
README.md

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir linuxtutorialwork

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ ls
linuxtutorialwork/  README.md

```

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir -p linuxtutorialwork/foo/bar

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ cd linuxtutorialwork/foo/bar

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork/foo/bar (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch5/linuxtutorialwork/foo/bar
```

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir -pv linuxtutorialwork/foo/bar

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ cd linuxtutorialwork/foo/bar

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork/foo/bar (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch5/linuxtutorialwork/foo/bar
```

## Removing a Directory

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ rmdir linuxtutorialwork/foo/bar

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ ls linuxtutorialwork/foo

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$
```

## Creating a Blank File

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch5/linuxtutorialwork

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
foo/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ touch example1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
example1  foo/
```

## Copying a File or Directory

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
example1  foo/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ cp example1 barney

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
barney  example1  foo/
```

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
barney  example1  foo/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ cp foo foo2
cp: -r not specified; omitting directory 'foo'

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ cp -r foo foo2

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
barney  example1  foo/  foo2/
```

## Moving a File or Directory

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
barney  example1  foo/  foo2/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ mkdir backups

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ mv foo2 backups/foo3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ mv barney backups/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  example1  foo/
```

### Renaming Files and Directories

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  example1  foo/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ mv foo foo3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  example1  foo3/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ cd ..

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir linuxtutorialwork/testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mv linuxtutorialwork/testdir ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork/fred

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ ls linuxtutorialwork
backups/  example1  foo3/  fred/
```

## Removing a File

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  example1  foo3/  fred/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ rm example1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  foo3/  fred/
```

### Removing non empty Directories

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
backups/  foo3/  fred/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ rmdir backups
rmdir: failed to remove 'backups': Directory not empty

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ rm backups
rm: cannot remove 'backups': Is a directory

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ rm -r backups

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/linuxtutorialwork (master)
$ ls
foo3/  fred/
```

## Actvity 1

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir actvity1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ ls
actvity1/  linuxtutorialwork/  README.md

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ cd actvity1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1 (master)
$ cd ..

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ mkdir -p actvity1/caesar/augustus

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5 (master)
$ cd actvity1/caesar/augustus

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ touch roman1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ ls
roman1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ touch roman2

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ touch roman3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ cp roman2 soldiers

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ la
bash: la: command not found

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch5/actvity1/caesar/augustus (master)
$ ls
roman1  roman2  roman3  soldiers
```


