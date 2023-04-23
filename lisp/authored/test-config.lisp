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

(deftest NAME-OF-YOUR-FUNCTION
  (testing "Small values"
    (ok (= (NAME-OF-YOUR-FUNCTION 2 1 2) 6))))