#!/usr/bin/node

const { argv } = process;

const convertedInt = parseInt(argv[2]);
if (convertedInt) {
  for (let x = 0; x < convertedInt; x++) {
    let square = '';
    for (let y = 0; y < convertedInt; y++) {
      square = square + 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
