var x = "str";
x.taint();
assert(x.isTainted());
var y = x.toUpperCase();
assert(y.isTainted());

success();