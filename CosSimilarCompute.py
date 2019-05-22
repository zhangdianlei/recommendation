import math
import numpy as np


def cosSimilarCompute(u_k, w_t):
    '''
    计算两向量之间的相似度
    :param u_k:
    :param w_t:
    :return: 相似度数值
    '''
    assert len(u_k) == len(w_t), "user vector size not equals item vector"
    assert len(u_k) != 0, "user vector size equals to 0"

    i = 0
    score1 = 0
    score2 = 0
    score3 = 0

    while i < len(u_k):
        score1 = score1 + u_k[i] * w_t[i]
        score2 = score2 + u_k[i] * u_k[i]
        score3 = score3 + w_t[i] * w_t[i]
        i = i + 1
    if score3 or score2 == 0:
        assert "user or item vector equal to 0"

    return score1 * 1.0 / (math.sqrt(score2 * math.sqrt(score3)))

def cosSim(u_k, w_t):
    '''
    使用numpy包内函数计算向量相似度
    :param u_k:
    :param w_t:
    :return:
    '''
    a = np.mat(u_k)
    b = np.mat(w_t)

    num = float(a * b.T)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

U = [[0.1, 0.5, 0.8, 0.6],
     [0.2, 0.3, 0.4, 0.7],
     [0.1, 0.8, 0.5, 0.6]]

W = [[0.2, 0.3, 0.6, 0.5],
     [0.4, 0.6, 0.8, 0.5],
     [0.5, 0.3, 0.6, 0.1]]

u_k = [0.1, 0.5, 0.8, 0.6]
w_t = [0.4, 0.6, 0.8, 0.5]

print(cosSimilarCompute(u_k, w_t))
print(cosSim(u_k, w_t))

