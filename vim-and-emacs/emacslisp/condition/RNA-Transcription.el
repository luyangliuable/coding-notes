;;; rna-transcription.el -- RNA Transcription (exercism)  -*- lexical-binding: t; -*-

;;; Commentary:

(defun to-rna (dna-strand)
  (let ((rna-strand ""))
    (dotimes (i (length dna-strand))
      (let ((nucleotide (aref dna-strand i)))
        (cond
          ((char-equal nucleotide ?G) (setq rna-strand (concat rna-strand "C")))
          ((char-equal nucleotide ?C) (setq rna-strand (concat rna-strand "G")))
          ((char-equal nucleotide ?T) (setq rna-strand (concat rna-strand "A")))
          ((char-equal nucleotide ?A) (setq rna-strand (concat rna-strand "U")))
          ()
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

(print (to-rna "Hello") )

(provide 'rna-transcription)
;;; rna-transcription.el ends here
