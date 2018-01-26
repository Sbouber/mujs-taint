var x = "str";
x.taint();
assert(x.isTainted());
var y = x.toString();
assert(y.isTainted());

success();