# Filters

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cat mysampledata.txt
Fred apples 20
Susy oranges 5
Mark watermellons 12
Robert pears 4
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3
Oliver rockmellons 2
Betty limes 14
```

## Head

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ head mysampledata.txt
Fred apples 20
Susy oranges 5
Mark watermellons 12
Robert pears 4
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ head -4 mysampledata.txt
Fred apples 20
Susy oranges 5
Mark watermellons 12
Robert pears 4
```

## Tail

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ tail mysampledata.txt
Mark watermellons 12
Robert pears 4
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3
Oliver rockmellons 2
Betty limes 14
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ tail -3 mysampledata.txt
Greg pineapples 3
Oliver rockmellons 2
Betty limes 14
```

## Sort

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ sort mysampledata.txt
Anne mangoes 7
Betty limes 14
Fred apples 20
Greg pineapples 3
Lisa peaches 7
Mark grapes 39
Mark watermellons 12
Oliver rockmellons 2
Robert pears 4
Susy oranges 12
Susy oranges 5
Terry oranges 9
```

## NL

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ nl mysampledata.txt
     1  Fred apples 20
     2  Susy oranges 5
     3  Mark watermellons 12
     4  Robert pears 4
     5  Terry oranges 9
     6  Lisa peaches 7
     7  Susy oranges 12
     8  Mark grapes 39
     9  Anne mangoes 7
    10  Greg pineapples 3
    11  Oliver rockmellons 2
    12  Betty limes 14

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ nl -s '. ' -w 10 mysampledata.txt
         1. Fred apples 20
         2. Susy oranges 5
         3. Mark watermellons 12
         4. Robert pears 4
         5. Terry oranges 9
         6. Lisa peaches 7
         7. Susy oranges 12
         8. Mark grapes 39
         9. Anne mangoes 7
        10. Greg pineapples 3
        11. Oliver rockmellons 2
        12. Betty limes 14
```

## WC

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ wc mysampledata.txt
 11  36 207 mysampledata.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ wc -l mysampledata.txt
11 mysampledata.txt

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ wc -lw mysampledata.txt
 11  36 mysampledata.txt
```

## Cut

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cut -f 1 -d ' ' mysampledata.txt
Fred
Susy
Mark
Robert
Terry
Lisa
Susy
Mark
Anne
Greg
Oliver
Betty

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cut -f 1,2 -d ' ' mysampledata.txt
Fred apples
Susy oranges
Mark watermellons
Robert pears
Terry oranges
Lisa peaches
Susy oranges
Mark grapes
Anne mangoes
Greg pineapples
Oliver rockmellons
Betty limes
```

## Sed

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ sed 's/oranges/bananas/g' mysampledata.txt
Fred apples 20
Susy bananas 5
Mark watermellons 12
Robert pears 4
Terry bananas 9
Lisa peaches 7
Susy bananas 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3
Oliver rockmellons 2
Betty limes 14
```

## Uniq

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cat mysampledata.txt
Fred apples 20
Susy oranges 5
Mark watermellons 12
Robert pears 4
Terry oranges 9
Lisa peaches 7
Susy oranges 12
Mark grapes 39
Anne mangoes 7
Greg pineapples 3
Oliver rockmellons 2
Betty limes 14
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ uniq mysampledata.txt
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
```

## Tac

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ tac mysampledata.txt
Betty limes 14
Oliver rockmelons 2
Greg pineapples 3
Anne mangoes 7
Mark grapes 39
Susy oranges 12
Lisa peaches 7
Terry oranges 9
Robert pears 4
Mark watermelons 12
Susy oranges 5
Fred apples 20
```

## Activity 9

```
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ head actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails gin 300
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ tail actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails gin 300
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ sort actvity1
Fingers fries 350
Foot cherries 100
Head brownies 80
Nails gin 300
Toes chicken 4

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ nl actvity1
     1  Foot cherries 100
     2  Head brownies 80
     3  Toes chicken 4
     4  Fingers fries 350
     5  Nails gin 300

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ wc actvity1
 4 15 85 actvity1

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cut -f 1 -d ' ' actvity1
Foot
Head
Toes
Fingers
Nails

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cut -f 1,2,3 -d ' ' actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails gin 300

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ sed 's/gin/chicken/g' actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails chicken 300
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ cat actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails gin 300
cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ uniq actvity1
Foot cherries 100
Head brownies 80
Toes chicken 4
Fingers fries 350
Nails gin 300

cj917@DESKTOP-381J2GT MINGW64 ~/Documents/courses/csc221/hw2/ch9 (master)
$ tac actvity1
Nails gin 300Fingers fries 350
Toes chicken 4
Head brownies 80
Foot cherries 100
```

