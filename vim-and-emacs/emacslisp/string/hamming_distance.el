;;; hamming.el --- Hamming (exercism)  -*- lexical-binding: t; -*-

;;; Commentary:

(defun hamming-distance (dna1 dna2)
  ;;; Code:  
  (if (not (eq (length dna1) (length dna2)))
      (print "Not same length")
  )

  (let ((dist 0))
    (dotimes (i (min (length dna1) (length dna2)) )
      (when (not (eq (aref dna1 i) (aref dna2 i)))
        (setq dist (+ dist 1))
      )
    )
    (progn
      (print dist)
      dist
    )
  )
)

(provide 'hamming)
(hamming-distance "hello" "bye")
;;; hamming.el ends here
