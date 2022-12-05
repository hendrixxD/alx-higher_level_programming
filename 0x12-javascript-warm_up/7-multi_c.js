#!/usr/bin/node

require('process');

const arg = process.argv;
let num;

if (arg.length === 2) {
  console.log('Missing number of occurences');
} else {
  num = parseInt(arg[2]);
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
