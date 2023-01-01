;; This program calculates the grams of dough needed for given number and size of pizzas
;; Author: Luyang Liu
;; Date: 2023-01-01

(defun dough-calculator (pizzas diameter)
  (round (* pizzas (+ 200 (/ (* 45 pi diameter) 20)) ) )
)

(dough-calculator '12 '12)
