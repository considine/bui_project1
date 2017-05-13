;; scheme daily homework 6
;; name: ??????????
;; date: ??????????
(use-modules (ice-9 debugging traps) (ice-9 debugging trace))

(define sum*
  (lambda (ttup)
    (cond
        ((null? ttup) 0)
        ((atom? (car ttup)) (+ (car ttup) (sum* (cdr ttup)) ))
        (else (+ (sum* (car ttup))(sum* (cdr ttup) )))
    )
)
)
(define (atom? x) (not (or (pair? x) (null? x))))
;; tests!
(display (sum* '((5)) ))
(display "\n")

(display (sum* '((0) ((0) ((5))) ((0) ((10)))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7)))) ((0) ((10) ))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7) ) ((8) ))) ((0) ((10) ))) ))
(display "\n")

;; correct output:
;;   $ guile d6.scm
;;   5
;;   15
;;   22
;;   30

