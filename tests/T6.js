var x = "str";
x.taint();
assert(x.isTainted());
var y = x.concat("stuff");
assert(y.isTainted());

success();