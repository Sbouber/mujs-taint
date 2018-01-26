var x = "str";
x.taint();
assert(x.isTainted());
var y = x.toLowerCase();
assert(y.isTainted());

success();