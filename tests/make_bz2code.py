#!/usr/bin/env python3

import bz2
import inspect

def moo():
	print('moo')
	
code = inspect.getsource(moo)
cmp = bz2.compress(code.encode())

with open('code.cmp', 'wb') as file:
	file.write(cmp)