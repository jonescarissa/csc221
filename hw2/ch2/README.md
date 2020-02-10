# Chapter 2: Navigation

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch2 (master)
$ pwd
/c/Users/cj917/Documents/courses/csc221/hw2/ch2
```

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch2 (master)
$ ls
README.md
```

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch2 (master)
$ ls -l
total 1
-rw-r--r-- 1 cj917 197609 278 Feb  7 10:29 README.md

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch2 (master)
$ ls /etc
bash.bash_logout  gitattributes        msystem        package-versions.txt  protocols
bash.bashrc       gitconfig            mtab@          pkcs11/               services
DIR_COLORS        hosts                nanorc         pki/                  ssh/
docx2txt.config   inputrc              networks       profile               tigrc
fstab             install-options.txt  nsswitch.conf  profile.d/            vimrc

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch2 (master)
$ ls -l /etc
total 98
-rw-r--r-- 1 cj917 197609   622 Nov  4 16:07 bash.bash_logout
-rw-r--r-- 1 cj917 197609  2488 Nov  4 16:07 bash.bashrc
-rw-r--r-- 1 cj917 197609  4339 Nov  4 16:07 DIR_COLORS
-rw-r--r-- 1 cj917 197609  1744 Nov  4 16:07 docx2txt.config
-rw-r--r-- 1 cj917 197609   271 Nov  4 16:07 fstab
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

## Paths
```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ls Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ~/Documents/courses/csc221
hw1/  hw2/  LICENSE  README.md
```

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ pwd
/c/Users/cj917

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ~/Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ./Documents
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ~/Documents/courses/csc221
hw1/  hw2/  LICENSE  README.md

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls ../../
'$RECYCLE.BIN'/             pagefile.sys           'System Volume Information'/
'Documents and Settings'@  'Program Files'/         Users/
 emacs/                    'Program Files (x86)'/   Windows/
 hiberfil.sys               ProgramData/            windows-version.txt
 Intel/                     Recovery/
 OneDriveTemp/              swapfile.sys

cj917@DESKTOP-381J2GT MINGW64 ~
$ ls /
bin/  dev/  git-bash.exe*  LICENSE.txt  proc/              tmp/          unins001.exe*  usr/
cmd/  etc/  git-cmd.exe*   mingw64/     ReleaseNotes.html  unins001.dat  unins001.msg

```

## Working with cd

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ pwd
/c/Users/cj917

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd Documents

cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ ls
 belhavencs/   courses/  'My Music'@  'My Pictures'@  'My Videos'@

cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ cd /

cj917@DESKTOP-381J2GT MINGW64 /
$ pwd
/

cj917@DESKTOP-381J2GT MINGW64 /
$ ls
bin/  dev/  git-bash.exe*  LICENSE.txt  proc/              tmp/          unins001.exe*  usr/
cmd/  etc/  git-cmd.exe*   mingw64/     ReleaseNotes.html  unins001.dat  unins001.msg

cj917@DESKTOP-381J2GT MINGW64 /
$ cd ~/Documents

cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ pwd
/c/Users/cj917/Documents

cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ cd ../../

cj917@DESKTOP-381J2GT MINGW64 /c/Users
$ pwd
/c/Users

cj917@DESKTOP-381J2GT MINGW64 /c/Users
$ cd

cj917@DESKTOP-381J2GT MINGW64 ~
$ pwd
/c/Users/cj917
```

