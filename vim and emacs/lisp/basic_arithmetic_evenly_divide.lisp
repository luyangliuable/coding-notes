;; This program calculates whether pizza can be evenly divided between friends
;; Author: Luyang Liu
;; Date: 2023-01-01

(defun fair-share-p ( pizza friend )
  (if (equal (mod (* pizza 8) friend) 0)
  'T
  'Nil
  )
)

(fair-share-p 3 4)
(fair-share-p 2 3)
