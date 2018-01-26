[![Build Status][build-status-img]][travis-ci]

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

**T1** `` x + T ---> T ``

**T2** `` T = x ---> x ``

**T3** `` x = T ---> T ``

**T4** `` new String(T) ---> T ``

**T5** `` T.toString() ---> T ``

**T6** `` T.concat(x) ---> T ``

**T7** `` x.concat(T) ---> T ``

**T8** `` T.split(x) ---> [T] ``

**T9** `` T.toLowerCase() ---> T ``

**T10** `` T.toUpperCase() ---> T ``

**T11** `` T.trim() ---> T ``

**T12** `` T.valueOf() ---> T ``

**T13** `` T.charAt(x) ---> T ``

**T14** `` T.toLocaleLowerCase() ---> T ``

**T15** `` T.toLocaleUpperCase() ---> T ``

**T16** `` T.slice(x,y) ---> T ``

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

[build-status-img]: https://travis-ci.org/Sbouber/mujs-taint.svg?branch=master
[travis-ci]: https://travis-ci.org/Sbouber/mujs-taint