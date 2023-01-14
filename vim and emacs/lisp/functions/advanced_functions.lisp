(defpackage :lillys-lasagna-leftovers
  (:use :cl)
  (:export
   :preparation-time
   :remaining-minutes-in-oven
   :split-leftovers))

(in-package :lillys-lasagna-leftovers)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;           Preparation time                                                  ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Define function preparation-time
(defun preparation-time (&rest rest)
  "Define function preparation-time"
  (print (* (length rest) 19))
  )

(preparation-time 'sauce 'cheese 'right-handed-macaroni 'cheese 'sauce
                  'left-handed-macaroni 'sauce 'sauce 'cheese 'cheese)
;; => 190 (because there are 10 layers.)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                                        ;            Remaining time           ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defun remaining-minutes-in-oven (&optional ( opt :normal ))
  "This function calculates the remaining minutes in an oven for a given time option.
  The time option can be :normal, :shorter, :very-short, :longer, :very-long, or not passed at all.
  :normal returns 337.
  :shorter returns 237.
  :very-short returns 137.
  :longer returns 437.
  :very-long returns 537.
  If no option passed the function returns 0.
  Default option is :normal"
  (setq result 337)
  (cond ( (equal opt :normal) (print result))
        ( (equal opt :shorter) (print (- result 100)))
        ( (equal opt :very-short) (print (- result 200)))
        ( (equal opt :longer) (print (+ result 100)))
        ( (equal opt :very-long) (print (+ result 200)))
        ( (equal opt nil) (print 0) )
        ((print result))
        )
  )

(remaining-minutes-in-oven)             ;; => 337
(remaining-minutes-in-oven :normal)     ;; => 337
(remaining-minutes-in-oven :shorter)    ;; => 237
(remaining-minutes-in-oven :very-short) ;; => 137
(remaining-minutes-in-oven :longer)     ;; => 437
(remaining-minutes-in-oven :very-long)  ;; => 537
(remaining-minutes-in-oven nil)  ;; => 0

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
                                        ;         Splitting leftovers         ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; define function preparation-time
;; (defun split-leftovers (keywords)
;;   (let* ((weight (getf keywords :weight))
;;          (human (getf keywords :human))
;;          (alien (getf keywords :alien))
;;          ;; using the reduce function with the binary function #'- to subtract the values of human and alien
;;          (total (reduce #'- (list human alien))))
;;     (- total weight)
;;     )
;;   )

;; (defun split-leftovers (keywords)
;;   (let* ((weight (or (getf keywords :weight) 0))
;;          (human (or (getf keywords :human) 0))
;;          (alien (or (getf keywords :alien) 0)))
;;     (- weight human alien)))


(defun split-leftovers (&key (weight 0) (human 10) (alien 10))
  "This function calculates the difference between the weight and the sum of human and alien values.
  It takes a single argument `keywords`, which is a list of keyword-value pairs, representing the weight, human, and alien values.
  If keyword-value pairs are not present in the input, the function will assume a default value of 0 for missing keyword-value pairs.
  The function returns the result of subtracting human and alien from weight."
  (cond
    ((equal weight 0) (print :JUST-SPLIT-IT))
    ((equal weight NIL) (print :LOOKS-LIKE-SOMEONE-WAS-HUNGRY))
    ( (- weight human alien)  )
    )
  )

(split-leftovers :weight 20 :human 10 :alien 5) ;; => 5
(split-leftovers :weight 20 :alien 10 :human 2) ;; => 8
(split-leftovers :alien 12 :weight 20 :human 4) ;; => 4
(split-leftovers :weight 20 :human 5) ;; => 5
(split-leftovers :weight 20 :alien 5) ;; => 5
(split-leftovers :weight 20)          ;; => 0
(split-leftovers :human 5 :alien 5) ;; => :JUST-SPLIT-IT
(split-leftovers :weight NIL :human 5 :alien 5) ;; => :LOOKS-LIKE-SOMEONE-WAS-HUNGRY
