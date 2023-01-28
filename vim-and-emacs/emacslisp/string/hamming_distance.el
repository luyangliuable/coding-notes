;;; hamming.el --- Hamming (exercism)  -*- lexical-binding: t; -*-
;;; Author: Luyang Liu
;;; Commentary:
;;; This file contains a function that calculates the Hamming distance
;;; between two DNA strings. The Hamming distance is the number of
;;; positions at which the corresponding symbols are different.
;;; Code:

(defun hamming-distance (dna1 dna2)
  "Calculate the Hamming distance between DNA strings DNA1 and DNA2.
  If the strings are of different length, return an error."
  (if (not (= (length dna1) (length dna2)))
      (error "Strings are not of equal length")
    (let ((dist 0))
      (dotimes (i (length dna1))
        ;; increment dist if characters at position i are different
        (when (not (eq (aref dna1 i) (aref dna2 i)))
          (setq dist (+ dist 1))
          )
        )
      (print dist)
      dist
      )
    )
  )

(provide 'hamming)
(print (hamming-distance "llo" "bye"))
;;; hamming.el ends here
