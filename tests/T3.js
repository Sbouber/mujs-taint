var x = "str";
assert(!x.isTainted());
var y = "str2";
y.taint();
assert(y.isTainted());
x = y;
assert(x.isTainted());

success();