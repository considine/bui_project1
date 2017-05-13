;; this is how to load external modules in scheme
(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_dailies/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; John Considine

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; (copy the output you saw here)
;; question 1: #f
;; explanation:
;; (use as many lines as necessary, just add more comments)
;;
;;
;; car( cdr (cdr q) ) is eqal to the third item in the list since 
;; cdr returns the "rest" of the list and car returns the first 
;; item which is the third. 
;; The third item is a list itself "stuffing potatoes ham" which is
;; not an atom since an atom is a basic element and inhrently nothing
;; that contains multple items
;;


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; question 2: #f
;;
;; explanation:
;; so we have the same middle part as problem 1; the car (cdr (cdr q) ) is 
;; the third item of the list which is the list (stuffing potatoes ham). Lat 
;; returns true if the list only contains atoms  which it does. If it
;; were stuffing potatoes ham (turkey raspberries) instead than lat? would 
;; have returned false
;;
;;


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;;
;;question 3: turkey
;; explanation:
;; a cond is a short circuit if statement essentially. A cond syntax basically
;; consists of a list of pairs of true/ false statements and actions; the 
;; true false statement is like the key, and the first key to return true has
;; the corresponding value executed. 
;;
;; The problem above asks: is the first item of q an atom? if so return
;; that item, else return nothing. The first item of q is turkey which is
;; an atom hence the car q is executed
;;
;;


