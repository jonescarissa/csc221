# Bash Scripting

## A Simple Example

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat myscript.sh
# hfhruhfurfrehrgr

echo dhfhhfehfeihshjsfhdjhd
ls
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ls -l myscript.sh
-rw-r--r-- 1 cj917 197609 50 Feb 10 00:04 myscript.sh

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ./myscript.sh
dhfhhfehfeihshjsfhdjhd
myscript.sh  README.md
```

## Important Points

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ which bash
/usr/bin/bash

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ which ls
/usr/bin/ls

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat myscript.sh
# hfhruhfurfrehrgr

echo dhfhhfehfeihshjsfhdjhd
ls
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ echo $PATH
/c/Users/cj917/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/cj917/bin:/c/ProgramData/DockerDesktop/version-bin:/c/Program Files/Docker/Docker/Resources/bin:/c/windows/system32:/c/windows:/c/windows/System32/Wbem:/c/windows/System32/WindowsPowerShell/v1.0:/c/windows/System32/OpenSSH:/cmd:/c/Users/cj917/AppData/Local/Microsoft/WindowsApps:/c/Users/cj917/AppData/Local/Programs/Microsoft VS Code/bin:/c/Program Files/Docker Toolbox:/usr/bin/vendor_perl:/usr/bin/core_perl
```

## Variables

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat variableexample.sh
# fhruvhrvbrivbjvr
# hfhvufhvufvjfv
echo sick of this crap
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ./variableexample.sh
sick of this crap

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat morevariables.sh
# dhfrufhrofe
# dnjfnvjnvd

echo My name is $0 and I have been given $# command line arguments
echo Here they are: $*
echo And the 2nd command line argument is $2
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ./morevariables.sh trash crap sleepy
My name is ./morevariables.sh and I have been given 3 command line arguments
Here they are: trash crap sleepy
And the 2nd command line argument is crap

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat backticks.sh
# vvjrrkjgrkgjek

lines=`cat $1 | wc -l`
echo The number of lines in the file $1 is $lines
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ./backticks.sh testfile.txt
cat: testfile.txt: No such file or directory
The number of lines in the file testfile.txt is 0

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat projectbackup.sh
mkdir ~/projectbackups/$1_$date
cp -R ~/projects/$1 ~/projectbackups/$1_$date
echo Backup of $1 completed
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ ./projectbackup.sh ocelot
mkdir: cannot create directory ‘/c/Users/cj917/projectbackups/ocelot_’: No such file or directory
cp: cannot stat '/c/Users/cj917/projects/ocelot': No such file or directory
Backup of ocelot completed
```

## If Statements

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch13 (master)
$ cat projectbackup.sh
mkdir ~/projectbackups/$1_$date
cp -R ~/projects/$1 ~/projectbackups/$1_$date
echo Backup of $1 completed
```





