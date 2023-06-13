#!/usr/bin/node
const argument = process.argv[2];

const parsedArgument = parseInt(argument);

if (!isNaN(parsedArgument)) {
  console.log("My number: " + parsedArgument);
} else {
  console.log("Not a number");
}

