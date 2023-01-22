;; This program calculates saunce from pizza perimeter
;; Author: Luyang Liu
;; Date: 2023-01-01

(defun size-from-sauce (sauce)
  (round (sqrt (/ (* 40 sauce) (* 3 pi)) ) )
)

(SIZE-FROM-SAUCE 12)
