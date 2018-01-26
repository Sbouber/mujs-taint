var x = "strrr";
x.taint();
assert(x.isTainted());
var y = x.slice(2);
assert(y.isTainted());

success();