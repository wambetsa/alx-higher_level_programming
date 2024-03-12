#!/usr/bin/node
// a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const num = Number(process.argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
