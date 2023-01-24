(defpackage :character-study
  (:use :cl)
  (:export
   :compare-chars
   :size-of-char
   :change-size-of-char
   :type-of-char))
(in-package :character-study)

(defun compare-chars (char1 char2)
  "This function takes two characters as inputs and compares them. It returns whether the first character is equal to, greater than or less than the second character."
  (cond
    ((char= char1 char2)
     (print :equal-to)
     )
    ((char-greaterp char1 char2)
     (print :greater-than)
     )
    ((char-lessp char1 char2)
     (print :less-than)
    )
  )
)

(compare-chars #\b #\a)

(defun size-of-char (char)
  "This function takes a character as input and returns whether it is upper-case, lower-case or has no size."
  (cond
    ((upper-case-p char)
     :big
    )
    ((lower-case-p char)
     :small
    )
    (:no-size)
  )
)

(print (size-of-char #\a))

(defun change-size-of-char (char wanted-size)
  "This function takes a character and the desired size as inputs and returns the character in the desired case."
  (cond
    ((equal wanted-size :big)
     (char-upcase char)
    )
    ((equal wanted-size :small)
     (char-downcase char)
    )
  )
)

(print (change-size-of-char #\a :big))
(print (change-size-of-char #\A :small))


(defun type-of-char (char)
  "This function takes a character as an input and returns whether the character is alphabetic, numeric, a newline, a space or unknown."
  (cond
    ((alpha-char-p char)
      (progn
      (print :alpaha)
      :alpha
      )
    )
    ((digit-char-p char)
      (progn
        (print :numeric)
        :numeric
      )
    )
    ((char= char #\Newline)
      (progn
        (print :newline)
        :newline
      )
    )
    ((char= char #\Space)
      (progn
        (print :space)
        :space
      )
    )
    ((progn
      (print :unknown )
      :unknown
    ))
  )
)


(type-of-char #\a)
(type-of-char #\1)
(type-of-char #\space)
(type-of-char #\newline)
(type-of-char #\!)
