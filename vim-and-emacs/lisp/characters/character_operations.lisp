(defpackage :character-study
  (:use :cl)
  (:export
   :compare-chars
   :size-of-char
   :change-size-of-char
   :type-of-char))
(in-package :character-study)

(defun compare-chars (char1 char2)
  (cond
    ((char= char1 char2)
     (print :equal-to)
     )
    ((char-greaterp char1 char2)
     (print :greater-than)
     )
     ((char-lessp char1 char2)
      (print :less-than)
      )
    )
  )
)

(compare-chars #\b #\a)
;; (defun size-of-char (char))

;; (defun change-size-of-char (char wanted-size))

;; (defun type-of-char (char))
