class Domino:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Chain:
    def __init__(self, dominos):
        self.dominos = dominos
    def topString(self):
        return str().join([domino.top for domino in self.dominos])
    def bottomString(self):
        return str().join([domino.bottom for domino in self.dominos])

# dominoList = [Domino('0','100'), Domino('01','00'), Domino('110', '11')] #To change dominos just use the Domino(top,bottom) constructor
                                                                         #in the list. 
dominoList = [Domino('MOM','M'), Domino('O', 'OMOMO')]
# dominoList = [Domino('AA','A')]

chains = [Chain([domino]) for domino in dominoList]
for element in [str([(domino.top, domino.bottom) for domino in chain.dominos])+'\n' for chain in chains]:
    print(element)
print('\n')

def expand(chain):
    for domino in dominoList:
        if domino == chain.dominos[-1]:
            continue
        newTopString = chain.topString() + domino.top
        newBottomString = chain.bottomString() + domino.bottom
        if newTopString == newBottomString:
            chains.append(Chain(chain.dominos + [domino]))
            print([(dom.top, dom.bottom) for dom in (Chain(chain.dominos + [domino])).dominos])
            print ('\nSUCCESS!\n' + 'Top String: ' + newTopString + '\n' + 'Bottom String: ' + newBottomString)
            quit()
        chains.append(Chain(chain.dominos + [domino]))
    chains.remove(chain)
    for element in [str([(domino.top, domino.bottom) for domino in chain.dominos])+'\n' for chain in chains]:
        print(element)
    print('\n')

def DFS(chainList):
    deepestChain = Chain([])
    for chain in chainList:
        if len(chain.dominos) > len(deepestChain.dominos):
            deepestChain = chain
    expand(deepestChain)

while chains:
    DFS(chains)