'''You are provided an array  of size  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by .

Note: View the sample explanation section for more clarification.'''



N = int(input())

x = input()
x = x.split(' ')
sep = ', '
y = []
for i in range(len(x)):
    y.append(x[i][len(x[i])-1])
r = ''

for i in range(len(y)):
    r+=y[i]

if r[len(r)-1]=='0':
    print('Yes')
else:
    print('No')
