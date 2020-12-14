import itertools


def combiner(list_, k, condition='=='):
    if k == 1:
        return list_
    else:
        if condition == '==':
            result = list(itertools.combinations(list_, k))
            list_result = []
            for r in result:
                r = list(r)
                list_result.append(r)
            return list_result
        elif condition == '>':
            cumm_result = []
            list_result = []
            for n in range(k+1, len(list_)):
                result = list(itertools.combinations(list_, n))
                cumm_result += result
            for res in cumm_result:
                res = list(res)
                list_result.append(res)
            return list_result
        elif condition == '<':
            cumm_result = []
            list_result = []
            for n in range(k - 1, 1, -1):
                result = list(itertools.combinations(list_, n))
                cumm_result += result
            for res in cumm_result:
                res = list(res)
                list_result.append(res)
            return list_result
        elif condition == '>=':
            cumm_result = []
            list_result = []
            for n in range(k, len(list_)):
                result = list(itertools.combinations(list_, n))
                cumm_result += result
            for res in cumm_result:
                res = list(res)
                list_result.append(res)
            return list_result
        elif condition == '<=':
            cumm_result = []
            list_result = []
            for n in range(k, 1, -1):
                result = list(itertools.combinations(list_, n))
                cumm_result += result
            for res in cumm_result:
                res = list(res)
                list_result.append(res)
            return list_result


print(combiner([1,2,3,4], 3, '<='))

