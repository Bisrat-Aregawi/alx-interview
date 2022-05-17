#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharsList (_, __, body) {
  const info = JSON.parse(body).characters;
  handleCharsList(info);
}

request(url, getCharsList);

function handleCharsList (value) {
  const arr = [];

  const printCharsList = (value2, idx, charCount) => {
    arr.push([value2, idx]);
    if (arr.length === charCount) {
      const newArr = arr.sort((a, b) => a[1] - b[1]);
      for (let i = 0; i < newArr.length; i++) {
        console.log(newArr[i][0]);
      }
    }
  };
  for (let i = 0; i < value.length; i++) {
    const handleCharsName = (_, __, body) => {
      const info = JSON.parse(body).name;
      printCharsList(info, i, value.length);
    };
    request(value[i], handleCharsName);
  }
}
