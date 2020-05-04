import re

import numpy as np

print('=====================tf========================')
documents_list = list()
with open('./tf-idf.dat', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        line = re.sub('[^A-Za-z\s]', ' ', line)
        line = line.lower()
        documents_list.append(line.split())

terms = list()
for document in documents_list:
    for term in document:
        if term not in terms:
            terms.append(term)
print(terms)

tf = list()
for document in documents_list:
    temp = [0] * len(terms)
    for term in document:
        temp[terms.index(term)] += 1
    tf.append(temp)

for count in tf:
    print(count)
print('================================================')
print('')
print('')
print('')
print('=====================Normalized========================')
normalized_tf = list()
print(terms)
for document in tf:
    max_value = max(document)
    document = list(map(lambda x: x / max_value, document))
    normalized_tf.append(document)

for count in normalized_tf:
    print(np.around(count, decimals=3))
print('================================================')
print('')
print('')
print('')
print('=====================Normalized========================')



print('================================================')
