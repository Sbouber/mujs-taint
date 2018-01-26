var x = "str";
assert(!x.isTainted());
x.taint();
assert(x.isTainted());
var y = 1 + x;
assert(y.isTainted());
var z = "str2" + x;
assert(z.isTainted());

success();