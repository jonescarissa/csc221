# Manual Pages

"For manual pages to work, I had to use Powershell instead of Git Bash"""

```
PS C:\Users\cj917> man ls

NAME
    Get-ChildItem

SYNTAX
    Get-ChildItem [[-Path] <string[]>] [[-Filter] <string>] [-Include <string[]>] [-Exclude <string[]>] [-Recurse]
    [-Depth <uint32>] [-Force] [-Name] [-UseTransaction] [-Attributes {ReadOnly | Hidden | System | Directory |
    Archive | Device | Normal | Temporary | SparseFile | ReparsePoint | Compressed | Offline | NotContentIndexed |
    Encrypted | IntegrityStream | NoScrubData}] [-Directory] [-File] [-Hidden] [-ReadOnly] [-System]
    [<CommonParameters>]

    Get-ChildItem [[-Filter] <string>] -LiteralPath <string[]> [-Include <string[]>] [-Exclude <string[]>] [-Recurse]
    [-Depth <uint32>] [-Force] [-Name] [-UseTransaction] [-Attributes {ReadOnly | Hidden | System | Directory |
    Archive | Device | Normal | Temporary | SparseFile | ReparsePoint | Compressed | Offline | NotContentIndexed |
    Encrypted | IntegrityStream | NoScrubData}] [-Directory] [-File] [-Hidden] [-ReadOnly] [-System]
    [<CommonParameters>]


ALIASES
    gci
    ls
    dir


REMARKS
    Get-Help cannot find the Help files for this cmdlet on this computer. It is displaying only partial help.
        -- To download and install Help files for the module that includes this cmdlet, use Update-Help.
        -- To view the Help topic for this cmdlet online, type: "Get-Help Get-ChildItem -Online" or
           go to https://go.microsoft.com/fwlink/?LinkID=113308.

```

## More on the Running of Commands

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ pwd
/c/Users/cj917

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

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls --all
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

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls -alh
total 8.4M
drwxr-xr-x 1 cj917 197609    0 Feb  8 08:36  ./
drwxr-xr-x 1 cj917 197609    0 Sep 20 19:06  ../
-rw-r--r-- 1 cj917 197609 7.4K Feb  8 18:29  .bash_history
drwxr-xr-x 1 cj917 197609    0 Sep 22 21:15  .docker/
-rw-r--r-- 1 cj917 197609   73 Sep 27 12:21  .gitconfig
-rw-r--r-- 1 cj917 197609   46 Feb  5 10:39  .lesshst
-rw-r--r-- 1 cj917 197609   44 Feb  8 08:45  .minttyrc
drwxr-xr-x 1 cj917 197609    0 Dec  9 15:43  .Origin/
drwxr-xr-x 1 cj917 197609    0 Dec  9 15:43  .QtWebEngineProcess/
drwxr-xr-x 1 cj917 197609    0 Jan 13 13:49  .ssh/
-rw-r--r-- 1 cj917 197609  14K Feb  8 08:36  .viminfo
drwxr-xr-x 1 cj917 197609    0 Sep 22 21:36  .VirtualBox/
drwxr-xr-x 1 cj917 197609    0 Nov 10 13:32  .vscode/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18 '3D Objects'/
drwxr-xr-x 1 cj917 197609    0 Sep 22 21:08  AppData/
lrwxrwxrwx 1 cj917 197609   30 Sep 20 18:42 'Application Data' -> /c/Users/cj917/AppData/Roaming/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Contacts/
lrwxrwxrwx 1 cj917 197609   58 Sep 20 18:42  Cookies -> /c/Users/cj917/AppData/Local/Microsoft/Windows/INetCookies/
drwxr-xr-x 1 cj917 197609    0 Jan 27 20:01  Documents/
drwxr-xr-x 1 cj917 197609    0 Sep 22 20:44  doodle/
drwxr-xr-x 1 cj917 197609    0 Jan 31 16:01  Downloads/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Favorites/
drwxr-xr-x 1 cj917 197609    0 Feb  2 03:16  IntelGraphicsProfiles/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Links/
lrwxrwxrwx 1 cj917 197609   28 Sep 20 18:42 'Local Settings' -> /c/Users/cj917/AppData/Local/
drwxr-xr-x 1 cj917 197609    0 Sep 20 18:48  MicrosoftEdgeBackups/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Music/
lrwxrwxrwx 1 cj917 197609   24 Sep 20 18:42 'My Documents' -> /c/Users/cj917/Documents/
lrwxrwxrwx 1 cj917 197609   66 Sep 20 18:42  NetHood -> '/c/Users/cj917/AppData/Roaming/Microsoft/Windows/Network Shortcuts'/
-rw-r--r-- 1 cj917 197609 5.3M Feb  2 03:15  NTUSER.DAT
-rw-r--r-- 1 cj917 197609 640K Sep 20 18:42  ntuser.dat.LOG1
-rw-r--r-- 1 cj917 197609 1.4M Sep 20 18:42  ntuser.dat.LOG2
-rw-r--r-- 1 cj917 197609  64K Sep 22 14:47  NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TM.blf
-rw-r--r-- 1 cj917 197609 512K Sep 22 14:47  NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000001.regtrans-ms
-rw-r--r-- 1 cj917 197609 512K Sep 20 18:42  NTUSER.DAT{c4bbd6eb-9877-11e9-8e69-00155df78518}.TMContainer00000000000000000002.regtrans-ms
-rw-r--r-- 1 cj917 197609   20 Sep 20 18:42  ntuser.ini
drwxr-xr-x 1 cj917 197609    0 Feb  8 13:16  OneDrive/
lrwxrwxrwx 1 cj917 197609   66 Sep 20 18:42  PrintHood -> '/c/Users/cj917/AppData/Roaming/Microsoft/Windows/Printer Shortcuts'/
lrwxrwxrwx 1 cj917 197609   55 Sep 20 18:42  Recent -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Recent/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18 'Saved Games'/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Searches/
lrwxrwxrwx 1 cj917 197609   55 Sep 20 18:42  SendTo -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/SendTo/
lrwxrwxrwx 1 cj917 197609   59 Sep 20 18:42 'Start Menu' -> '/c/Users/cj917/AppData/Roaming/Microsoft/Windows/Start Menu'/
lrwxrwxrwx 1 cj917 197609   58 Sep 20 18:42  Templates -> /c/Users/cj917/AppData/Roaming/Microsoft/Windows/Templates/
drwxr-xr-x 1 cj917 197609    0 Dec 11 13:18  Videos/
```
## Actvity 1

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ man ls
bash: man: command not found

cj917@DESKTOP-381J2GT MINGW64 ~
$ man cat
bash: man: command not found
```

