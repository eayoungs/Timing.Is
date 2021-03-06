#!/usr/bin/env python

""" This module provides uint-tests for the main application functions of the
    webapp; "timing.is" """

__author__ = "Eric Allen Youngson"
__email__ = "eayoungs@gmail.com"
__copyright__ = "Copyright 2017 Eric Youngson"
__license__ = "Apache 2.0"

import os
import sys

import timingis
import unittest
import tempfile


sys.path.append('../')


class TimingisTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, timingis.app.config['DATABASE'] = tempfile.mkstemp()
        timingis.app.testing = True
        self.app = timingis.app.test_client()
        with timingis.app.app_context():
            timingis.init_db()

    def tearDown():
        os.close(self.db_fd)
        os.unlink(timingis.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()
