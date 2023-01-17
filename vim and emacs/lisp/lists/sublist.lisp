(defpackage :sublist
  (:use :cl)
  (:export :sublist))

(in-package :sublist)

(defun contiguous-sublistp (A B)
  "This function checks if A is a contiguous sublist of B.
  It returns T if A is a contiguous sublist of B, NIL otherwise."

  (setq length-A (length A))

  ;; check if A and B are both empty or if B is shorter than A
  (cond
    ( (or
       (and (null A) (null B))
       (< (length B) (length A))
       )
      ;; If A and B are both empty or B is shorter than A, return NIL
      (return-from contiguous-sublistp nil)
    )

    ;; check if A is empty but B is not
    (( null A )
     (return-from contiguous-sublistp t)
    )

    ;; check if B is empty but A is not
    (( null B )
     (return-from contiguous-sublistp nil)
    )
  )

  ;; loop through B and check if the sublist starting at the current index and of length A is equal to A
  (loop for i from 0 to (- (length B) length-A)
    do (cond
          ((equal A (subseq B i (+ i length-A)))
          (return t)
        )
    )
  )
)

(defun sublist (A B)
  "This function compares two lists A and B and determines if A is an equal list, a sublist, or a superlist of B."
  (cond
    ;; Check if A and B are both empty
    ((and (null A) (null B))
     (print :equal))

    ;; Check if A and B are identical lists
    ((equal A B)
     (print :equal))

    ;; Check if A is a sublist of B
    ((contiguous-sublistp A B)
     (print :sublist))

    ;; Check if A is a superlist of B
    ((contiguous-sublistp B A)
     (print :superlist))

    ;; If none of the above conditions are true, the lists are not related
    (t (print :unequal))
  )
)

(sublist (list 1 2 3 4 5) (list 2 3 4)) ;; superlist
(sublist (list 2 3 4) (list 1 2 3 4 5) ) ;; sublist
(sublist (list) (list)) ;; equal
(sublist (list 1 2 3) (list)) ;; superlist
(sublist (list) (list 1 2 3) ) ;; superlist
(sublist (list 3 4 5) (list 1 2 3 4 5) ) ;; superlist
