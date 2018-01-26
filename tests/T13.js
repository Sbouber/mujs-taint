var x = "str";
x.taint();
assert(x.isTainted());
var y = x.charAt(0);
assert(y.isTainted());

success();