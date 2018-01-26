var x = "str";
x.taint();
assert(x.isTainted());
var y = x.toLocaleUpperCase();
assert(y.isTainted());

success();