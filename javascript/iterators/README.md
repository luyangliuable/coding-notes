# Iterators

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Iterators](#iterators)
    - [Functions as data](#functions-as-data)

<!-- markdown-toc end -->


## Functions as data

In JavaScript functions are **first-class objects**. This means that, like other objects you’ve encountered, JavaScript functions can have properties and methods.

```javascript
const announceThatIAmDoingImportantWork = () => {
    console.log("I’m doing very important work!");
};

const busy = announceThatIAmDoingImportantWork;

busy(); // This function call barely takes any space!
```

## 
