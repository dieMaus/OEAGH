import objPais
import pickle
import btree as b

btree = b.BTree(4)
binaries = open('binaries.kbb', 'rb')
arq = open('tourism.pkl', 'wb')

for i in range(1, 196):
    pais = pickle.load(binaries)
    print (pais.name)
    btree.insert([pais.tourism, pais.name, i])

pickle.dump(btree, arq)

binaries.close()
arq.close()
