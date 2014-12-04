# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('have_len'):
    with it('passes if string has the expected length'):
        expect('foo').to(have_len(3))

    with it('passes if iterable has the expected length'):
        expect(iter('foo')).to(have_len(3))

    with it('fails if string does not have the expected length'):
        with failure("Expected 'foo' to have len 2"):
            expect('foo').to(have_len(2))

    with it('fails if iterable does not have the expected length'):
        with failure('to have len 2'):
            expect(iter('foo')).to(have_len(2))

    with context('#negated'):
        with it('passes if string does not have the expected length'):
            expect('foo').not_to(have_len(2))

        with it('fails if string has the expected length'):
            with failure("Expected 'foo' not to have len 3"):
                expect('foo').not_to(have_len(3))