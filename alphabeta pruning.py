import math 
def alpha_beta(depth,nodeindex,maximizingplayer,values,alpha,beta,height):
    
    if depth == height:
        return values[nodeindex]
 
    if maximizingplayer:
        best = -math.inf
 
        for i in range(0, 2):
            val = alpha_beta(depth + 1, nodeindex * 2 + i, False, values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
 
            if beta <= alpha:
                break
 
        return best
 
    else:
        best = math.inf
 
        for i in range(0, 2):
            val = alpha_beta(depth + 1, nodeindex * 2 + i, True, values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
 
            if beta <= alpha:
                break
 
        return best
   