## Activity 1
```
cj917@DESKTOP-381J2GT MINGW64 /
$ cd /etc

cj917@DESKTOP-381J2GT MINGW64 /etc
$ ls
bash.bash_logout  gitattributes        msystem        package-versions.txt  protocols
bash.bashrc       gitconfig            mtab@          pkcs11/               services
DIR_COLORS        hosts                nanorc         pki/                  ssh/
docx2txt.config   inputrc              networks       profile               tigrc
fstab             install-options.txt  nsswitch.conf  profile.d/            vimrc

cj917@DESKTOP-381J2GT MINGW64 /etc
$ cd ../

cj917@DESKTOP-381J2GT MINGW64 /
$ cd /var/log
bash: cd: /var/log: No such file or directory

cj917@DESKTOP-381J2GT MINGW64 /
$ cd ~

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /var/log
bash: cd: /var/log: No such file or directory

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /bin

cj917@DESKTOP-381J2GT MINGW64 /bin
$ ls
'[.exe'*                      locate.exe*                     nohup.exe*
 addgnupghome*                logname.exe*                    notepad*
 applygnupgdefaults*          ls.exe*                         nproc.exe*
 arch.exe*                    lsattr.exe*                     numfmt.exe*
 astextplain*                 mac2unix.exe*                   od.exe*
 autopoint*                   md5sum.exe*                     openssl.exe*
 awk.exe*                     minidumper.exe*                 p11-kit.exe*
 b2sum.exe*                   mintheme*                       passwd.exe*
 backup*                      mintty.exe*                     paste.exe*
 base32.exe*                  mkdir.exe*                      patch.exe*
 base64.exe*                  mkfifo.exe*                     pathchk.exe*
 basename.exe*                mkgroup.exe*                    perl.exe*
 basenc.exe*                  mknod.exe*                      perl5.26.2.exe*
 bash.exe*                    mkpasswd.exe*                   pinentry.exe*
 bashbug*                     mktemp.exe*                     pinentry-w32.exe*
 bunzip2.exe*                 mount.exe*                      pinky.exe*
 bzcat.exe*                   mpicalc.exe*                    pkcs1-conv.exe*
 bzcmp*                       msgattrib.exe*                  pldd.exe*
 bzdiff*                      msgcat.exe*                     pluginviewer.exe*
 bzegrep*                     msgcmp.exe*                     pr.exe*
 bzfgrep*                     msgcomm.exe*                    printenv.exe*
 bzgrep*                      msgconv.exe*                    printf.exe*
 bzip2.exe*                   msgen.exe*                      ps.exe*
 bzip2recover.exe*            msgexec.exe*                    psl.exe*
 bzless*                      msgfilter.exe*                  psl-make-dafsa*
 bzmore*                      msgfmt.exe*                     ptx.exe*
 c_rehash*                    msggrep.exe*                    pwd.exe*
 captoinfo.exe*               msginit.exe*                    readlink.exe*
 cat.exe*                     msgmerge.exe*                   realpath.exe*
 chattr.exe*                  msgunfmt.exe*                   rebase.exe*
 chcon.exe*                   msguniq.exe*                    rebaseall*
 chgrp.exe*                   msys-2.0.dll*                   recode-sr-latin.exe*
 chmod.exe*                   msys-apr-1-0.dll*               regtool.exe*
 chown.exe*                   msys-aprutil-1-0.dll*           reset.exe*
 chroot.exe*                  msys-asn1-8.dll*                restore*
 cksum.exe*                   msys-asprintf-0.dll*            rm.exe*
 clear.exe*                   msys-assuan-0.dll*              rmdir.exe*
 cmp.exe*                     msys-atomic-1.dll*              rnano.exe*
 column.exe*                  msys-blkid-1.dll*               runcon.exe*
 comm.exe*                    msys-bz2-1.dll*                 rview.exe*
 core_perl/                   msys-charset-1.dll*             rvim.exe*
 cp.exe*                      msys-com_err-1.dll*             sasldblistusers2.exe*
 csplit.exe*                  msys-crypt-0.dll*               saslpasswd2.exe*
 cut.exe*                     msys-crypto-1.0.0.dll*          scp.exe*
 cygcheck.exe*                msys-crypto-1.1.dll*            sdiff.exe*
 cygpath.exe*                 msys-curl-4.dll*                sed.exe*
 cygwin-console-helper.exe*   msys-edit-0.dll*                seq.exe*
 d2u.exe*                     msys-expat-1.dll*               setfacl.exe*
 dash.exe*                    msys-exslt-0.dll*               setmetamode.exe*
 date.exe*                    msys-fdisk-1.dll*               sexp-conv.exe*
 dd.exe*                      msys-ffi-6.dll*                 sftp.exe*
 df.exe*                      msys-formw6.dll*                sh.exe*
 diff.exe*                    msys-gcc_s-seh-1.dll*           sha1sum.exe*
 diff3.exe*                   msys-gcrypt-20.dll*             sha224sum.exe*
 dir.exe*                     msys-gettextlib-0-19-8-1.dll*   sha256sum.exe*
 dircolors.exe*               msys-gettextpo-0.dll*           sha384sum.exe*
 dirmngr.exe*                 msys-gettextsrc-0-19-8-1.dll*   sha512sum.exe*
 dirmngr-client.exe*          msys-gio-2.0-0.dll*             shred.exe*
 dirname.exe*                 msys-glib-2.0-0.dll*            shuf.exe*
 docx2txt*                    msys-gmodule-2.0-0.dll*         sleep.exe*
 docx2txt.pl*                 msys-gmp-10.dll*                sort.exe*
 dos2unix.exe*                msys-gmpxx-4.dll*               split.exe*
 du.exe*                      msys-gnutls-30.dll*             ssh.exe*
 dumpsexp.exe*                msys-gnutlsxx-28.dll*           ssh-add.exe*
 echo.exe*                    msys-gobject-2.0-0.dll*         ssh-agent.exe*
 egrep*                       msys-gomp-1.dll*                ssh-copy-id*
 env.exe*                     msys-gpg-error-0.dll*           sshd.exe*
 envsubst.exe*                msys-gssapi-3.dll*              ssh-keygen.exe*
 ex.exe*                      msys-gthread-2.0-0.dll*         ssh-keyscan.exe*
 expand.exe*                  msys-hcrypto-4.dll*             ssh-pageant.exe*
 expr.exe*                    msys-hdb-9.dll*                 ssp.exe*
 factor.exe*                  msys-heimbase-1.dll*            start*
 false.exe*                   msys-heimntlm-0.dll*            stat.exe*
 fgrep*                       msys-history8.dll*              strace.exe*
 file.exe*                    msys-hogweed-5.dll*             stty.exe*
 find.exe*                    msys-hx509-5.dll*               sum.exe*
 findssl.sh*                  msys-iconv-2.dll*               sync.exe*
 fmt.exe*                     msys-idn2-0.dll*                tabs.exe*
 fold.exe*                    msys-intl-8.dll*                tac.exe*
 funzip.exe*                  msys-kadm5clnt-7.dll*           tail.exe*
 gapplication.exe*            msys-kadm5srv-8.dll*            tar.exe*
 gawk.exe*                    msys-kafs-0.dll*                tee.exe*
 gawk-5.0.0.exe*              msys-kdc-2.dll*                 test.exe*
 gdbus.exe*                   msys-krb5-26.dll*               tic.exe*
 gencat.exe*                  msys-ksba-8.dll*                tig.exe*
 getconf.exe*                 msys-lzma-5.dll*                timeout.exe*
 getemojis*                   msys-magic-1.dll*               toe.exe*
 getfacl.exe*                 msys-menuw6.dll*                touch.exe*
 getopt.exe*                  msys-metalink-3.dll*            tput.exe*
 gettext.exe*                 msys-mpfr-6.dll*                tr.exe*
 gettext.sh*                  msys-ncurses++w6.dll*           true.exe*
 gettextize*                  msys-ncursesw6.dll*             truncate.exe*
 gio-querymodules.exe*        msys-nettle-7.dll*              trust.exe*
 git-flow*                    msys-nghttp2-14.dll*            tset.exe*
 git-flow-bugfix              msys-npth-0.dll*                tsort.exe*
 gitflow-common               msys-p11-kit-0.dll*             tty.exe*
 git-flow-config              msys-panelw6.dll*               tzset.exe*
 git-flow-feature             msys-pcre-1.dll*                u2d.exe*
 git-flow-hotfix              msys-pcre2-8-0.dll*             umount.exe*
 git-flow-init                msys-perl5_26.dll*              uname.exe*
 git-flow-log                 msys-psl-5.dll*                 uncompress*
 git-flow-release             msys-readline7.dll*             unexpand.exe*
 gitflow-shFlags              msys-readline8.dll*             uniq.exe*
 git-flow-support             msys-roken-18.dll*              unix2dos.exe*
 git-flow-version             msys-sasl2-3.dll*               unix2mac.exe*
 gkill.exe*                   msys-serf-1-0.dll*              unlink.exe*
 glib-compile-schemas.exe*    msys-sl-0.dll*                  unzip.exe*
 gobject-query.exe*           msys-smartcols-1.dll*           unzipsfx.exe*
 gpg.exe*                     msys-sqlite3-0.dll*             update-ca-trust*
 gpg-agent.exe*               msys-ssh2-1.dll*                updatedb*
 gpgconf.exe*                 msys-ssl-1.0.0.dll*             users.exe*
 gpg-connect-agent.exe*       msys-ssl-1.1.dll*               vdir.exe*
 gpg-error.exe*               msys-svn_client-1-0.dll*        vendor_perl/
 gpgparsemail.exe*            msys-svn_delta-1-0.dll*         vi*
 gpgscm.exe*                  msys-svn_diff-1-0.dll*          view.exe*
 gpgsm.exe*                   msys-svn_fs_fs-1-0.dll*         vim.exe*
 gpgtar.exe*                  msys-svn_fs_util-1-0.dll*       vimdiff.exe*
 gpgv.exe*                    msys-svn_fs_x-1-0.dll*          vimtutor*
 gpg-wks-server.exe*          msys-svn_fs-1-0.dll*            watchgnupg.exe*
 grep.exe*                    msys-svn_ra_local-1-0.dll*      wc.exe*
 groups.exe*                  msys-svn_ra_serf-1-0.dll*       which.exe*
 gsettings.exe*               msys-svn_ra_svn-1-0.dll*        who.exe*
 gunzip*                      msys-svn_ra-1-0.dll*            whoami.exe*
 gzexe*                       msys-svn_repos-1-0.dll*         winpty.dll*
 gzip.exe*                    msys-svn_subr-1-0.dll*          winpty.exe*
 head.exe*                    msys-svn_swig_perl-1-0.dll*     winpty-agent.exe*
 hmac256.exe*                 msys-svn_swig_py-1-0.dll*       winpty-debugserver.exe*
 hostid.exe*                  msys-svn_swig_ruby-1-0.dll*     wordpad*
 hostname.exe*                msys-svn_wc-1-0.dll*            xargs.exe*
 iconv.exe*                   msys-tasn1-6.dll*               xgettext.exe*
 id.exe*                      msys-ticw6.dll*                 xxd.exe*
 infocmp.exe*                 msys-unistring-2.dll*           yat2m.exe*
 infotocap.exe*               msys-uuid-1.dll*                yes.exe*
 install.exe*                 msys-wind-0.dll*                zcat*
 join.exe*                    msys-xml2-2.dll*                zcmp*
 kbxutil.exe*                 msys-xslt-1.dll*                zdiff*
 kill.exe*                    msys-z.dll*                     zegrep*
 ldd.exe*                     mv.exe*                         zfgrep*
 ldh.exe*                     nano.exe*                       zforce*
 less.exe*                    nettle-hash.exe*                zgrep*
 lessecho.exe*                nettle-lfib-stream.exe*         zipgrep*
 lesskey.exe*                 nettle-pbkdf2.exe*              zipinfo.exe*
 link.exe*                    ngettext.exe*                   zless*
 ln.exe*                      nice.exe*                       zmore*
 locale.exe*                  nl.exe*                         znew*

cj917@DESKTOP-381J2GT MINGW64 /bin
$ cd ../

cj917@DESKTOP-381J2GT MINGW64 /
$ cd /usr/bin

cj917@DESKTOP-381J2GT MINGW64 /usr/bin
$ ls
'[.exe'*                      locate.exe*                     nohup.exe*
 addgnupghome*                logname.exe*                    notepad*
 applygnupgdefaults*          ls.exe*                         nproc.exe*
 arch.exe*                    lsattr.exe*                     numfmt.exe*
 astextplain*                 mac2unix.exe*                   od.exe*
 autopoint*                   md5sum.exe*                     openssl.exe*
 awk.exe*                     minidumper.exe*                 p11-kit.exe*
 b2sum.exe*                   mintheme*                       passwd.exe*
 backup*                      mintty.exe*                     paste.exe*
 base32.exe*                  mkdir.exe*                      patch.exe*
 base64.exe*                  mkfifo.exe*                     pathchk.exe*
 basename.exe*                mkgroup.exe*                    perl.exe*
 basenc.exe*                  mknod.exe*                      perl5.26.2.exe*
 bash.exe*                    mkpasswd.exe*                   pinentry.exe*
 bashbug*                     mktemp.exe*                     pinentry-w32.exe*
 bunzip2.exe*                 mount.exe*                      pinky.exe*
 bzcat.exe*                   mpicalc.exe*                    pkcs1-conv.exe*
 bzcmp*                       msgattrib.exe*                  pldd.exe*
 bzdiff*                      msgcat.exe*                     pluginviewer.exe*
 bzegrep*                     msgcmp.exe*                     pr.exe*
 bzfgrep*                     msgcomm.exe*                    printenv.exe*
 bzgrep*                      msgconv.exe*                    printf.exe*
 bzip2.exe*                   msgen.exe*                      ps.exe*
 bzip2recover.exe*            msgexec.exe*                    psl.exe*
 bzless*                      msgfilter.exe*                  psl-make-dafsa*
 bzmore*                      msgfmt.exe*                     ptx.exe*
 c_rehash*                    msggrep.exe*                    pwd.exe*
 captoinfo.exe*               msginit.exe*                    readlink.exe*
 cat.exe*                     msgmerge.exe*                   realpath.exe*
 chattr.exe*                  msgunfmt.exe*                   rebase.exe*
 chcon.exe*                   msguniq.exe*                    rebaseall*
 chgrp.exe*                   msys-2.0.dll*                   recode-sr-latin.exe*
 chmod.exe*                   msys-apr-1-0.dll*               regtool.exe*
 chown.exe*                   msys-aprutil-1-0.dll*           reset.exe*
 chroot.exe*                  msys-asn1-8.dll*                restore*
 cksum.exe*                   msys-asprintf-0.dll*            rm.exe*
 clear.exe*                   msys-assuan-0.dll*              rmdir.exe*
 cmp.exe*                     msys-atomic-1.dll*              rnano.exe*
 column.exe*                  msys-blkid-1.dll*               runcon.exe*
 comm.exe*                    msys-bz2-1.dll*                 rview.exe*
 core_perl/                   msys-charset-1.dll*             rvim.exe*
 cp.exe*                      msys-com_err-1.dll*             sasldblistusers2.exe*
 csplit.exe*                  msys-crypt-0.dll*               saslpasswd2.exe*
 cut.exe*                     msys-crypto-1.0.0.dll*          scp.exe*
 cygcheck.exe*                msys-crypto-1.1.dll*            sdiff.exe*
 cygpath.exe*                 msys-curl-4.dll*                sed.exe*
 cygwin-console-helper.exe*   msys-edit-0.dll*                seq.exe*
 d2u.exe*                     msys-expat-1.dll*               setfacl.exe*
 dash.exe*                    msys-exslt-0.dll*               setmetamode.exe*
 date.exe*                    msys-fdisk-1.dll*               sexp-conv.exe*
 dd.exe*                      msys-ffi-6.dll*                 sftp.exe*
 df.exe*                      msys-formw6.dll*                sh.exe*
 diff.exe*                    msys-gcc_s-seh-1.dll*           sha1sum.exe*
 diff3.exe*                   msys-gcrypt-20.dll*             sha224sum.exe*
 dir.exe*                     msys-gettextlib-0-19-8-1.dll*   sha256sum.exe*
 dircolors.exe*               msys-gettextpo-0.dll*           sha384sum.exe*
 dirmngr.exe*                 msys-gettextsrc-0-19-8-1.dll*   sha512sum.exe*
 dirmngr-client.exe*          msys-gio-2.0-0.dll*             shred.exe*
 dirname.exe*                 msys-glib-2.0-0.dll*            shuf.exe*
 docx2txt*                    msys-gmodule-2.0-0.dll*         sleep.exe*
 docx2txt.pl*                 msys-gmp-10.dll*                sort.exe*
 dos2unix.exe*                msys-gmpxx-4.dll*               split.exe*
 du.exe*                      msys-gnutls-30.dll*             ssh.exe*
 dumpsexp.exe*                msys-gnutlsxx-28.dll*           ssh-add.exe*
 echo.exe*                    msys-gobject-2.0-0.dll*         ssh-agent.exe*
 egrep*                       msys-gomp-1.dll*                ssh-copy-id*
 env.exe*                     msys-gpg-error-0.dll*           sshd.exe*
 envsubst.exe*                msys-gssapi-3.dll*              ssh-keygen.exe*
 ex.exe*                      msys-gthread-2.0-0.dll*         ssh-keyscan.exe*
 expand.exe*                  msys-hcrypto-4.dll*             ssh-pageant.exe*
 expr.exe*                    msys-hdb-9.dll*                 ssp.exe*
 factor.exe*                  msys-heimbase-1.dll*            start*
 false.exe*                   msys-heimntlm-0.dll*            stat.exe*
 fgrep*                       msys-history8.dll*              strace.exe*
 file.exe*                    msys-hogweed-5.dll*             stty.exe*
 find.exe*                    msys-hx509-5.dll*               sum.exe*
 findssl.sh*                  msys-iconv-2.dll*               sync.exe*
 fmt.exe*                     msys-idn2-0.dll*                tabs.exe*
 fold.exe*                    msys-intl-8.dll*                tac.exe*
 funzip.exe*                  msys-kadm5clnt-7.dll*           tail.exe*
 gapplication.exe*            msys-kadm5srv-8.dll*            tar.exe*
 gawk.exe*                    msys-kafs-0.dll*                tee.exe*
 gawk-5.0.0.exe*              msys-kdc-2.dll*                 test.exe*
 gdbus.exe*                   msys-krb5-26.dll*               tic.exe*
 gencat.exe*                  msys-ksba-8.dll*                tig.exe*
 getconf.exe*                 msys-lzma-5.dll*                timeout.exe*
 getemojis*                   msys-magic-1.dll*               toe.exe*
 getfacl.exe*                 msys-menuw6.dll*                touch.exe*
 getopt.exe*                  msys-metalink-3.dll*            tput.exe*
 gettext.exe*                 msys-mpfr-6.dll*                tr.exe*
 gettext.sh*                  msys-ncurses++w6.dll*           true.exe*
 gettextize*                  msys-ncursesw6.dll*             truncate.exe*
 gio-querymodules.exe*        msys-nettle-7.dll*              trust.exe*
 git-flow*                    msys-nghttp2-14.dll*            tset.exe*
 git-flow-bugfix              msys-npth-0.dll*                tsort.exe*
 gitflow-common               msys-p11-kit-0.dll*             tty.exe*
 git-flow-config              msys-panelw6.dll*               tzset.exe*
 git-flow-feature             msys-pcre-1.dll*                u2d.exe*
 git-flow-hotfix              msys-pcre2-8-0.dll*             umount.exe*
 git-flow-init                msys-perl5_26.dll*              uname.exe*
 git-flow-log                 msys-psl-5.dll*                 uncompress*
 git-flow-release             msys-readline7.dll*             unexpand.exe*
 gitflow-shFlags              msys-readline8.dll*             uniq.exe*
 git-flow-support             msys-roken-18.dll*              unix2dos.exe*
 git-flow-version             msys-sasl2-3.dll*               unix2mac.exe*
 gkill.exe*                   msys-serf-1-0.dll*              unlink.exe*
 glib-compile-schemas.exe*    msys-sl-0.dll*                  unzip.exe*
 gobject-query.exe*           msys-smartcols-1.dll*           unzipsfx.exe*
 gpg.exe*                     msys-sqlite3-0.dll*             update-ca-trust*
 gpg-agent.exe*               msys-ssh2-1.dll*                updatedb*
 gpgconf.exe*                 msys-ssl-1.0.0.dll*             users.exe*
 gpg-connect-agent.exe*       msys-ssl-1.1.dll*               vdir.exe*
 gpg-error.exe*               msys-svn_client-1-0.dll*        vendor_perl/
 gpgparsemail.exe*            msys-svn_delta-1-0.dll*         vi*
 gpgscm.exe*                  msys-svn_diff-1-0.dll*          view.exe*
 gpgsm.exe*                   msys-svn_fs_fs-1-0.dll*         vim.exe*
 gpgtar.exe*                  msys-svn_fs_util-1-0.dll*       vimdiff.exe*
 gpgv.exe*                    msys-svn_fs_x-1-0.dll*          vimtutor*
 gpg-wks-server.exe*          msys-svn_fs-1-0.dll*            watchgnupg.exe*
 grep.exe*                    msys-svn_ra_local-1-0.dll*      wc.exe*
 groups.exe*                  msys-svn_ra_serf-1-0.dll*       which.exe*
 gsettings.exe*               msys-svn_ra_svn-1-0.dll*        who.exe*
 gunzip*                      msys-svn_ra-1-0.dll*            whoami.exe*
 gzexe*                       msys-svn_repos-1-0.dll*         winpty.dll*
 gzip.exe*                    msys-svn_subr-1-0.dll*          winpty.exe*
 head.exe*                    msys-svn_swig_perl-1-0.dll*     winpty-agent.exe*
 hmac256.exe*                 msys-svn_swig_py-1-0.dll*       winpty-debugserver.exe*
 hostid.exe*                  msys-svn_swig_ruby-1-0.dll*     wordpad*
 hostname.exe*                msys-svn_wc-1-0.dll*            xargs.exe*
 iconv.exe*                   msys-tasn1-6.dll*               xgettext.exe*
 id.exe*                      msys-ticw6.dll*                 xxd.exe*
 infocmp.exe*                 msys-unistring-2.dll*           yat2m.exe*
 infotocap.exe*               msys-uuid-1.dll*                yes.exe*
 install.exe*                 msys-wind-0.dll*                zcat*
 join.exe*                    msys-xml2-2.dll*                zcmp*
 kbxutil.exe*                 msys-xslt-1.dll*                zdiff*
 kill.exe*                    msys-z.dll*                     zegrep*
 ldd.exe*                     mv.exe*                         zfgrep*
 ldh.exe*                     nano.exe*                       zforce*
 less.exe*                    nettle-hash.exe*                zgrep*
 lessecho.exe*                nettle-lfib-stream.exe*         zipgrep*
 lesskey.exe*                 nettle-pbkdf2.exe*              zipinfo.exe*
 link.exe*                    ngettext.exe*                   zless*
 ln.exe*                      nice.exe*                       zmore*
 locale.exe*                  nl.exe*                         znew*
```

```
cj917@DESKTOP-381J2GT MINGW64 /usr/bin
$ cd ~cj917

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /usr/bin

cj917@DESKTOP-381J2GT MINGW64 /usr/bin
$ cd ~/

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /usr/bin

cj917@DESKTOP-381J2GT MINGW64 /usr/bin
$ cd ~

cj917@DESKTOP-381J2GT MINGW64 ~
$ cd /usr/bin

cj917@DESKTOP-381J2GT MINGW64 /usr/bin
$ cd

cj917@DESKTOP-381J2GT MINGW64 ~
$
```





