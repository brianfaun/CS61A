(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
    (map (lambda (x) (cons first x)) rests))

(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
  )

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper s n)
    (if (null? s) s
      (cons (list n (car s)) (helper (cdr s) (+ n 1)))
      ))
    (helper s 0)
  )

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond ((null? denoms) nil)
        ((= total 0) (cons nil nil))
        ((< total (car denoms)) (list-change total (cdr denoms)))
        (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                      (list-change total (cdr denoms))
              ))
    )
)

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr) expr)
        ((quoted? expr) expr)
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           (append (list form params) (map let-to-lambda body))
           )
          )
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (define symbols (car (zip (let-to-lambda values))))
           (define vals (cadr (zip (let-to-lambda values))))
           (cons (cons 'lambda (cons symbols (let-to-lambda body))) vals)
           ; END PROBLEM 18
           )
          )
        (else
          (map let-to-lambda expr)
        )
  )
)
