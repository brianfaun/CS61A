(define (partial-sums stream)
  (define (ps-helper stream sum)
    (if (null? stream)
      nil
      (cons-stream (+ (car stream) sum) (ps-helper (cdr-stream stream) (+ (car stream) sum)))
    )
  )
  (ps-helper stream 0)
)
