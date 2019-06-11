from numpy import *

'''

'''

def loadExData():
    data = [[0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 5],
            [0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 4, 1, 0, 1, 0, 4, 0],
            [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
            [5, 4, 2, 0, 0, 0, 0, 5, 5, 0, 0],
            [0, 0, 0, 0, 5, 0, 1, 0, 0, 0, 0],
            [4, 1, 4, 0, 0, 0, 0, 4, 5, 0, 1],
            [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
            [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
            [1, 0, 0, 4, 0, 0, 0, 1, 2, 0, 0]]

    return data

def svdEst(userData, xformedItems, user, item, simMeas=cos()):
    n = shape(xformedItems)[0]
    simTotal = 0.0
    ratSimTotal = 0.0
    # 对于给定用户，for循环所有的物品，计算与item的相似度
    for j in range(n):
        userRating = userData[:, j]
        if userRating == 0 or j == item:
            continue
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print('the %d and %d similarity is: %f ' % (item, j, similarity))

        # 对相似度求和
        simTotal += similarity
        ratSimTotal += similarity * userRating

    if simTotal == 0:
        return 0
    else:
        return ratSimTotal/simTotal

def recommend(dataMat, user, N=3, simMeas=cos(), estMethod=svdEst()):
    '''
    基于SVD进行推荐，寻找未评级的物品，对给定用户建立一个未评分的物品列表
    :param dataMat:
    :param user:
    :param N:
    :param simMeas:
    :param estMethod:
    :return:
    '''
    U, Sigma, VT = linalg.svd(dataMat)
    Sig4 = mat(eye(4)*Sigma[:4])
    xformedItems = dataMat.T * U[:, :4] * Sig4.I
    print('xformedItems=', xformedItems)
    print('xformedItems行和列数', shape(xformedItems))

    unratedItems = nonzero(dataMat[user, :].A == 0)[1]
    print('dataMat[user, :].A=', dataMat[user, :].A)

    if len(unratedItems) == 0:
        return ('you rated everything')
    itemScores = []
    for item in unratedItems:
        print('item=', item)
        estimatedScore = estMethod(dataMat[user, :], xformedItems, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]

myMat = mat(loadExData())
result = recommend(myMat, 1, estMethod=svdEst())
print(result)


