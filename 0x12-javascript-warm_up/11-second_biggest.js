#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const max = Math.max(...numbers);
  const filteredNumbers = numbers.filter((num) => num !== max);
  const secondMax = Math.max(...filteredNumbers);
  console.log(secondMax);
}
