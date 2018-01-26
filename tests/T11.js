var x = "str";
x.taint();
assert(x.isTainted());
var y = x.trim();
assert(y.isTainted());

success();