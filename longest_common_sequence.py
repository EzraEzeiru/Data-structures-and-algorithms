def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if len(seq1) == idx1 or len(seq2) == idx2:
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)

print(lcs_recursive("great", "treat"))


def max_profit_recursive(profits, weights, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(profits, weights, capacity, idx+1)
    else:
        option1 = max_profit_recursive(profits, weights, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(profits, weights, capacity-weights[idx], idx+1)
        return max(option1, option2)
