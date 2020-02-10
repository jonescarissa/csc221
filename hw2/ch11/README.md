# Piping and Redirection 

## Redirecting to a File

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls
barry.txt  bob_example.png  firstfile  foo1  README.md  video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls > myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls
barry.txt  bob_example.png  firstfile  foo1  myoutput  README.md  video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
barry.txt
bob_example.png
firstfile
foo1
myoutput
README.md
video.mpeg
```

### Saving to an Existing File

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
barry.txt
bob_example.png
firstfile
foo1
myoutput
README.md
video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ wc barry.txt > myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
0 0 0 barry.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls >> myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
0 0 0 barry.txt
barry.txt
bob_example.png
firstfile
foo1
myoutput
README.md
video.mpeg
```

## Redirecting from a File

```

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ wc myoutput
 8 11 87 myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ wc < myoutput
 8 11 87

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ wc < barry.txt > myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
0 0 0
```

## Redirecting STDERR

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l video.mpeg blah.foo
ls: cannot access 'blah.foo': No such file or directory
-rw-r--r-- 1 cj917 197609 0 Feb  9 23:12 video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l video.mpeg blah.foo 2> errors.txt
-rw-r--r-- 1 cj917 197609 0 Feb  9 23:12 video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat errors.txt
ls: cannot access 'blah.foo': No such file or directory

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l video.mpeg blah.foo > myoutput 2>&1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
ls: cannot access 'blah.foo': No such file or directory
-rw-r--r-- 1 cj917 197609 0 Feb  9 23:12 video.mpeg
```

## Piping

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls
barry.txt  bob_example.png  errors.txt  firstfile  foo1  myoutput  README.md  video.mpeg

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls | head -3
barry.txt
bob_example.png
errors.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls | head -3 | tail -1
errors.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls | head -3 | tail -1 > myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
errors.txt
```

## More Examples

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l /etc | tail -n +2 | sort
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 pkcs11/
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 pki/
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 ssh/
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:26 profile.d/
lrwxrwxrwx 1 cj917 197609    12 Jan 13 13:26 mtab -> /proc/mounts
-rw-r--r-- 1 cj917 197609   211 Nov  4 16:07 nsswitch.conf
-rw-r--r-- 1 cj917 197609   271 Nov  4 16:07 fstab
-rw-r--r-- 1 cj917 197609   321 Jan 13 13:26 install-options.txt
-rw-r--r-- 1 cj917 197609   355 Jan 13 13:26 gitconfig
-rw-r--r-- 1 cj917 197609   407 Mar 18  2019 networks
-rw-r--r-- 1 cj917 197609   515 Nov  8 14:08 gitattributes
-rw-r--r-- 1 cj917 197609   622 Nov  4 16:07 bash.bash_logout
-rw-r--r-- 1 cj917 197609  1358 Mar 18  2019 protocols
-rw-r--r-- 1 cj917 197609  1744 Nov  4 16:07 docx2txt.config
-rw-r--r-- 1 cj917 197609  1826 Nov  4 16:07 msystem
-rw-r--r-- 1 cj917 197609  2413 Dec 13 17:58 hosts
-rw-r--r-- 1 cj917 197609  2488 Nov  4 16:07 bash.bashrc
-rw-r--r-- 1 cj917 197609  2710 Nov 29 19:30 inputrc
-rw-r--r-- 1 cj917 197609  2904 Nov 29 19:30 vimrc
-rw-r--r-- 1 cj917 197609  3651 Dec  7 20:09 package-versions.txt
-rw-r--r-- 1 cj917 197609  4339 Nov  4 16:07 DIR_COLORS
-rw-r--r-- 1 cj917 197609  6675 Nov  4 16:07 profile
-rw-r--r-- 1 cj917 197609 10434 Nov  4 16:07 nanorc
-rw-r--r-- 1 cj917 197609 17635 Mar 18  2019 services
-rw-r--r-- 1 cj917 197609 17683 Nov 21 13:52 tigrc

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l /etc | less

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l ~ | grep '^.....w'
lrwxrwxrwx 1 cj917 197609      30 Sep 20 18:42 Application Data -> /c/Users/cj917/AppData/Roaming/
lrwxrwxrwx 1 cj917 197609      58 Sep 20 18:42 Cookies -> /c/Users/cj917/AppData/Local/Microsoft/Windows/INetCookies/
lrwxrwxrwx 1 cj917 197609      28 Sep 20 18:42 Local Settings -> /c/Users/cj917/AppData/Local/
lrwxrwxrwx 1 cj917 197609      24 Sep 20 18:42 My Documents -> /c/Users/cj917/Documents/
lrwxrwxrwx 1 cj917 197609      66 Sep 20 18:42 NetHood -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Network Shortcuts/
lrwxrwxrwx 1 cj917 197609      66 Sep 20 18:42 PrintHood -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Printer Shortcuts/
lrwxrwxrwx 1 cj917 197609      55 Sep 20 18:42 Recent -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Recent/
lrwxrwxrwx 1 cj917 197609      55 Sep 20 18:42 SendTo -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/SendTo/
lrwxrwxrwx 1 cj917 197609      59 Sep 20 18:42 Start Menu -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Start Menu/
lrwxrwxrwx 1 cj917 197609      58 Sep 20 18:42 Templates -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Templates/

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls -l /projects/ghosttrail | tail -n +2 | sed 's/\s\s*/ /g' | cut -d ' ' -f 3 | sort | uniq -c
ls: cannot access '/projects/ghosttrail': No such file or directory
```

## Actvity 11

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ wc firstfile > myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
0 0 0 firstfile

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ ls >> myoutput

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch11 (master)
$ cat myoutput
0 0 0 firstfile
barry.txt
bob_example.png
errors.txt
firstfile
foo1
myoutput
q
README.md
video.mpeg

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls -l /etc | tail -20
-rw-r--r-- 1 cj917 197609   515 Nov  8 14:08 gitattributes
-rw-r--r-- 1 cj917 197609   355 Jan 13 13:26 gitconfig
-rw-r--r-- 1 cj917 197609  2413 Dec 13 17:58 hosts
-rw-r--r-- 1 cj917 197609  2710 Nov 29 19:30 inputrc
-rw-r--r-- 1 cj917 197609   321 Jan 13 13:26 install-options.txt
-rw-r--r-- 1 cj917 197609  1826 Nov  4 16:07 msystem
lrwxrwxrwx 1 cj917 197609    12 Jan 13 13:26 mtab -> /proc/mounts
-rw-r--r-- 1 cj917 197609 10434 Nov  4 16:07 nanorc
-rw-r--r-- 1 cj917 197609   407 Mar 18  2019 networks
-rw-r--r-- 1 cj917 197609   211 Nov  4 16:07 nsswitch.conf
-rw-r--r-- 1 cj917 197609  3651 Dec  7 20:09 package-versions.txt
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 pkcs11/
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 pki/
-rw-r--r-- 1 cj917 197609  6675 Nov  4 16:07 profile
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:26 profile.d/
-rw-r--r-- 1 cj917 197609  1358 Mar 18  2019 protocols
-rw-r--r-- 1 cj917 197609 17635 Mar 18  2019 services
drwxr-xr-x 1 cj917 197609     0 Jan 13 13:25 ssh/
-rw-r--r-- 1 cj917 197609 17683 Nov 21 13:52 tigrc
-rw-r--r-- 1 cj917 197609  2904 Nov 29 19:30 vimrc
```





