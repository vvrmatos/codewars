#!/usr/bin/env python


def are_you_playing_banjo(name):
    y_banjo_message = " plays banjo"
    n_banjo_message = " does not play banjo"
    message = [y_banjo_message, n_banjo_message]

    if name[0].lower() == "r":
        return name + message[0]

    return name + message[1]

