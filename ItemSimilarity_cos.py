import math

def ItemSimilarity_cos(train):
    '''
    基于物品的协同过滤方法--余弦方法
    :param train:
    :return:
    '''
    C = dict()  ## 物品对同时被喜欢的次数
    N = dict()  ## 物品被喜欢用户数
    for u, items in train.items():
        for i in items.keys():
            if i not in N.keys():
                N[i] = 0
            N[i] += items[i] * items[i]
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i] = dict()
                if j not in C[i].keys():
                    C[i][j] = 0
                C[i][j] += items[i] * items[j]

    W = dict()
    ## 具体相似度的计算方法
    for i, related_items in C.items():
        if i not in W.keys():
            W[i] = dict()
        for j, cij in related_items.items():
            W[i][j] = cij / (math.sqrt(N[i]) * math.sqrt(N[j]))

    return W


if __name__ == '__main__':
    Train_data = {
        'A': {'i1': 1, 'i2': 1, 'i4': 1},
        'B': {'i1': 1, 'i4': 1},
        'C': {'i1': 1, 'i2': 1, 'i5': 1},
        'D': {'i2': 1, 'i3': 1},
        'E': {'i3': 1, 'i5': 1},
        'F': {'i2': 1, 'i4': 1}
    }
    W = ItemSimilarity_cos(Train_data)
    print("end")
