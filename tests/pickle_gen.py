#!/usr/bin/env python3

import pickle
import base64

def moo():
	print('moo')

f = open('example_pickle.bpkl', 'w')
m = pickle.dumps(moo)
f.write(base64.b64encode(m).decode())
f.close()