def sel_sort_recursion(seq):

    '''
    >>> seq1 = [1, 11, 2, 22]
    >>> sel_sort_recursion(seq1)
    >>> print(seq1)
    [1, 2, 11, 22]
    '''

    def aux(seq, index):
        if index == 0: return
        
        max_j = index

        for j in range(index):
            if seq[j] > seq[max_j]:
                max_j = j
        
        seq[index], seq[max_j] = seq[max_j], seq[index]

        aux(seq, index-1)
    
    aux(seq, len(seq)-1)

def sel_sort_iteration(seq):
    '''
    >>> seq2 = [1, 11, 2, 22]
    >>> sel_sort_iteration(seq2)
    >>> print(seq2)
    [1, 2, 11, 22]
    '''

    lenth = len(seq)

    for i in range(lenth-1, 0, -1):
        max_i = i

        for j in range(0, i):
            if seq[j] > seq[max_i]:
                max_i = j
            
        seq[i], seq[max_i] = seq[max_i], seq[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
