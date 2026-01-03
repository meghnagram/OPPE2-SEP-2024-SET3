

n = int(input())
for i in range(n):
    roll, marks = map(int, input().split())
    if marks % 10 in [8, 9]:
        marks = (marks // 10 + 1) * 10
        print(roll, marks)


# #Another Method:

# # Write your code here

# num=int(input())

# while(num!=0):
#     num -=1
#     l=[]
#     s=input()
#     l=s.split(' ')
#     u=int(l[1])%10
#     t=int(l[1])//10
#     if u ==8 or u==9:
#         print (l[0]+' '+str((t+1)*10))

# Ceil Marks to Nearest Tens if Close
# Write a program to process roll numbers and marks for students. If a student's marks have a unit digit of 8 or 9, round their marks up to the nearest tens. Otherwise, keep the marks unchanged. Print only the roll number and updated marks for students whose marks were updated.

# NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

# Input Format

# The first line contains the number of lines of student data n.
# Next n lines contains the student data with roll number and marks separated by space.
# Output Format

# Student data for the roll number whose marks has been updated in the format of roll number and separated by comma.
# Examples

# 48 -> 50
# 69 -> 70
# 70 -> 70
# 37 -> 37
