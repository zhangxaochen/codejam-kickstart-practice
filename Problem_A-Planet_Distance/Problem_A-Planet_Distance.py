#coding=utf-8

'Problem A. Planet Distance @https://code.google.com/codejam/contest/4384486/dashboard#s=p0'

from collections import Counter
from datetime import datetime

begt=datetime.now()

res_str_total=''

with open('A-small-practice.in') as fin:
    case_num = int(fin.readline())
    for case_idx in range(case_num):
        N = int(fin.readline())
        #print 'case_idx, N:', case_idx, N
        
        #nbr_lst = [set() for i in range(N)]
        nbr_lst = [[] for i in range(N)]
        deg_lst = [0] * N #degree
        
        INVALID_DIST = -1
        dist_lst = [INVALID_DIST] * N
        
        for i in range(N):
            a, b = map(int, fin.readline().split())
            nbr_lst[a-1].append(b)
            nbr_lst[b-1].append(a)
            deg_lst[a-1] += 1
            deg_lst[b-1] += 1
        #print 'nbr_lst', nbr_lst, deg_lst
        
        q = [] #elems with degree *1*
        for i in range(N):
            if len(nbr_lst[i]) == 1:
                q.append(i+1) #planet idx, starts from 1, not 0
        #print q

        while len(q) > 0:
            idx = q.pop(0)
            deg_lst[idx-1] -= 1
            for nbr_idx in nbr_lst[idx-1]:
                deg_lst[nbr_idx-1] -= 1
                if deg_lst[nbr_idx-1] == 1:
                    q.append(nbr_idx)
        #print deg_lst
        
        for i, deg in enumerate(deg_lst):
            if deg > 0:
                q.append(i+1)
                dist_lst[i] = 0 #node (i+1) is in cycle, dist is 0
        
        while len(q) > 0:
            idx = q.pop(0)
            for nbr_idx in nbr_lst[idx-1]:
                if dist_lst[nbr_idx-1] == INVALID_DIST:
                    dist_lst[nbr_idx-1] = dist_lst[idx-1] + 1
                    q.append(nbr_idx)
        #print 'dist_lst', dist_lst

        #print 'Case #%d:' % case_idx+1, ' '.join(map(str, dist_lst))
        res_str_total += 'Case #%d: %s\n' % (case_idx+1, ' '.join(map(str, dist_lst)) )
        
with open('res.x', 'w') as fout:
    fout.write(res_str_total)

print 'time cost: %ds'% (datetime.now()-begt).total_seconds()