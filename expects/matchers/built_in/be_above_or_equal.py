# -*- coding: utf-8 -*

from .. import Matcher


class be_above_or_equal(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject >= self._expected

    def _description(self, subject):
        return 'be above or equal {expected!r}'.format(expected=self._expected)
