function assert(b) {
	if (!b) {
		print("FALSE\n");
	} else {
		print("TRUE\n");
	}
}


function $(x) {
	if(x.isTainted()) {
		print("Tainted value passed to $: " + x);
	}
}

var jQuery = $;


var window = {};
var document = {};

var location = {href: "https://www.google.com", "hash": "#test", "host": "google.com"};
location.taint();
location.href.taint();
location.hash.taint();

var a = location;
assert(a.isTainted());

var b = location.href;
assert(b.isTainted());

var c = location.hash;
assert(c.isTainted());
var d = c.split("#")[1];
assert(d.isTainted());

var e = location.toString();
assert(e.isTainted());

var f = location.hash + "stuff";
assert(f.isTainted());

var g = location.hash + 1;
assert(g.isTainted());

var h = "stuff" + location.hash;
assert(h.isTainted());

var i = "stuff";
i.taint();
assert(i.trim().isTainted());

var j = "stuff";
assert(!j.trim().isTainted());

var k = "aaa";
k.taint();
assert(k.toUpperCase().isTainted());

var l = "zzz";
l.taint();
assert(l.concat("aaa").isTainted());

var m = "zzz";
m.taint();
assert("aaa".concat(m).isTainted());

var n = "aaa";
n.taint();
assert("z".concat(["a", "b", n]).isTainted());