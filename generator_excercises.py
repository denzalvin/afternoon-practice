#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def primes_gen():
    yield 2
    yield from _primes_gen(3)


gen = primes_gen()
for _ in range(10):
    if gen % 2 == 0:
        print(next(gen), end=' ')
    
# Expected output


# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(string):
    for letter in string:
        if letter not in string[string.index(letter)+1:]:
            yield letter

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o