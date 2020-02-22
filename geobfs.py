words = "ABC CDE CFG EHE EIJ GHK GLC" #Put the word list here separated by spaces
# words = "ABC CDE CFG EHI GJC GKG"
wordList = words.split() 

class Chain:
    def __init__(self, chain, remainingWords):
        self.chain = chain
        self.remainingWords = remainingWords

chains = [Chain([word],[remWord for remWord in wordList if remWord != word]) for word in wordList]
print([chain.chain for chain in chains])

def expand(chain):
    if chain.remainingWords == []:
        print('\nSUCCESS: ' + str(chain.chain))
        quit()
    for word in chain.remainingWords:
        if chain.chain[-1][-1] == word[0]:
            remainingWords = [remWord for remWord in chain.remainingWords if remWord != word]
            chains.append(Chain(chain.chain + [word], remainingWords))
    chains.remove(chain)
    print([chain.chain for chain in chains])
    if not chains:
        print('\nFAILURE')

def BFS(chainList):
    expand(chainList[0])

while chains:
    BFS(chains)