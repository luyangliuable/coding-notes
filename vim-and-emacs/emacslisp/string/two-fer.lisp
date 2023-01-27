;;; two-fer.el --- Two-fer Exercise (exercism)
;;; Commentary:


;;; Code:
(defun two-fer (&optional name)
  (if (null name)
    (progn
      (print "One for ~A, one for me")
      "One for ~A, one for me"
    )
    (format "One for %s, one for me." name)
  )
)

(provide 'two-fer)
;;; two-fer.el ends here
