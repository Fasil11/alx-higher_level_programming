#!/usr/bin/node

const name = process.argv[2]

if (!name) {
    console.log("please provide a name");
} else {
    console.log('Hello, ${name}');
}
