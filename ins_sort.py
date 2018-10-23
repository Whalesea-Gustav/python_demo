def ins_sort_recursion(seq):

    '''
    >>> seq = [1, 11, 2, 14, 5, 8]
    >>> print(ins_sort_recursion(seq))
    [1, 2, 5, 8, 11, 14]
    '''

    def aux(seq, i):
        #when the index is 0, finish sorting
        if i == 0: return
        #sort 0....i-1 recursively
        aux(seq, i-1)
        #insert seq[i] into the seq[0..i-1]

        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1


    aux(seq, len(seq)-1)

    return seq


def ins_sort_recursion2(seq, i):
    if i == 0: return

    ins_sort_recursion2(seq, i-1)

    while i > 0 and seq[i-1] > seq[i]:
        seq[i-1], seq[i] = seq[i], seq[i-1]
        i -= 1


def ins_sort_iteration(seq):
    '''
    >>> seq2 = [1, 11, 2, 13, 5]
    >>> ins_sort_iteration(seq2)
    >>> print(seq2)
    [1, 2, 5, 11, 13]
    '''
    for i in range(1,len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
