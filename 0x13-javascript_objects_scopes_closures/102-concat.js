#!/usr/bin/node
const fs = require('fs');
let data = '';
data = fs.readFileSync(process.argv[2]).toString();
data += fs.readFileSync(process.argv[3]).toString();
fs.writeFile(process.argv[4], data, 'utf8', (err) => {
  if (err) {
    console.error('Error reading the file:', err);
  }
});
