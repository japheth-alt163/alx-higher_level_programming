#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

const contentA = fs.readFileSync(fileAPath, 'utf-8');
const contentB = fs.readFileSync(fileBPath, 'utf-8');

const concatenatedContent = `${contentA}${contentB}`;

fs.writeFileSync(fileCPath, concatenatedContent);
