;; get list items
;; author: luyang liu
;; date: 2023-01-01

(defun first-thing (list)
  (car list)
)

(defun second-thing (list)
  (setq res ( subseq list 1 2) )
  (car res)
)

(defun third-thing (list)
  (setq res ( subseq list 2 3) )
  (car res)
)

(defun twenty-third-thing (list)
  (setq res ( subseq list 22 23) )
  (car res)
)

(first-thing (list 'butter 'milk 'egg))
(second-thing (list 'butter 'milk 'egg))
(third-thing (list 'butter 'milk 'egg))
