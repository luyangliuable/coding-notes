10            ; an atom; it evaluates to itself
:thing        ; another atom; evaluating to the symbol :thing
t             ; another atom, denoting true
(+ 1 2 3 4)   ; an s-expression
'(4 :foo t)   ; another s-expression

(defun meaning (life)
  "Return the computed meaning of LIFE"
  (let ((meh "abc"))
    ;; Invoke krakaboom
    (loop :for x :across life
          :collect x)))

(meaning 123)

(concatenate 'string "Hello, " "world!") ; => "Hello, world!"
(elt "Apple" 0) ; => #\A

(let ((me "dance with you")) me) ; => "dance with you"
(cons 1 (cons 2 (cons 3 nil)))

(append '(1 2) '(3 4))
(cons 1 (cons 2 (cons 3 nil)))
(concatenate 'list '(1 2) '(3 4))

;;; Vectors

;;; Vector's literals are fixed-length arrays

#(1 2 3) ; => #(1 2 3)

;;; Use CONCATENATE to add vectors together

(concatenate 'vector #(1 2 3) #(4 5 6)) ; => #(1 2 3 4 5 6)

;;; Adjustable vectors

;;; Adjustable vectors have the same printed representation as
;;; fixed-length vector's literals.

(defparameter *adjvec* (make-array '(3) :initial-contents '(1 2 3)
                                   :adjustable t :fill-pointer t))
*adjvec* ; => #(1 2 3)

(lambda () "Hello World")

(funcall (lambda () "Hello World"))


(defun hello-world () "Hello World")
(hello-world) ; => "Hello World"

;; Evaluates to some symbol (not a keyword)
(defun lennys-favorite-food ()
  ;; put your symbol here
  (intern "LASAGNA")
  )

(lennys-favorite-food)

;; Evaluates to some keyword
(defun LENNYS-SECRET-KEYWORD ()
  ;; put your keyword here
  ":ALIENS-ARE-REAL"
  )

(LENNYS-SECRET-KEYWORD)
(KEYWORDP (LENNYS-SECRET-KEYWORD))

(symbolp (lennys-favorite-food))


(defun test2 (n)
  (loop :for result = (list) :then (return i)
        :for i :in n
        :finally (return result)))

(test2 '( 10 2 3 10 ))


( first-thing '(0 1 2) )

(defun LENNYS-SECRET-KEYWORD ()
  :ALIENS-ARE-REAL
  )

( LENNYS-SECRET-KEYWORD )

(KEYWORDP (LENNYS-SECRET-KEYWORD))

