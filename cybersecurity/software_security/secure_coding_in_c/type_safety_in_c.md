# Type Safety in C

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Type Safety in C](#type-safety-in-c)
    - [Type Safety](#type-safety)

<!-- markdown-toc end -->

* C/C++ is not type safe.
* They are designed for high performance.
    * Manual memory management.
* Typical enforcement of type safety is expensive.

## Type Safety
* Each data object is ascribed a type.
* Object are always compatible with its assigned type.
* Type safety is stronger than memory safety.

## Dynamically Typed Languages
* Do not require declarations the identify types, can be viewed as type safe.
  * Each object has on type (i.e. dynamic)
  * Each operand on a dynamic object is permitted but may be unimplemented (checked at runtime)
    * Object is able to respond to any method or operation that is called on it, but some of those methods or operations may not have any actual functionality.
    * This can occur in certain programming languages where objects can be defined as "dynamic", meaning that they are not bound to a specific set of methods or properties at compile-time, but can respond to any method or property that is called on them at runtime. 
    * In this case, if an operation is called on the object that has not been implemented, the object may simply return a default or null value, or it may throw an exception indicating that the operation is not supported.
