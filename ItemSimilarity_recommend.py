import math

def ItemSimilarity_alpha(train, alpha=0.3):
    '''
    基于物品的协同过滤方法--alpha热门物品惩罚
    :param train:
    :return:
    '''
    C = dict()  ## 物品对同时被喜欢的次数
    N = dict()  ## 物品被喜欢用户数
    for u, items in train.items():
        for i in items.keys():
            if i not in N.keys():
                N[i] = 0
            N[i] += 1
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i] = dict()
                if j not in C[i].keys():
                    C[i][j] = 0
                C[i][j] += 1

    W = dict()
    ## 具体相似度的计算方法
    for i, related_items in C.items():
        if i not in W.keys():
            W[i] = dict()
        for j, cij in related_items.items():
            W[i][j] = cij / (math.pow(N[i], alpha) * math.pow(N[j], 1-alpha))

    return W


def Recommend(train, user_id, W, K):
    '''
    计算预测评分
    :param train:
    :param user_id:
    :param W:
    :param K: 召回参数
    :return:
    '''
    rank = dict()
    ru = train[user_id]
    for i, pi in ru.items():
        tmp = W[i]
        for j, wj in sorted(tmp.items(), key=lambda d: d[1], reverse=True)[0:K]:
            if j not in rank.keys():
                rank[j] = 0
            if j in ru:
                continue
            rank[j] += pi * wj

    return rank


if __name__ == '__main__':
    Train_data = {
        'A': {'i1': 1, 'i2': 1, 'i4': 1},
        'B': {'i1': 1, 'i4': 1},
        'C': {'i1': 1, 'i2': 1, 'i5': 1},
        'D': {'i2': 1, 'i3': 1},
        'E': {'i3': 1, 'i5': 1},
        'F': {'i2': 1, 'i4': 1}
    }
    W = ItemSimilarity_alpha(Train_data)
    rank = Recommend(Train_data, 'C', W, 3)
    print("end")
