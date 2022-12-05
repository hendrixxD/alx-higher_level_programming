#!/usr/bin/node
// prints a factorial of a number

const num = parseInt(process.argv[2], 10);

function factorialix(num) {
    if (isNaN(num) || num === 0) {
        console.log(1);
    }
    return (num * factorialix(num -1));
}
console.log(factorialix(num));