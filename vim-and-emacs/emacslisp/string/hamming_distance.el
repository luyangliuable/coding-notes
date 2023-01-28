;;; hamming.el --- Hamming (exercism)  -*- lexical-binding: t; -*-

;;; Commentary:

(defun hamming-distance (dna1 dna2)
  ;;; Code:  
  (let ((dist 0))
    (dotimes (i (min (length dna1) (length dn2)) )
      (when (not (eq (aref dna1 i) (aref dna2 i) )))
    )
  )
)

(provide 'hamming)
(hamming-distance "hello" "bye")
;;; hamming.el ends here
