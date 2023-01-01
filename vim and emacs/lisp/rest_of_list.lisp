;; This program gets the first element of a list
;; Author: Luyang Liu
;; Date: 2023-01-01

;; Evaluates to the 'rest' of the CONS
;; using subseq
(defun rest-of-it (cons)
  ;; put the code to get the rest of CONS here
  (setq result ( subseq cons 1 (length cons) ))
  (print (length result))
  ;; If the length is one just get the first
  (if (equal ( length result ) 1)
      (nth 1 cons))
  ( subseq cons 1 (length cons) )
  )

;; Evaluates to the 'rest' of the CONS
;; Using cdr
(defun rest-of-it (cons)
  (setq result ( cdr cons ))
  )
