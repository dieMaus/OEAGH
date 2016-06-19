import btree as b
import pickle
from operator import itemgetter

arq = open('tourism.pkl', 'rb')

btree = pickle.load(arq)
lista = []
lista = btree.crescent(btree._root, lista)
print (lista)
arq.close()
