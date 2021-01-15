import numpy as np

def F1_score(y_pred, y_true):
    P = precision(y_pred, y_true)
    R = recall(y_pred, y_true)
    return 2*(P*R)/(P+R)

def precision(y_pred, y_true):
    TP, TN, FP, FN = __calculate(y_pred, y_true)
    return TP/(TP+FP)

def accuracy(y_pred, y_true):
    TP, TN, FP, FN = __calculate(y_pred, y_true)
    return (TP+TN)/(TP+FN+TN+FP)

def specificity(y_pred, y_true):
    TP, TN, FP, FN = __calculate(y_pred, y_true)
    return TN/(TN+FP)

def recall(y_pred, y_true):
    TP, TN, FP, FN = __calculate(y_pred, y_true)
    return TP/(TP+FN)

def __calculate(y_pred, y_true):
    TP, TN, FP, FN = 0, 0, 0, 0
    N = len(y_pred)
    for i in range(N):
        if y_pred[i] == y_true[i]:
            if y_true[i] == 1:
                TP += 1
            else:
                FN += 1
        else:
            if y_true[i] == 0:
                FP += 1
            else:
                TN += 1
    return TP, TN, FP, FN