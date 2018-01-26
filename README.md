# mujs-taint (WIP)
Taint tracking for mujs

This modification of mujs adds basic taint tracking to variables (just strings for now). Taint is currently not applied on a byte level.

## The following function can be used to apply taint to a variable:

``
Object.prototype.taint()
``

## The following function can be used to check if a variable is tainted:

``
Object.prototype.isTainted()
``

## Taint propagation rules:

`` T + x ---> T``

`` x + T --> T ``

`` T.toString() --> T ``

`` T.concat(x) --> T ``

`` x.concat(T) --> T ``

`` T.split(x) --> [T] ``

`` T.toLowerCase() --> T ``

`` T.toUpperCase() --> T ``

`` T.trim() --> T ``

## Use cases

### Dom based XSS
This taint tracker could be used to detect DOM-based XSS, such as

``
var x = tainted_user_input.split(a)[1];

var y = x.trim();

$(z).html(y);
``
