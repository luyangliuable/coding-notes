;; This program calculates cheese per cube
;; Author: Luyang Liu
;; Date: 2023-01-01

(defun pizzas-per-cube (cube-size diameter)
  (round (/ (* 2 (expt cube-size 3) ) (* 3 pi (expt diameter 2)) ) )
)

(pizzas-per-cube 12 12)

