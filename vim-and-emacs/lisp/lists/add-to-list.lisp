;; this program adds to list of items
;; author: luyang liu
;; date: 2023-01-01

(defun add-to-list (item list)
  (append (list item ) list)
)

(add-to-list 'butter (list 'milk 'egg))
