
(define-macro (switch expr cases)
    (cond ((= (eval expr) (car (car cases))) (cdr (car cases)))
          (else (switch expr (cdr cases)))
    )
)
