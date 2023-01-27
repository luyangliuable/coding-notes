;;; rna-transcription.el -- RNA Transcription (exercism)  -*- lexical-binding: t; -*-

;;; Commentary:

(defun to-rna (strand)
  ;;; Code:
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

(print (to-rna 'A) )

(provide 'rna-transcription)
;;; rna-transcription.el ends here
