;;;; https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/commonlisp

(defun expressions-matter (a b c)
  (max (+ a b c)
       (* a b c)
       (* a (+ b c))
       (* c (+ a b))))
