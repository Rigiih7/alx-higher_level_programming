#!/usr/bin/node
const process = require('process');
const fs = require('fs');


// File path
const file = process.argv[2];
// string to write
const text = process.argv[3];
fs.writeFile(file, text, 'utf8', function (err, data) {
  // If an error occurred during while writing, print the error object
  if (err) {
    console.log(err);
  }
});
