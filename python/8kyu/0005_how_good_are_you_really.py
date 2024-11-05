#!/usr/bin/env python


def better_than_average(class_score, my_score):
    class_score_average = sum(class_score) // len(class_score)
    return my_score > class_score_average

