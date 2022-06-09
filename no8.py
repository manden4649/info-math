import numpy as np #使ってない

#標準入力非対応
#行列固定


#即席掛け算計算機
A = [[17,7],[24,19]]
B = [[20,21,12],[5,12,3]]
ans = [[0,0,0],[0,0,0]]
mod = 28
for i in range(3):
    for j in range(2):
        ans[j][i] = (A[j][0] * B[0][i]) + (A[j][1] * B[1][i])
        while ans[j][i] >= mod:
            ans[j][i] = ans[j][i] - mod

print(ans[0])
print(ans[1])
