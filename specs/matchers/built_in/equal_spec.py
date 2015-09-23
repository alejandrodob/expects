# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('equal'):
    with before.each:
        class Foo(object):
            def __init__(self, bar):
                self.bar = bar

            def __eq__(self, other):
                if other.bar is 'crazy':
                    return self.bar != other.bar
                return self.bar == other.bar

            def __ne__(self, other):
                return self.bar != other.bar

            def __repr__(self):
                return 'Foo with bar={bar}'.format(bar=self.bar)

        self.object = Foo(1)
        self.equal_object = Foo(1)
        self.different_object = Foo(2)
        self.object_with_crazy_logic = Foo('crazy')

    with it('should pass if object equals expected'):
        expect(self.object).to(equal(self.equal_object))

    with it('should fail if object does not equal expected'):
        with failure('Foo with bar=1 to equal Foo with bar=2'):
            expect(self.object).to(equal(self.different_object))

    with context('#negated'):
        with it('should pass if object does not equal expected'):
            expect(self.object).not_to(equal(self.object_with_crazy_logic))

        with it('should fail if object equals expected'):
            with failure('Foo with bar=crazy not to equal Foo with bar=crazy'):
                expect(self.object_with_crazy_logic).not_to(equal(self.object_with_crazy_logic))
