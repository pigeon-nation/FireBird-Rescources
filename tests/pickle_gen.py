#!/usr/bin/env python3

import pickle

def moo():
	print('moo')

f = open('example_pickle.pkl', 'wb')
pickle.dump(moo, f)
f.close()