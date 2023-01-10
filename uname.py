# Example: uname.py ef1500 -v would output af1500, if1500, of1500, uf1500 (replacing vowels)
# Example: uname.py ef1500 -n 9999 would output ef0, ef1 .... ef9999
# Example: uname.py ef1500 -n 9999 -z would output ef0000, ef0001 .... ef9999
import argparse
from utils import pMethods
import os

parser = argparse.ArgumentParser(prog="Username Permutator", description="Permutate Usernames", epilog="https://github.com/ef1500")
parser.add_argument('-o', '--output', type=str, help="Output Filename", default="usernames.txt")
parser.add_argument('uname', metavar='USERNAME', type=str, help="Username to Permutate")
parser.add_argument('-p', '--print', action="store_true", help="Print the results to the terminal", required=False)
operations = parser.add_mutually_exclusive_group(required=True)
operations.add_argument('-v', '--vowelswap', action="store_true", help="Swap vowels in the username")
operations.add_argument('-n', '--numswap', type=int, help="Swap numbers in the username, counting to a specified number")
operations.add_argument('-nA', '--numadd', type=int, help="Add numbers to end of the username, counting up")
parser.add_argument('-aZ', '--addzeroes', type=int, help="add N leading zeroes during the numswap/numadd operation", default=None, required=False)

args = parser.parse_args()

u_pMethods = pMethods(args.uname)
if args.vowelswap:
    u_pMethods.vowelswap_permutate()

if args.numswap:
    u_pMethods.numswap(args.numswap, isinstance(args.addzeroes, int), args.addzeroes)
    
if args.numadd:
    u_pMethods.numswap(args.numswap, isinstance(args.addzeroes, int), args.addzeroes, function="numadd")
    
with open(os.path.join(os.getcwd(), args.output), "w", encoding="utf-8") as username_file:
    unames = u_pMethods.unames()
    for uname in unames:
        if args.print is True:
            print(uname)
        username_file.write(f"{uname}\n")
    print(f"Created {args.output} containing {len(unames)} usernames.")