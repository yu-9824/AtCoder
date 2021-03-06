def LI(): return list(map(int, input().split()))

import sys
sys.setrecursionlimit(10 ** 9)

'''
# 思ったこと
事前に縦と横の合計しらべればいいのでは？そのあと取り出すイメージ．
O(HW)でもギリいける?

横着してnumpy + numbaでやろうとするとTLE(cache=Trueで14AC, 2TLE)
横着しなくてもTLE(なんなら10AC, 6TLEなので結果が悪い)
PyPyで8AC, 8TLEで解決できない．

解答をみる: https://twitter.com/e869120/status/1378115289649348611
やり方は完全にあっている．ただ，できない．

*** sum(list(*A))がめちゃくちゃ重かったっぽい．***
参考: https://gitlab.com/w0mbat/kyopro_educational_90/-/blob/main/004.py
'''

# https://atcoder.jp/contests/typical90/tasks/typical90_d

def main(*args):
    H, W, A = args

    sum_W = [sum(A[h][w] for h in range(H)) for w in range(W)] # sum(list(*A))でtranspose()している．←これがTLEの元凶だったっぽい．これを変えて，PyPyにしたところめっちゃ早くなった．listからジェネレータによる計算に変わったことが要因？
    sum_H = [sum(A[h]) for h in range(H)]
    
    [print(*[str(sum_W[w] + sum_H[h] - A[h][w]) for w in range(W)]) for h in range(H)]
    

if __name__ == '__main__':
    H, W = LI()
    A = [LI() for h in range(H)]
    main(H, W, A)

