(defpackage :lillys-lasagna
  (:use :cl)
  (:export :expected-time-in-oven
           :remaining-minutes-in-oven
           :preparation-time-in-minutes
           :elapsed-time-in-minutes))

(in-package :lillys-lasagna)

(defun expected-time-in-oven ()
  "Define function expected-time-in-oven"
  (print 337)
)

(expected-time-in-oven)

(defun remaining-minutes-in-oven (time)
  "Define function remaining-minutes-in-oven"
  (- 337 time)
)

(remaining-minutes-in-oven 100)

(defun preparation-time-in-minutes (layers)
  "Define function preparation-time-in-minutes"
  (* layers 19)
)

(preparation-time-in-minutes 3) ;; => 57

(defun elapsed-time-in-minutes (layers minutes) "Define function elapsed-time-in-minutes" (+ (* layers 19) minutes))

(defun add-nums (x y) "Add X and Y together" (+ x y))
(DOCUMENTATION 'add-nums 'FUNCTION)

(elapsed-time-in-minutes 3 100)
 
