#!/usr/bin/node

const { argv } = process;

const firstarg = parseInt(argv[2]);

if (firstarg) {
  console.log(`My number: ${firstarg}`);
} else {
  console.log('Not a number');
}
