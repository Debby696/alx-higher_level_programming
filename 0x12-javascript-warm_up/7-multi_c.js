#!/usr/bin/node

const { argv } = process;

const x = parseInt(argv[2]);

if (!x) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
