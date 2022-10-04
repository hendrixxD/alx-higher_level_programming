#!/usr/bin/node

require('process');

let argvLen = process.argv.length - 2;

if (argvLen > 1) {
    console.log('Arguments found');
} else if (argvLen == 1) {
    console.log('Argument Found');
} else {
    console.log('No Argument');
}

