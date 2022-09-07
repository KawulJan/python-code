 #write a function that takes a string argument
    #and returns the numer of works in it.


def vowl_count(string):
        vowels =['a','e','i','u','o']
        count = 0
        for ch in string:
            if ch in vowels:
               count += 1
        return count


def text_with_my_name():
         assert vowl_count('carlos') ==4

def test_with_my_uppercase_name():
       assert vowl_count('KIDMAN CARLOS') ==4
