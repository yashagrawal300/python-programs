'''Cheeku is ill. He goes to Homeopathic Doctor - Dr. Thind. 

Doctor always recommends medicines after reading from a secret book that he has. This secret book has recipe to cure any disease. Cheeku is chalak. He wants to know if Doctor is giving him correct medicine or not. 

So he asks Doctor 2 questions -

Length of name of Book.
Number of pages in the Book.
Cheeku will take medicine from him only if Length of name of Book is lesser than or equal to 23 and number of pages in book is between 500 to 1000.

Otherwise he will not take medicine from this Doctor.

Help Cheeku decide. Print "Take Medicine" if he should take medicine from doctor. Else print "Don't take Medicine".

Input:

2 integers-

First denoting length of Secret Book.

Second is number of pages in Book.'''


t = input()
t = t.split(' ')
if int(t[0])<=23 and int(t[1])<=1000 and int(t[1])>=500:
    print("Take Medicine")
else:
    print("Don't take Medicine")
