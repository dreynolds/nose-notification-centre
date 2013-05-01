import os

from pync import Notifier
from nose.plugins import Plugin


class NCPlugin(Plugin):
    name = 'NCPlugin'
    enabled = True

    def finalize(self, result):
        failures = len(result.failures)
        errors = len(result.errors)
        skips = len(result.skipped)
        folder = result.config.workingDir.strip('/').split('/')[-1]

        if result.wasSuccessful():
            title = "Tests passed in: %s" % folder
            msg = 'Hurrah! All of your %s test(s) passed!' % result.testsRun
        else:
            msg = 'Boo! %s failures, %s errors and %s skips' % (failures, errors, skips)
            title = "Tests failed in: %s" % folder

        Notifier.notify(msg, title=title, group='%s_%s_tests' % (folder, self.name))