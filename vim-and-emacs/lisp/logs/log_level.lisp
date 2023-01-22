(defpackage :log-levels
(:use :cl)
(:export :log-message :log-severity :log-format))

(in-package :log-levels)

(defun log-message (log-string)
"Extract the message from the log string, and print it.
log-string - the log string in the format '[level]: message'"
(setq a (subseq log-string 8 (length log-string)))
(print a)
)

(log-message "[ohno]: whoops!") ; => "whoops!"

(defun log-severity (log-string)
"Extract the severity level from the log string and print a corresponding symbol.
log-string - the log string in the format '[level]: message'"
(setq severity (subseq log-string 1 5))
(cond
((string= (string-downcase severity ) "warn")
(print :getting-worried)
)
((string= (string-downcase severity ) "info")
(print :everything-ok)
)
((string= (string-downcase severity ) "ohno")
(print :run-for-cover)
)
)
)

(log-severity "[info]: might want to get that checked") ; => :getting-worried
(log-severity "[warn]: might want to get that checked") ; => :getting-worried
(log-severity "[ohno]: might want to get that checked") ; => :getting-worried
(log-severity "[WaRn]: string case system failing") ; => :getting-worried

(defun log-format (log-string)
"Extract the message and the severity level from the log string and print a corresponding symbol.
log-string - the log string in the format '[level]: message'"
(setq severity (subseq log-string 1 5))
(setq message (subseq log-string 8 (length log-string)))
(cond
((string= (string-downcase severity ) "warn")
(print (string-capitalize message ))
)
((string= (string-downcase severity ) "info")
(print (string-downcase message ))
)
((string= (string-downcase severity ) "ohno")
(print (string-upcase message ))
)
)
)

(log-format "[ohno]: whoops!") ; => WHOOPS!
(log-format "[warn]: whoops!") ; => WHOOPS!
(log-format "[info]: whoops!") ; => WHOOPS!
