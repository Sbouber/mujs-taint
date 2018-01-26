var loc = location.href;
var h = loc.split("#")[1];
var a = "stuff";
if (a != "stuff")
{
	a = "a" + stuff;
} else {
	var ele = $(".someclass");
	ele.html(h); // XSS #1
}

if (window.location.search.slice(1).split("=")[1] == "somevalue") // Tainted value is compared
{
	document.write(window.location.search); // XSS #2
}