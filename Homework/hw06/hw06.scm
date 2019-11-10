; ;;;;;;;;;;;;;;
; ; Questions ;;
; ;;;;;;;;;;;;;;
; Scheme
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign x)
  (if (< x 0)
      -1
      (if (= x 0)
          0
          1)))

(define (square x) (* x x))

(define (pow b n)
  (if (= n 1)
      b
      (if (even? n)
          (square (pow b (/ n 2)))
          (* b (square (pow b (/ (- n 1) 2)))))))

(define (unique s)
  (if (null? s)
      nil
      (cons (car s)
            (filter (lambda (elem) (not (eq? elem (car s))))
                    (unique (cdr s))))))
