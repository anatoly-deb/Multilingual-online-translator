from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TranslatorTest(StageTest):
    def generate(self):
        return [TestCase(stdin='fr\nhello\n'),]

    def check(self, reply, attach):
        if 'bonjour' in reply and 'examples' in reply.lower():
            return CheckResult.true()
        return CheckResult.false("Test failed. You probably don't print translations or examples. You should print some of them both.")

TranslatorTest('translator.translator').run_tests()