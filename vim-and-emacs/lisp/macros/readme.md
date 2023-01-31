# Lisp Macros

* Allow you to write your own control structures in the language
* They are used to write abstractions that simplify complex tasks
* Macros are executed during the compilation phase, so they can be used to generate code before it is executed
* A common use of macros is to define a domain-specific language (DSL) for a specific task or application
* Macros can also be used to improve performance by generating more optimized code for a specific use case
* Macros can be used to define custom control structures like loops, conditionals, and other types of program flow.

```
(defmacro when-let (binding-form &body body)
  `(let ,binding-form
     (when ,(first binding-form)
       ,@body)))

(when-let ((x (some-function)))
  (do-something x))
```
