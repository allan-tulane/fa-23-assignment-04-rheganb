import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    a = len(S)
    b = len(T)
  
    fast_m = [[0 for j in range(b+1)] for i in range(a+1)] #fill MED bottom up
  
    for x in range(a+1):
      for y in range(b+1):
        if x == 0:
          fast_m[x][y] = y #the minimum operations is j
        elif y == 0:
          fast_m[x][y] = x
        elif S[x-1] == T[y-1]: #if last characters are the same
          fast_m[x][y] = fast_m[x-1][y-1]
        else: # if last characters are different
          fast_m[x][y] = 1 + min(fast_m[x-1][y], fast_m[x][y-1], fast_m[x-1][y-1])
    return fast_m[a][b]

def fast_align_MED(S, T, MED={}):
    fast_m = fast_MED(S, T)
    aligned_S = []
    aligned_T = []
  
    a = len(S)
    b = len(T)
  
  def fast_align_MED(S, T, fMED={}):
    # TODO - keep track of alignment
    fMED = fast_MED(S, T)
    S_align = []
    T_align = []
    i = len(S)
    j = len(T)

    while i > 0 or j > 0:
        insert = fMED[i][j - 1] if j > 0 else float('inf')
        remove = fMED[i - 1][j] if i > 0 else float('inf')
        sub = fMED[i - 1][j - 1] if i > 0 and j > 0 else float('inf')

        minimum = min(insert, remove, sub)

        if sub == minimum:
            S_align = [S[i - 1]] + S_align
            T_align = [T[j - 1]] + T_align
            i -= 1
            j -= 1
        elif insert == minimum:
            S_align = ['-'] + S_align
            T_align = [T[j - 1]] + T_align
            j -= 1
        elif remove == minimum:
            T_align = ['-'] + T_align
            S_align = [S[i - 1]] + S_align
            i -= 1

    s_str = ""
    t_str = ""
    s_str = s_str.join(S_align)
    t_str = t_str.join(T_align)

    return s_str, t_str


def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
