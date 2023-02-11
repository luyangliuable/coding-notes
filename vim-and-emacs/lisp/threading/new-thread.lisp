(ql:quickload :bordeaux-threads)

(defun my-thread-function ()
  (format t "Hello from a new thread!~%")
  (bt:sleep 5)
  (format t "Goodbye from the new thread.~%"))

(bt:make-thread #'my-thread-function)
