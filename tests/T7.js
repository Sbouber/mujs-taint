var x = "str";
assert(!x.isTainted());
var y = "stuff";
y.taint();
var z = x.concat(y);
assert(z.isTainted());

success();