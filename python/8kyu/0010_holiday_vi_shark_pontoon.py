#!/usr/bin/env python


def shark(pontoon_distance, shark_distance, your_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed >>= 1
    if pontoon_distance / your_speed if > shark_distance / shark_speed:
        return "Shark Bait!"
    else:
        return "Alive!"

