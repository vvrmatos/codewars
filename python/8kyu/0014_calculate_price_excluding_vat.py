#!/usr/bin/env python


def excluding_vat_price(price):
    return round(price * 0.87, 2) if price else -1


