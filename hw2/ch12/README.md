# Process Management

## The top command doesnt work 

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents
$ top
bash: top: command not found
```

## Killing a Crashed Process

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ps aux | grep 'chrome'

cj917@DESKTOP-381J2GT MINGW64 ~
$ kill 6978
bash: kill: (6978) - No such process

cj917@DESKTOP-381J2GT MINGW64 ~
$ ps aux | grep 'chrome'

cj917@DESKTOP-381J2GT MINGW64 ~
$ kill -9 6978
bash: kill: (6978) - No such process

cj917@DESKTOP-381J2GT MINGW64 ~
$ ps aux | grep 'chrome'
```

## Foreground and Background Jobs

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ sleep 5

cj917@DESKTOP-381J2GT MINGW64 ~
$ sleep 5 &
[1] 1994

cj917@DESKTOP-381J2GT MINGW64 ~
$ sleep 15 &
[2] 1998
[1]   Done                    sleep 5

cj917@DESKTOP-381J2GT MINGW64 ~
$ sleep 10

[3]+  Stopped                 sleep 10

cj917@DESKTOP-381J2GT MINGW64 ~
$ jobs
[2]-  Done                    sleep 15
[3]+  Stopped                 sleep 10

cj917@DESKTOP-381J2GT MINGW64 ~
$ fg 2
bash: fg: 2: no such job
```

## Actvity 12

```
cj917@DESKTOP-381J2GT MINGW64 ~
$ ps aux | grep 'internet explorer'
```

