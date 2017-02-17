# Question 1 - Print Function:
from __future__ import print_function
if __name__ == '__main__':
    myString = ""
    n = int(raw_input())
    for i in range(n):
        myString += str(i+1)
    print(myString)

# Question 2 - Tuples

if __name__ == '__main__':
    t = ()
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = hash(tuple(integer_list))
    print(t)

# Question 3 - Finding the Percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]), '.2f'))


# Question 4 - Text Wrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
    

# Question 5 - Sum and Prod:

import numpy

N, M = map(int, raw_input().split())

my_array = numpy.array([ map(int, raw_input().split()) for i in range(N) ])
print numpy.prod( numpy.sum( my_array, axis = 0 ) )
