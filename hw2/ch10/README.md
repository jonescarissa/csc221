# Grep and Regular Expressions

## eGrep

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ cat mysampledata.txt
Fred apples 20
Susy oranges 5
Mark watermelons 12
Robert pears 4
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3
Oliver rockmelons 2
Betty limes 14

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep 'melon' mysampledata.txt
Mark watermelons 12
Oliver rockmelons 2

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep -n 'melon' mysampledata.txt
3:Mark watermelons 12
11:Oliver rockmelons 2

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep -c 'melon' mysampledata.txt
2
```

## Some Examples

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '[aeiou]{2,}' mysampledata.txt
Robert pears 4
Lisa peaches 7
Anne mangoes 7
Greg pineapples 3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '2.+' mysampledata.txt
Fred apples 20
Mark watermelons 12
Susy oranges 12
Oliver rockmelons 2

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '2$' mysampledata.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep 'or|is|go' mysampledata.txt
Susy oranges 5
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Anne mangoes 7

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '^[A-K]' mysampledata.txt
Fred apples 20
Anne mangoes 7
Greg pineapples 3
Betty limes 14
```

## Actvity 10

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ cat actvity10
Greg vodka 454
Fred whiskey 13
Susan patron 20
Carissa Fourloco 180
Frank beer 789
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep 'patron' actvity10
Susan patron 20

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep -n 'patron' actvity10
3:Susan patron 20

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep -c 'patron' actvity10
1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '[aeiou]{3,}' actvity10

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '[aeiou]{2,}' actvity10
Carissa Fourloco 180
Frank beer 789

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep '4.+' actvity10
Greg vodka 454

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch10 (master)
$ egrep 'is|an|eg' actvity10
Greg vodka 454
Fred whiskey 13
Susan patron 20
Carissa Fourloco 180
Frank beer 789
```

