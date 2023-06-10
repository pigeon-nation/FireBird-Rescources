#!/usr/bin/env python3

import pickle

def moo():
	print('moo')

f = open('example_pickle.pkl', 'wb')
m = pickle.dumps(moo)
f.write(m)
f.close()