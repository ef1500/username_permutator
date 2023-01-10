# utils.py
# Username Permutator
# Example: uname.py ef1500 -v would output af1500, if1500, of1500, uf1500 (replacing vowels)
# Example: uname.py ef1500 -n 9999 would output ef0, ef1 .... ef9999
# Example: uname.py ef1500 -n 9999 -z would output ef0000, ef0001 .... ef9999
import itertools
import re

class pMethods:
    
    def __init__(self, uname):
        self.uname = uname #username
        self.uname_as_list = list(self.uname)
        self.p_unames = [] #permutated usernames
        
    @staticmethod
    def list_to_string(c_list):
        return ''.join([str(elem) for elem in c_list])
        
    @staticmethod
    def swap_at_index(uname_list, index, iterable) -> list:
        """Create x new strings from index and iterable
        Args:
            uname_list (list): input string as list
            index (iterator): index of character to replace
            iterable (list): list of replacements
        """
        uname_tmp = uname_list
        new_strings = [] # list to save the new strings in
        for item in iterable: # iterate over iterable
            uname_tmp[index] = item
            new_strings.append(pMethods.list_to_string(uname_tmp))
        return new_strings
    
    def unames(self):
        return self.p_unames
     
    def numswap(self, numto, preserve_zeroes=False, numzeroes=None, function="numswap"):
        """Generate usernames by swapping numbers

        Args:
            numto (int): number to count to
            numrange (list, optional): range of numbers. Defaults to None.
            preserve_zeroes (bool, optional): preserve zeroes. Defaults to False.
        """
        temp_unames = []
        if preserve_zeroes is False:
            iterator = (itertools.count(start=0, step=1))
            num_list = list(str(next(iterator)) for _ in range(numto + 1))
        if preserve_zeroes is True:
            iterator = (itertools.count(start=0, step=1))
            num_list = list(str(next(iterator)).rjust(numzeroes, '0') for _ in range(numto + 1))
            
        if function == "numadd":
            if len(self.p_unames) != 0:
                for nums in num_list:
                    for p_uname in self.p_unames:
                        temp_unames.append(f"{p_uname + nums}")
                self.p_unames.extend(temp_unames)
            else:
                self.p_unames.extend([f"{self.uname+num}" for num in num_list])
        if function == "numswap":
            if len(self.p_unames) != 0:
                for p_uname in self.p_unames:
                    temp_uname = p_uname
                    regex = r'\d{1,}'
                    re_find = re.finditer(regex, temp_uname)
                    for iteritem in re_find:
                        for range_1, range_2 in iteritem.regs:
                            for num in num_list:
                                temp_uname_list = list(p_uname)
                                temp_uname_list[range_1:range_2] = num
                                temp_unames.append(pMethods.list_to_string(temp_uname_list))
                self.p_unames.extend(temp_unames)
            else:
                temp_uname = self.uname
                regex = r'\d{1,}'
                re_find = re.finditer(regex, temp_uname)
                for iteritem in re_find:
                    for range_1, range_2 in iteritem.regs:
                        for num in num_list:
                            temp_uname_list = list(temp_uname)
                            temp_uname_list[range_1:range_2] = num
                            temp_unames.append(pMethods.list_to_string(temp_uname_list))
                self.p_unames.extend(temp_unames)
     
    def vowelswap_permutate(self) -> None:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        for index in enumerate(self.uname): # For each letter in the username
            if index[1] in vowels: # If there is a vowel present
                temp_unames = pMethods.swap_at_index(self.uname_as_list, index[0], vowels) # Create More!
                self.p_unames.extend(temp_unames) # Map to the append
                temp_unames.clear() # Clear the list