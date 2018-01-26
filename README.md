# mujs-taint (WIP)
Taint tracking for MuJS

This modification of MuJS adds basic taint tracking to variables (just strings for now). Taint is currently not applied on a byte level.

## The following function can be used to apply taint to a variable:

``
Object.prototype.taint()
``

## The following function can be used to check if a variable is tainted:

``
Object.prototype.isTainted()
``

## Taint propagation rules:

**T0** `` T + x ---> T``

**T1** `` x + T --> T ``

**T2** `` T.toString() --> T ``

**T3** `` T.concat(x) --> T ``

**T4** `` x.concat(T) --> T ``

**T5** `` T.split(x) --> [T] ``

**T6** `` T.toLowerCase() --> T ``

**T7** `` T.toUpperCase() --> T ``

**T8** `` T.trim() --> T ``

## Use cases

### Dom based XSS
This taint tracker could be used to detect DOM-based XSS, such as

```javascript
var x = tainted_user_input.split(a)[1];

var y = x.trim();

$(z).html(y);
```

## Limitations

MuJS implements ES5, so not all javascript code can be passed into MuJS. There are some ES6->ES5 compilers available to overcome this limitation.
