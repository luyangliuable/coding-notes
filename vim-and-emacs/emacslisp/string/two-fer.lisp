;;; two-fer.el --- Two-fer Exercise (exercism)
;;; Commentary:
;;; This file contains the implementation of the function two-fer
;;; which takes an optional name parameter and returns the string
;;; "One for name, one for me." if the name is provided, otherwise
;;; it returns the string "One for you, one for me."
;;;
;;; Author: Luyang Liu <blackfish@Luyangs-MacBook-Pro.local>
;;;
;;; Code:
(defun two-fer (&optional name)
  "Return string 'One for name, one for me' if name is provided otherwise return 'One for you, one for me'."
  (if (null name)
      (progn
        (setq result "One for you, one for me.")
        (print result)
        result
        )
      (progn
        (setq result (format "One for %s, one for me." name))
        (print result)
        result
        )
      )
  )

(provide 'two-fer)
;;; two-fer.el ends here
