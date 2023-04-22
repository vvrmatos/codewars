;; Initial solution
(defpackage #:challenge/solution
  (:use #:cl)
  (:export #:NAME-OF-YOUR-FUNCTION))
(in-package #:challenge/solution)

;; Sample tests
(in-package #:cl-user)
(defpackage #:challenge/tests/solution
  (:use #:cl #:rove #:challenge/solution))
(in-package #:challenge/tests/solution)

(deftest expressions-matter
  (testing "Small values"
    (ok (= (expressions-matter 2 1 2) 6))
    (ok (= (expressions-matter 2 1 1) 4))
    (ok (= (expressions-matter 1 1 1) 3))
    (ok (= (expressions-matter 1 2 3) 9))
    (ok (= (expressions-matter 1 3 1) 5))
    (ok (= (expressions-matter 2 2 2) 8)))
  (testing "Medium values"
    (ok (= (expressions-matter 5 1 3) 20))
    (ok (= (expressions-matter 3 5 7) 105))
    (ok (= (expressions-matter 5 6 1) 35))
    (ok (= (expressions-matter 1 6 1) 8))
    (ok (= (expressions-matter 2 6 1) 14))
    (ok (= (expressions-matter 6 7 1) 48)))
  (testing "Mixed values"
    (ok (= (expressions-matter 2 10 3) 60))
    (ok (= (expressions-matter 1 8 3) 27))
    (ok (= (expressions-matter 9 7 2) 126))
    (ok (= (expressions-matter 1 1 10) 20))
    (ok (= (expressions-matter 9 1 1) 18))
    (ok (= (expressions-matter 10 5 6) 300))
    (ok (= (expressions-matter 1 10 1) 12))))
