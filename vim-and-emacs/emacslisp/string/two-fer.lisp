;;; two-fer.el --- Two-fer Exercise (exercism)
;;; Commentary:


;;; Code:
(defun two-fer (&optional name)
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
