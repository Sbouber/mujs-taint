var x = "str";
x.taint();
assert(x.isTainted());
var y = "str2";
assert(!y.isTainted());
x = y;
assert(!x.isTainted());