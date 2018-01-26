#!/usr/bin/env python



# TODO python bindings for mujs
# interp = MuJS()
# interp.run("var a = 1;")
# interp.addfunc()
# interp.ontaint(cb)


import ctypes


class MuJS(object):

	def __init__(self):

		self.lib = ctypes.CDLL("mujs/build/release/libmujs.so")
		self.state_ptr = self.lib.js_newstate(None, None, 0)

		self.lib.js_dostring.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
		self.lib.js_dofile.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
		self.lib.js_newcfunction.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
		self.lib.js_setglobal.argtypes = [ctypes.c_char_p]

	def run(self, s):
		self.lib.js_dostring(self.state_ptr, s.encode("utf-8"))

	def runfile(self, f):
		self.lib.js_dofile(self.state_ptr, f.encode("utf-8"))

	def addfunc(self, cb, name, argcount):

		# Todo:
		# - register cb_wrapper as a cfunction with name as name
		# - use setglobal
		# - cb_wrapper should grab argcount args from the stack, convert to python types
		# - then call the given cb with args
		# - grab the return value and convert it to a JsValue

		def cb_wrapper():
			pass





def js_func(x,y):
	print(x)
	print(y)

if __name__ == "__main__":
	interp = MuJS()
	interp.run("var x = 10; var y = 20;")
	interp.addfunc(js_func, "js_func", 2)
	interp.run("js_func(x, y);")