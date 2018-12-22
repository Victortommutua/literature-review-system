from itertools import combinations

f = open("keywords.txt",'r')

fin = open("out_text.txt",'r')

alltext = fin.read()
alltext = alltext.lower()


phrases = ['in this paper','in this ','in this study','our research','this paper proposes','this novel','this paper','this paper aimed','we describe','this article', 'this article extends','this work examined','the present study','we present','the objective of this paper','we examine','this paper surveys','this paper conducted', 'this paper presents','we develop a novel approach','we develop','in this paper,we have proposed','this paper describe','in this domain', 'method proposed']

def rSubset(arr, r):   
	return list(combinations(arr, r)) 

def findWords(words):
	
	n = alltext.count(words)
#	print(words + " : " + str(n))
	return n



words = f.read()
words = words.split('\n')

tempwords = []
for j in words:
	if j != '':
		tempwords.append(j)

words = tempwords
	
print('\nCandidate words -> Occurences\n')


newList = []

for i in words:
	num = i.count(" ")+1
	number_occ = findWords(i)
	print(i+" -> "+str(number_occ))
	if number_occ > 1:
		newList.append(i)

	if num > 2:
		listword = i.split()
		combinations = rSubset(listword, 2)
		for comb in combinations:
			check = (" ".join(comb))
			number_occ = findWords(check)
			print(check+" -> "+str(number_occ))
			if number_occ > 1:
				newList.append(check)

print('\n Final Selected keywords:\n')

counter = 1

for items in newList:
	
	if items not in phrases:	
		print(str(counter) + " "+ items)
		counter+=1
		

