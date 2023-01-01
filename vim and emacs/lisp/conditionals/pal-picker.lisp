;; Pick a pal program
;; Author: Luyang Liu
;; Date: 2023-01-01

(defun pal-picker (personality)
  (cond ((equal personality :lazy) "Cat")
        ((equal personality :energetic) "Dog")
        ((equal personality :quiet) "Fish")
        ((equal personality :hungry) "Rabbit")
        ((equal personality :talkative) "Bird")
        ("I don't know... A dragon?")
  )
)

(pal-picker :lazy)
(pal-picker :talkative)
(pal-picker :poo)

(defun habitat-fitter (weight)
  (cond (( >= weight 40 ) :massive)
  (( and (>= weight 20) (<= weight 39) ) :large)
  (( and (>= weight 10) (<= weight 19) ) :medium)
  (( and (>= weight 1) (<= weight 9) ) :small)
  ((<= weight 0) :just-your-imagination))
)

(habitat-fitter 40)
(habitat-fitter 20)
(habitat-fitter 10)
(habitat-fitter 0)

(defun feeding-time-p (fullness)
  (cond ( (> fullness 20) "All is well." )
        ((<= fullness 20) "It's feeding time!")
  )
)

(feeding-time-p 21)
(feeding-time-p 20)

(defun pet (pet)
  (if (equal pet "Fish")
      (print 't)
      ())
)

(pet "Fish")
(pet "Dog")

(defun play-fetch (pet)
  ;; (print (equal pet "Dog"))
  (if (equal pet "Dog")
      ()
      (print 't)
      )
)

(play-fetch "Dog")
(play-fetch "Fish")
(play-fetch "Cat")

