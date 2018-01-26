import os

binary = "./mujs/build/release/mujs"
lib = ""

fail = False

for f in os.listdir("lib"):
	lib += open("lib/" + f, "r").read()


for f in os.listdir('tests'):
	print("============================ Running %s ============================" % f)
	out = open("testcase.js", "w")
	out.write(lib + "\n" + open("tests/" + f, "r").read())
	out.close()

	ret = os.system(binary + " testcase.js")

	if ret == 0:
		print("Testcase [%s]: PASSED\n" % f)
	else:
		print("Testcase [%s]: FAILED\n" % f)
		fail = True

	print("=======================================================================")

if fail:
	exit(1)
else:
	exit(0)