#!/usr/bin/node

const request = require('process')
const fs = require('fs');

const url = process.argv[1];

const fileStream = fs.createWriteStream(process.argv[2]);
request
    .get(url)
    .pipe(fileStream);
