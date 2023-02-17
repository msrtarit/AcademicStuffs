from math import log

from numpy import argmax, array


def beam_search_decoder(data, k):
    sequences = [[list(), 0.0]]
   
    for row in data:
        all_candidates = list()
       
        for i in range(len(sequences)):
            seq, score = sequences[i]
            for j in range(len(row)):
                candidate = [seq + [j], score - log(row[j])]
                all_candidates.append(candidate)
       
        ordered = sorted(all_candidates, key=lambda tup: tup[1])
     
        sequences = ordered[:k]
    return sequences



data = [[12, 15, 10, 7, 14],
        [13, 18, 13, 20, 5],
        [17, 9, 23, 24, 19],
        [7, 14, 16, 12, 34],
        [20, 5, 23, 13, 18]]
data = array(data)

result = beam_search_decoder(data, 3)

for seq in result:
    print(seq)
