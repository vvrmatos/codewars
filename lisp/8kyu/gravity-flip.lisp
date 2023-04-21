;;;; https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/commonlisp

(defun flip (dir boxes)
    (cond ((equal dir #\L) (sort boxes '>))
          ((equal dir #\R) (sort boxes '<))))

