from collections import Counter
def max_permutation(perm, pointsList=None):
    '''
    >>> print(max_permutation([2, 2, 0, 5, 3, 5, 7, 4]))
    {0, 2, 5}
    ''' 

    if pointsList is None: pointsList = set(range(len(perm)))
    
    if len(pointsList) == 1: return pointsList                               #结束条件1: 点列表只包含一个元素，那么一定是一一映射
    
    mappingList = set(perm[i] for i in pointsList)                           #根据点列表，创建映射表(集合)
    notMappedPointsList = pointsList - mappingList                           #找到没有被映射的点的列表(集合)

    if notMappedPointsList:
        pointsList.remove(notMappedPointsList.pop())
        max_permutation(perm, pointsList)
    return pointsList                                                        #结束条件2: 不存在没有被映射到的点列表(集合)，全部都是一一映射                                    


def max_permutation_optimized(perm, pointsList=None):
    '''
    >>> print(max_permutation_optimized([2, 2, 0, 5, 3, 5, 7, 4]))
    {0, 2, 5}
    '''
    if pointsList == None: pointsList = set(range(len(perm)))
    if len(pointsList) == 1: return pointsList
    
    referenceCounter = Counter(perm)
    notMappedPointsList = [i for i in pointsList if referenceCounter[i] == 0]
    
    while notMappedPointsList:
        
        element = notMappedPointsList.pop()
        pointsList.remove(element)
        index = perm[element]
        referenceCounter[index] -= 1

        if referenceCounter[index] == 0:
            notMappedPointsList.append(index)
    
    return pointsList





if __name__ == '__main__':
    import doctest
    doctest.testmod()

    


