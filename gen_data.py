import sys
import random


qa = dict()

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        q, a, sim_q = line.split('\t')
        qa[q] = a

for q, a in qa.items():
    tmp = list(qa.values())
    tmp.remove(a)
    cand_q = random.sample(tmp, 20)
    print('1' + '\t' + q + '\t' + a)
    for i in cand_q:
        print('0' + '\t' + q + '\t' + i)

