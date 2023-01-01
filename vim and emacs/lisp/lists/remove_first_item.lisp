;; Removes first item from list
;; Author: Luyang Liu
;; Date: 2023-01-01


;; Evaluates to the 'rest' of the CONS
;; Using cdr
(defun remove-first-item (list)
  (setq result ( cdr list ))
)

(remove-first-item (list 'butter 'milk 'egg))
