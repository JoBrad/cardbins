from __future__ import division, print_function
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: JoBrad
# Website: https://github.com/JoBrad/cardbins
"""
Python script for identifying card types based on their BIN
"""
import re
_ALLOWEDNAMES = set(['__name__', '__file__', '__doc__'])
_IGNOREDNAMES = set()
_IGNOREDNAMES = set(locals().keys()) - _ALLOWEDNAMES

CARD_BINS = {
    'Diners Club International': re.compile(pattern = '^(30[0-59]|3[689])[\d]*'),
    'Dankort': re.compile(pattern = '^(4175|4571)[\d]*'),
    'Diners Club United States & Canada': re.compile(pattern = '^(5[45])[\d]*'),
    'Maestro': re.compile(pattern = '^(50|5[6-9]|6[0-9])[\d]*'),
    'Discover Card': re.compile(pattern = '^(6011|622(12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[0-1][0-9]|92[0-5])|64[4-9]|65)[\d]*'),
    'American Express': re.compile(pattern = '^3[47][\d]*'),
    'Diners ClubCarte Blanche': re.compile(pattern = '^30[0-5][\d]*'),
    'Japan Credit Bureau': re.compile(pattern = '^35(2[89]|[3-7][0-9]|8[0-9])[\d]*'),
    'Visa': re.compile(pattern = '^4[\d]*'),
    'China UnionPay': re.compile(pattern = '^62[\d]*'),
    'InstaPayment': re.compile(pattern = '^63[7-9][\d]*'),
    'InterPaymentTM': re.compile(pattern = '^636[\d]*'),
    'MasterCard': re.compile(pattern = '^5[1-5][\d]*')
}

def getCardType(cardBIN = None):
    try:
        cardBINValue = str(cardBIN).strip()
        cardType = ''
        for cardMatch in CARD_BINS:
            if cardType == '':
                if CARD_BINS[cardMatch].match(cardBIN) is not None:
                    cardType = cardMatch
        if cardType == '':
            return None
        else:
            return cardType

    except:
        raise ValueError('The provided card bin could not be parsed.')

__all__ = sorted(set(locals().keys()) - _IGNOREDNAMES)
del _ALLOWEDNAMES
del _IGNOREDNAMES
