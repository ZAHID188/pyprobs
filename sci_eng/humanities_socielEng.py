




from nltk.corpus import inaugural
from nltk.probability import *
cfd = ConditionalFreqDist((fileid, len(w))
for fileid in inaugural.fileids()
for w in inaugural.words(fileid)
if fileid > '1980' and fileid < '2010')
print(cfd.items())
cfd.plot()







"""
inaugural
look at the frequency function to found "freedom" word and it's frequency

"""

# from nltk.corpus import inaugural
# from nltk.probability import *
# fd3 = FreqDist([s for s in inaugural.words()])
# print(fd3.freq('freedom'))


'''
look the most used data in the graph and exact number
'''

# from nltk.corpus import gutenberg
# from nltk.probability import *
# allwords = gutenberg.words('shakespeare-hamlet.txt')
# fd2 = FreqDist([sx.lower() for sx in allwords if sx.isalpha()])
# print(fd2.B())
# print(fd2.N())
# fd2.tabulate(20)
# fd2.plot(20)
# fd2.plot(20, cumulative = True)



"""
books text=shakespeare-hamlet.txt
"""

# from nltk.corpus import gutenberg
# allwords = gutenberg.words('shakespeare-hamlet.txt')
# print(len(allwords))
# print(allwords.count("Hamlet"))

# A = set(allwords)
# longwords = [w for w in A if len(w) > 12]
# print(sorted(longwords))



"""
books
"""

# from nltk.corpus import gutenberg
# print(gutenberg.fileids())







