# Username Permutator
Simple python program to manipulate usernames

usage: `python3 uname.py elira120 -o usernames.txt -v -p`
output: 
```
alira120
elira120
ilira120
olira120
...
ylyry120
```
### Options
`python3 uname.py -h`
```
usage: Username Permutator [-h] [-o OUTPUT] [-p] (-v | -n NUMSWAP | -nA NUMADD | -aZ ADDZEROES) USERNAME

Permutate Usernames

positional arguments:
  USERNAME              Username to Permutate

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output Filename
  -p, --print           Print the results to the terminal
  -v, --vowelswap       Swap vowels in the username
  -n NUMSWAP, --numswap NUMSWAP
                        Swap numbers in the username, counting to a specified number
  -nA NUMADD, --numadd NUMADD
                        Add numbers to end of the username, counting up
  -aZ ADDZEROES, --addzeroes ADDZEROES
                        add N leading zeroes during the numswap/numadd operation
```

#### Application
You have a target that has the username `pomu100` they're known to use the same base username, but perhaps they add a unique string of digits to the end of each.
This application will quickly allow you to generate a list of all possible usernames they may be using like so:
`python3 uname.py pomu100 -n 999` will generate a list containing every username starting from pomu0 to pomu999.
you can even add zeroes, to generate usernames from pomu000 to pomu999. This can by done like so:
`python3 uname.py pomu100 -n 999 -aZ 3`