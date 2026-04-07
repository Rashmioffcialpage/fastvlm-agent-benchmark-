def evaluate(pred, gt):
    if gt.lower() in pred.lower():
        return 1
    return 0
