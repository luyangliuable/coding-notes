# Testing React with Jest

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Testing React with Jest](#testing-react-with-jest)
    - [Setting Up the Project](#setting-up-the-project)
    - [Syntax](#syntax)
    - [References](#references)

<!-- markdown-toc end -->

## Setting Up the Project
* Get started
```sh
mkdir getting-started-with-jest && cd $_
npm init -y
```

* Install jest
```sh
npm i jest --save-dev
```

* Configure package json to run test command using jest
```json
  "scripts": {
    "test": "jest"
  },
```

* Create tests folder
```sh
mkdir __tests__
```

* Create test file
    * It is a convention borrowed from Ruby for marking the file as a specification for a given functionality.

```sh
touch ./__tests__/filterByTerm.spec.js
```

## Syntax
```js
// Import the 'expect' function from the 'jest' package 
const filterByTerm = require("../src/filterByTerm");
//...
const { expect } = require('jest');

/**
 * This function filters an array of objects by a search term, matching it against the 'url' property of each object.
 *
 * @param {Array} inputArr - The array of objects to filter
 * @param {string} searchTerm - The term to use as a filter
 * @returns {Array} - The filtered array
 */
function filterByTerm(inputArr, searchTerm) {
  return inputArr.filter(function(arrayElement) {
    return arrayElement.url.match(searchTerm);
  });
}

describe("Filter function", () => {
  test("it should filter by a search term (link)", () => {
    // Test input
    const input = [
      { id: 1, url: "https://www.url1.dev" },
      { id: 2, url: "https://www.url2.dev" },
      { id: 3, url: "https://www.link3.dev" }
    ];

    // Expected output
    const output = [{ id: 3, url: "https://www.link3.dev" }];

    // Assert that the function returns the expected output when called with the test input
    expect(filterByTerm(input, "link")).toEqual(output);
    expect(filterByTerm(input, "LINK")).toEqual(output);
  });
});

```

## References
https://www.valentinog.com/blog/jest/
