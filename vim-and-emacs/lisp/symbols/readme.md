# Symbols
In Common Lisp, symbols are a data type used for naming variables, functions, and other entities. Symbols serve as a way to label values and provide a means of identifying and referring to them.

Here's an example of using symbols in Common Lisp:

```lisp
;; Define a symbol "x" and assign it a value of 5
(setf x 5)

;; Retrieve the value of symbol "x"
(print x) ; Output: 5

;; Define a symbol "square" and assign it a function that calculates the square of a number
(defun square (x) (* x x))

;; Call the "square" function using the symbol
(print (square x)) ; Output: 25

```

In this example, the symbol "x" is used both as a variable and as an argument to the "square" function. The symbol "square" is used to refer to the function, which can then be called using the symbol as the function name.

## Symbol vs Variable
In Lisp, symbols serve as a representation of a named entity, while variables serve as a means of storing values.

Symbols are used to refer to objects, functions, or values. For example, a symbol such as 'x refers to the named entity "x". A symbol can also be used as a function name or as an argument to a function. For example, (+ 1 2) calls the "+" function with arguments 1 and 2.

Variables, on the other hand, store values that can change at runtime. For example, (setf x 5) assigns the value 5 to the variable x. The value of a variable can be accessed using its symbol, such as x.

In summary, symbols in Lisp are used to refer to entities, while variables are used to store values that can change at runtime.
