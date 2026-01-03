
with open(filename) as f:
    n = int(f.readline())
    i = 1
    for line in f:
        filled_line = ""
        for char in line:
            if char == "_" and i <= n:
                filled_line += str(i)
                i += 1
            else:
                filled_line += char
        print(filled_line, end="")

  #Another Method:

# Write your code to read the file and print the result.
# use the variable filename for the name of the file.


with open(filename,'r') as file:
    firstline=file.readline().rstrip()

    num=int(firstline)
    i=1
    

    for line in file:
        for ch in line:
            if ch=='_' and i<=num:
                print(i,end='')
                i +=1
            else: 
                print(ch,end='')

Fill the first n blanks with 1 to n
Write a program to fill the first n blanks (represented by underscores _) in a text with numbers from 1 to n.

The first line of the input contains the integer n, the number of blanks to fill.
Subsequent lines contain the text, with blanks represented as _.
Fill the blanks sequentially with numbers from 1 to n.
If there are more blanks than n, the remaining blanks remain unchanged.


Example

Input

11
a_bc__d___e
f_g__h__i__j
k___l_m__n
Output

11
a1bc23d456e
f7g89h1011i__j
k___l_m__n

