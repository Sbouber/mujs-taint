function assert(x)
{
	if (!x) {
		print(new Error("Assertion Failure!\n"));
		quit(1);
	}
}

function success()
{
	quit(0);
}
var x = "str";
x.taint();
assert(x.isTainted());
var y = x.trim();
assert(y.isTainted());

success();