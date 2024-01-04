#!/usr/bin/node
const process = require('process');
const fs = require('fs');


const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  // If an error occurred during the reading, print the error object
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
