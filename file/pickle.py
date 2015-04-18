__author__ = 'Administrator'

'''
    pickle 储存python原生对象
    有错
'''

D = {'a': 1, "b": 2}
F = open("c:\\D.pk", 'wb')
import pickle
pickle.dump(D, F)
F.close()
