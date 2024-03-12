#!/usr/bin/node
/*
A script that concats 2 files.
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const file = require('fs');
const fileA = file.readFileSync(process.argv[2], 'utf8');
const fileB = file.readFileSync(process.argv[3], 'utf8');
file.writeFileSync(process.argv[4], fileA + fileB);
