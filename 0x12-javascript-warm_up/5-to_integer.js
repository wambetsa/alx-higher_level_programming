#!/usr/bin/node
// Prints two arguments passed to it, in the following format: “ is ”

// Get the first argument from the command line
const arg = process.argv[2];

// Convert the argument to an integer using parseInt
const num = parseInt(arg);

// Check if the argument can be converted to an integer
if (!isNaN(num)) {
  // If it can be converted, print "My number: <integer>"
  console.log(`My number: ${num}`);
} else {
  // If it can't be converted, print "Not a number"
  console.log("Not a number");
}