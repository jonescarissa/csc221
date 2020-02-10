# Permissions

## View Permissions

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png
```

## Change Permissions

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod g+x frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod u-w frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-r--r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-r--r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod g+wx frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod go-x frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png
```

## Setting Permissions Shorthand

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod 751 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod 240 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png
```

## Permissions for Directories

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ ls
file1  file2  file3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ cd ..

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ chmod 400 testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ ls -ld testdir
drwxr-xr-x 1 cj917 197609 0 Feb  9 21:49 testdir/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ cd testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ ls
file1  file2  file3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ cd ..

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ chmod 100 testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ ls -ld testdir
drwxr-xr-x 1 cj917 197609 0 Feb  9 21:49 testdir/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ ls testdir
file1  file2  file3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ cd testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch8/testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ ls -ld testdir
drwxr-xr-x 1 cj917 197609 0 Feb  9 21:54 testdir/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8 (master)
$ cd testdir

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ ls
file1  file2  file3  samplefile.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/testdir (master)
$ cat samplefile.txt
Kyle 20
Stan 11
Kenny 37
```

## Actvity 1

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls -l Documents
total 0
drwxr-xr-x 1 cj917 197609  0 Sep 23 10:05  belhavencs/
drwxr-xr-x 1 cj917 197609  0 Jan 27 19:57  courses/
lrwxrwxrwx 1 cj917 197609 20 Sep 20 18:42 'My Music' -> /c/Users/cj917/Music/
lrwxrwxrwx 1 cj917 197609 23 Sep 20 18:42 'My Pictures' -> /c/Users/cj917/Pictures
lrwxrwxrwx 1 cj917 197609 21 Sep 20 18:42 'My Videos' -> /c/Users/cj917/Videos/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls
foo3/  fred/  frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod o+x frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod 755 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ ls -l frog.png
-rw-r--r-- 1 cj917 197609 0 Feb  9 21:38 frog.png

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch8/linuxtutorialwork (master)
$ chmod u-r frog.png
```

