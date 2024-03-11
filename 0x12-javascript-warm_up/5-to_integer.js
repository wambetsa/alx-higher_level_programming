#!/usr/bin/node
// Prints two arguments passed to it, in the following format: “ is ”

const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);