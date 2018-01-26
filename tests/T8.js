var x = "str1:str2";
x.taint();
assert(x.isTainted());
var y = x.split(":");
assert(y[0].isTainted());
assert(y[1].isTainted());

success();