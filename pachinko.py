def eval_pachinko_helper(pachinko, score, i):
    if pachinko is None or i == -1 or pachinko == '':
        return 0
    if i > len(pachinko) - 1:
        return score
    if pachinko[i] == '.':
        return eval_pachinko_helper(pachinko, score, i+1)
    if pachinko[i] == '_':
        return eval_pachinko_helper(pachinko, score, i+1)
    if pachinko[i] == '/':
        return eval_pachinko_helper(pachinko[:i], 0, i-1) + eval_pachinko_helper(pachinko, score, i+1)
    if pachinko[i] == '\\':
        return eval_pachinko_helper(pachinko[i+1], 0, 0) + eval_pachinko_helper(pachinko, score, i+1)

def eval_pachinko(pachinko):
    return eval_pachinko_helper(pachinko, 0, 0) / len(pachinko)