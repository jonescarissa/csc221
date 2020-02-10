# Wildcards

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ pwd
/c/Users/cj917

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls
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

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls n*
ntuser.dat.LOG1  ntuser.dat.LOG2  ntuser.ini
```

## Some More Examples

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls *.DAT
NTUSER.DAT

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ?i*
Links:
desktop.ini  Desktop.lnk*  Downloads.lnk*

MicrosoftEdgeBackups:
backups/

Videos:
Captures/  desktop.ini

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls *.???
NTUSER.DAT  NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TM.blf  ntuser.ini

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls [cd]*
birthday2019/  cheers2019/  README.md  summer2019/

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls *[0-9]*
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TM.blf
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000002.regtrans-ms

'3D Objects':
desktop.ini

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls [^a-k]*
'Local Settings'@
'My Documents'@
 NetHood@
 NTUSER.DAT
 ntuser.dat.LOG1
 ntuser.dat.LOG2
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TM.blf
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000001.regtrans-ms
 NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000002.regtrans-ms
 ntuser.ini
 PrintHood@
 Recent@
 SendTo@
'Start Menu'@
 Templates@

'3D Objects':
desktop.ini

Links:
desktop.ini  Desktop.lnk*  Downloads.lnk*

MicrosoftEdgeBackups:
backups/

Music:
desktop.ini

OneDrive:
 Attachments/   desktop.ini  'Personal Vault.lnk'*   Public/
 Desktop/       Documents/    Pictures/              Videos/

'Saved Games':
desktop.ini

Searches:
 desktop.ini
 Everywhere.search-ms
'Indexed Locations.search-ms'
 winrt--{S-1-5-21-1241693658-2769261382-3671258428-1001}-.searchconnector-ms

Videos:
Captures/  desktop.ini
```

## Some Real World Examples

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ file ~/Documents/*
/c/Users/cj917/Documents/belhavencs:  directory
/c/Users/cj917/Documents/courses:     directory
/c/Users/cj917/Documents/My Music:    symbolic link to /c/Users/cj917/Music
/c/Users/cj917/Documents/My Pictures: broken symbolic link to /c/Users/cj917/Pictures
/c/Users/cj917/Documents/My Videos:   symbolic link to /c/Users/cj917/Videos

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls Music
desktop.ini

cj917@DESKTOP-381J2GT MINGW64 ~
$ mv Music/*.??i Videos

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls -lh ~/*/Documents
total 194K
drwxr-xr-x 1 cj917 197609   0 Jan 13 13:30  belhavencs/
-rw-r--r-- 1 cj917 197609 17K Dec  5 22:15 'CA worldview paper-DESKTOP-381J2GT.docx'
-r--r--r-- 1 cj917 197609 120 Nov 12 14:57 "Carissa's Notebook.url"
drwxr-xr-x 1 cj917 197609   0 Sep 28 23:57 'Custom Office Templates'/
-rw-r--r-- 1 cj917 197609 402 Dec 11 13:18  desktop.ini
drwxr-xr-x 1 cj917 197609   0 Dec 18 21:40  Downloads/
drwxr-xr-x 1 cj917 197609   0 Dec  9 22:45 'Electronic Arts'/
-rw-r--r-- 1 cj917 197609 16K Oct 15  2018 'Essay #2.docx'
-rw-r--r-- 1 cj917 197609 38K Dec  4 16:46 'Study Guide, Final Exam, Western Civ I, 2019.docx'
-rw-r--r-- 1 cj917 197609 32K Nov 14 17:44 'Synthetic Paper.docx'
-rw-r--r-- 1 cj917 197609 42K Nov  6 17:17 'Thought Questions (1).docx'
-rw-r--r-- 1 cj917 197609 33K Jan 31 16:01 'Trig Chapter 7 Review.pdf'
-rw-r--r-- 1 cj917 197609 20K Dec  5 22:16 'Worldview project.docx'
drwxr-xr-x 1 cj917 197609   0 Sep 20 21:47  YouCam/
```

## Actvity 1

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /etc

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls
bash.bash_logout  gitattributes        msystem        package-versions.txt  protocols
bash.bashrc       gitconfig            mtab@          pkcs11/               services
DIR_COLORS        hosts                nanorc         pki/                  ssh/
docx2txt.config   inputrc              networks       profile               tigrc
fstab             install-options.txt  nsswitch.conf  profile.d/            vimrc

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls b*
bash.bash_logout  bash.bashrc

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls D*
DIR_COLORS

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls *.txt
install-options.txt  package-versions.txt

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls *.???
install-options.txt  package-versions.txt

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls *.????
nsswitch.conf
```



