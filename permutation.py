def insertion(e, s):
    # This generator yields all possible insertions of element e into the list s.
    for i in range(len(s) + 1):
        yield s[:i] + [e] + s[i:]

def perm(s):
    # This function generates all permutations of the input list s.
    if s == []:  # Base case: if the list is empty, yield an empty list
        yield []
    else:
        # Select the first element e and the rest of the list s1
        e, s1 = s[0], s[1:]
        
        # Recursively generate all permutations of the remaining list s1
        for s1p in perm(s1):
            # For each permutation s1p, generate all possible insertions of e
            for p in insertion(e, s1p):
                yield p  # Yield each permutation resulting from different insertions

# Example Usage:
# Generate and print all permutations of the list [1, 2, 3, 4]
for p in perm([1, 2, 3, 5]):
    print(p)
'''
Recursion:

    When the input list s is not empty, the function proceeds with the recursive case.

    e, s1 = s[0], s[1:]: It selects the first element e and the rest of the list s1. This is done to process each element one by one.

    for s1p in perm(s1):: This loop recursively generates all permutations of the remaining list s1. The variable s1p will hold each permutation of the sublist.

    for p in insertion(e, s1p):: For each permutation s1p, the function generates all possible insertions of the current element e into that permutation using the insertion function. This allows the generation of permutations that include the current element at different positions.

    yield p: The nested loops yield each permutation p resulting from different insertions of e into the permutations of the remaining list.
    '''
