# More About Files

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ file Documents/mymusic
Documents/mymusic: cannot open `Documents/mymusic' (No such file or directory)
```

## Spaces in Names

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd MyMusic
bash: cd: MyMusic: No such file or directory
```

### Quotes

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ cd 'My Music'

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/My Music
$ pwd
/c/Users/cj917/Documents/My Music
```

### Escape Characters

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ cd My\ Music

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/My Music
$ pwd
/c/Users/cj917/Documents/My Music
```

## Hidden Files and Directories

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls -a Documents
 ./   ../   belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@
```

## Activity 1

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ file Music
Music: directory

cj917@DESKTOP-381J2GT MINGW64 ~
$ file /etc
/etc: directory

cj917@DESKTOP-381J2GT MINGW64 ~
$ file OneDrive
OneDrive: directory

cj917@DESKTOP-381J2GT MINGW64 ~
$ file OneDrive/Documents
OneDrive/Documents: directory
```

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls -a
 ./
 ../
 .bash_history
 .docker/
 .gitconfig
 .lesshst
 .minttyrc
 .Origin/
 .QtWebEngineProcess/
 .ssh/
 .viminfo
 .VirtualBox/
 .vscode/
'3D Objects'/
 AppData/
'Application Data'@
 Contacts/
 Cookies@
 Documents/
 doodle/
 Downloads/
 Favorites/
 IntelGraphicsProfiles/
 Links/
'Local Settings'@
 MicrosoftEdgeBackups/
 Music/
'My Documents'@
 NetHood@
 NTUSER.DAT
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TM.blf
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000002.regtrans-ms
 ntuser.ini
 OneDrive/
 PrintHood@
 Recent@
'Saved Games'/
 Searches/
 SendTo@
'Start Menu'@
 Templates@
 Videos/
```