;; This if elseif else statement check
;; Author: Luyang Liu
;; Date: 2023-01-25T09:35:13+11:00

(defun if-elseif-else ()
  "This function takes a number x and checks if it is less than, equal to, or greater than 0. It then prints the corresponding message."
  (let ((x 5))
    (if (< x 0)
      (print "x is less than 0")
      (if (= x 0)
        (print "x is equal to 0")
        (print "x is greater than 0")
      )
    )
  )
)

;; call the function
(if-elseif-else)
