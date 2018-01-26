var x = "str";
x.taint();
assert(x.isTainted());
var y = new String(x);
assert(y.isTainted());

success();