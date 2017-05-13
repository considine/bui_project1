;; scheme tictactoe homework
;; name: ??????????
;; date: ??????????

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_tictactoe/paradigms_ttt.scm")
(use-modules (ice-9 paradigms_ttt))

;; REPLACE WITH YOUR FUNCTIONS FROM A PREVIOUS HOMEWORK:
;;  greatest
;;  positionof
;;  value

(define greatest
  (lambda (tup)
   (cond
    ((null? tup) 0)
    (( > (car tup) (greatest (cdr tup))) (car tup))
    (else (greatest (cdr tup)))
)))

(define positionof
  (lambda (n tup)
   (cond
   ((eq? (car tup) n) 1)
   (else (+ 1 (positionof n (cdr tup))))
)))


(define value
  (lambda (p)
   (lambda (gs)
    (cond 
     ((win? p gs) 10)
     ((win? (other p) gs) -10)
     (else 0)

))))


(define sum*-g
  (lambda (ttup f)
    (cond
        ((null? ttup) 0)
        ((null? (cdr ttup)) (f (car ttup)))
        (else (+ (sum*-g (car (cdr ttup)) f)(sum*-g (cons (car ttup) (cdr (cdr ttup))) f)))
        
    )
)
)
;;utility function 
(define sumrest
  (lambda (p ttup)
   (cond 
    ((null? ttup) '())
    (else (cons (sum*-g (car ttup) (value p)) (sumrest p (cdr ttup))))
   )))


;; MODIFY your sum* function for this assignment...

;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
  (lambda (p gt)
   (cond 
    ((null? (cdr gt)) '())
    (else (pick (positionof (greatest (sumrest p (cdr gt))) (sumrest p (cdr gt))) (firsts (cdr gt))))
)))
;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

