;;; rna-transcription.el -- RNA Transcription (exercism)  -*- lexical-binding: t; -*-
;;; Author: Luyang Liu
;;; Commentary:
;;; This file contains the implementation of the to-rna function, which takes a DNA strand as input
;;; and returns its corresponding RNA strand.
;;; Code:
(defun to-rna (dna-strand)
  (let ((rna-strand ""))
    (dotimes (i (length dna-strand))
      (let ((nucleotide (aref dna-strand i)))
        (cond
         ;; char-equal is used here to compare the character
         ;; because it is case-insensitive, whereas char= is case-sensitive
         ;; ?G, ?C, ?T, ?A are used as shortcut to represent #\G, #\C, #\T, #\A respectively
         ((char-equal nucleotide ?G) (setq rna-strand (concat rna-strand "C")))
         ((char-equal nucleotide ?C) (setq rna-strand (concat rna-strand "G")))
         ((char-equal nucleotide ?T) (setq rna-strand (concat rna-strand "A")))
         ((char-equal nucleotide ?A) (setq rna-strand (concat rna-strand "U")))
         ;; error function is used to raise an error with a custom message
         ((error "Invalid char: %s" nucleotide))
         )
        )
      )
    rna-strand
    )
  )

(defun to-rna-one-char (char)
  (cond ((string= strand 'A)
         'U
         )
        ((string= strand 'G)
         'C
         )
        ((string= strand 'C)
         'G
         )
        ((string= strand 'T)
         'A
    )
  )
)

(print (to-rna "AGCT") )

(provide 'rna-transcription)
;;; rna-transcription.el ends here
