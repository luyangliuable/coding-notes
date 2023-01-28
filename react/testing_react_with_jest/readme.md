# Testing React with Jest

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Testing React with Jest](#testing-react-with-jest)
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

```sh
mkdir __tests__
```

## Syntax
```js
function filterByTerm(inputArr, searchTerm) {
  return inputArr.filter(function(arrayElement) {
    return arrayElement.url.match(searchTerm);
  });
}

describe("Filter function", () => {
  test("it should filter by a search term (link)", () => {
    const input = [
      { id: 1, url: "https://www.url1.dev" },
      { id: 2, url: "https://www.url2.dev" },
      { id: 3, url: "https://www.link3.dev" }
    ];

    const output = [{ id: 3, url: "https://www.link3.dev" }];

    expect(filterByTerm(input, "link")).toEqual(output);
  });
});
```

## References
https://www.valentinog.com/blog/jest/
