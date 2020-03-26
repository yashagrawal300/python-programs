#Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. All numbers at input are integers of one or two digits.

#You can terminate the program after getting 42

while True:
    x=int(input())
    if x==42:
       break
    else:
        print(x)
