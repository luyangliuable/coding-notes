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

## Functions as parameters


```javascript
const timeFuncRuntime = funcParameter => {
   let t1 = Date.now();
   funcParameter();
   let t2 = Date.now();
   return t2 - t1;
}
 
const addOneToOne = () => 1 + 1;
 
timeFuncRuntime(addOneToOne);
```

```javascript
timeFuncRuntime(() => {
  for (let i = 10; i>0; i--){
    console.log(i);
  }
});
```
