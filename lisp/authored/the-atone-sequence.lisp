;;;; 2 ^ n - 1

(defpackage #:challenge/solution
  (:use #:cl)
  (:export #:atone))
(in-package #:challenge/solution)

(defun atone (pos)
  (parse-integer (make-string pos :initial-element #\1) :radix 2))
