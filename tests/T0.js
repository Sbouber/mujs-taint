var x = "str";
assert(!x.isTainted());
x.taint();
assert(x.isTainted());
var y = x + 1;
assert(y.isTainted());
var z = x + "str2";
assert(z.isTainted());

success();