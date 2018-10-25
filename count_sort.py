from collections import defaultdict

'''
计数排序，复杂度为O(n)主要原因是，并不是通过比较来完成排序
计数排序假设 n 个输入元素中的每一个都是介于 [0,k] 之间的整数，计数排序的思路是对每一个输入元素 x ，
确定小于 x 的所有元素个数，然后就可以直接把 x 放到它在最终输出数组的位置上

'''
def counting_sort_v1(seq):
    '''
    counting sort Version 1
    >>> print(counting_sort_v1([9, 0, 1, 1, 2, 3]))
    [0, 1, 1, 2, 3, 9]
    '''
    counter = []

    k = max(seq)

    # Time complexity: O(k)
    for i in range(k+1):
        counter.append(0)
    # Time complexity: O(n)
    for i in seq:
        counter[i] += 1
    # Time complexity: O(k)
    for i in range(1, k+1):
        counter[i] += counter[i-1]


    result = [0] * len(seq)

    index = len(seq) - 1

    # Time complexity O(k)
    while True:
        if k == 0:
            break
        elif counter[k] == counter[k-1]:
            k -= 1
        else:
            result[index] = k
            index -= 1
            counter[k] -= 1

    return result

def counting_sort_v2(seq):
    '''
    counting sort Version 2
    >>> print(counting_sort_v2([9, 0, 1, 1, 2, 3]))
    [0, 1, 1, 2, 3, 9]
    '''
    counter = []

    k = max(seq)

    for i in range(k+1):
        counter.append(0)

    for i in seq:
        counter[i] += 1

    for i in range(1, k+1):
        counter[i] += counter[i-1]


    result = [0] * (len(seq)+1)

    index = len(seq) - 1
    # the change compared to Version 1 is that because we store the new index of the seq[i] in the 'counter', we can directly assign the seq[i] to the result[new index]
    # Time compelxity: O(n)
    while index >= 0:
        result[counter[seq[index]]] = seq[index]        #counter[seq[index]] store the new index of the seq[index]
        counter[seq[index]] -= 1                        #to deal with replication, eveytime when place the seq[index] in the right place, couter[seq[index]] minus 1
        index -= 1

    return result[1:]




def counting_sort_V3(seq, key=lambda x: x):
    '''
    Version 3
    >>> print(counting_sort_V3([9, 0, 1, 1, 2, 3]))
    [0, 1, 1, 2, 3, 9]
    '''
    (result, counter) =([], defaultdict(list)) #default(list) set that the default value is list([])

    for x in seq:
       counter[key(x)].append(x)

    for k in range(min(counter), max(counter)+1):
        result.extend(counter[k])              #concate list in order to get the sorted list

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()