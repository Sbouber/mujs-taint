#!/usr/bin/env python



# TODO python bindings for mujs
# interp = MuJS()
# interp.run("var a = 1;")
# interp.addfunc()
# interp.ontaint(cb)


import ctypes
import jsbeautifier


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

	interp.ontaint(taint_cb)

	interp.runf("lib/assert.js")
	interp.runf("lib/browser.js")
	interp.run(jsfile)