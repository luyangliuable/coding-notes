;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                                      Let                                    ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun mean (numbers)
  "This function takes a list of numbers as input and returns the mean (average) of the numbers."
  (let ((sum 0)    ; initialize sum and count variables
       (count 0))
    (dolist (n numbers)
            (setq sum   (+ sum n))
            (setq count (1+ count)))
            (/ sum count)
  )
)
