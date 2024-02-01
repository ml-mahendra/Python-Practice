# -*- coding: utf-8 -*-
"""

@author: Mahendra Nath Reddy E
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    total_query_marks = sum(query_marks)
    query_avg_marks = total_query_marks / len(query_marks)
    formated_avg = "{:.2f}".format(query_avg_marks)
    print(formated_avg)
    