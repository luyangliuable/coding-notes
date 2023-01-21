;; This program checks if the argument is an atom
;; Author: Luyang Liu
;; Date: 2023-01-01

;; Evaluates to T if THING is an atom, NIL otherwise
(defun is-an-atom-p (thing)
  ;; put the code to determine if THING is a CONS here
  (if  (atom thing)
       T
       Nil))
