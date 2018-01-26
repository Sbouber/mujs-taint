var x = "str";
x.taint();
assert(x.isTainted());
var y = x.valueOf();
assert(y.isTainted());

success();