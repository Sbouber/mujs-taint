var x = "str";
x.taint();
assert(x.isTainted());
var y = x.toLocaleLowerCase();
assert(y.isTainted());

success();