;; File: square-numbers.lisp
;; Author: Luyang Liu
;; Description: A LISP code to square numbers using the mapcar function

(mapcar #'(lambda (x) (* x x)) '(1 2 3 4 5))
;; Output: (1 4 9 16 25)
