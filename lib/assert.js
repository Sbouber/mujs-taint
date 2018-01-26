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