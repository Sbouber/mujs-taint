var loc = location.href;
var h = loc.split("#")[1];
var a = "stuff";
if (a != "stuff")
{
	a = "a" + stuff;
} else {
	var ele = $(".someclass");
	ele.html(h); // XSS
}