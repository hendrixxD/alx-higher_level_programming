//foo.js
foo = function() {
    console.log('foo!');
}

//app.js
require('./foo.js'); //including the function foo with the require function
foo();
