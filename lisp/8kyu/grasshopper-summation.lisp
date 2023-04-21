;;;; https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/commonlisp

(defun summation (n)
  (let ((result 0))
    (dotimes (i n)
      (incf result (+ i 1)))
    result))
