#!/usr/bin/env python

import ctypes
import jsbeautifier


# TODO
# implement the following legacy functions:
#
# 1) Object.prototype.__defineGetter__()
# 2) Object.prototype.__defineSetter__()
# 3) Object.prototype.__lookupGetter__()
# 4) Object.prototype.__lookupSetter__()
#



class MuJS(object):

	def __init__(self):

		self.lib = ctypes.CDLL("mujs/build/release/libmujs.so")
		self.state_ptr = self.lib.js_newstate(None, None, 0)

		self.lib.js_dostring.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
		self.lib.js_dofile.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
		self.lib.js_newcfunction.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
		self.lib.js_setglobal.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

	def run(self, s):
		self.lib.js_dostring(self.state_ptr, s.encode("utf-8"))

	def runfile(self, f):
		self.lib.js_dofile(self.state_ptr, f.encode("utf-8"))

	def addfunc(self, cb, name, argcount):

		@ctypes.CFUNCTYPE(None)
		def cb_wrapper():
			print("cb_wrapper called")

			# TODO:

			# grab argcount args

			# convert to python values

			# call cb with args

		self.lib.js_newcfunction(self.state_ptr, cb_wrapper, name.encode("utf-8"), argcount)
		self.lib.js_setglobal(self.state_ptr, name.encode("utf-8"))





def js_func(x,y):
	print(x)
	print(y)

if __name__ == "__main__":
	interp = MuJS()
	jsfile = open("examples/domxss1.js", "r").read()
	jsfile = jsbeautifier.beautify(jsfile)

	def taint_cb(line_no, jsval):
		pass

	interp.on_taint_apply(taint_apply_cb)
	interp.on_taint_eq(taint_eq_cb)
	interp.on_taint_cmp(taint_cmp_cb)

	interp.runf("lib/assert.js")
	interp.runf("lib/env.js")
	interp.run(jsfile)