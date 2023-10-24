#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const webpage = process.argv[2];
const file = process.argv[3];
request.get(webpage).pipe(fs.createWriteStream(file));
