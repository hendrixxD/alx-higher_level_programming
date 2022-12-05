#!/usr/bin/node
// prints a factorial of a number

const num = parseInt(process.argv[2]);

function factorialix (num) {
  if (isNaN(num) || num === 0) {
    return (1);
  }
  if (num < 0) {
    return (-1);
  }
  return (num * factorialix(num - 1));
}
console.log(Number(factorialix(num)));
