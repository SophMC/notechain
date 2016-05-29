# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import hello_world2


class HelloWorldTests(unittest.TestCase):

    def test_hello_without_name(self):
        self.assertEqual(
            'Hello, World!',
            hello_world2.hello()
        )

    def test_hello_with_sample_name(self):
        self.assertEqual(
            'Hello, Alice!',
            hello_world2.hello('Alice')
        )

    def test_hello_with_other_sample_name(self):
        self.assertEqual(
            'Hello, Bob!',
            hello_world2.hello('Bob')
        )

    def test_hello_with_umlaut_name(self):
        self.assertEqual(
            'Hello, Jürgen!',
            hello_world2.hello('Jürgen')
        )

if __name__ == '__main__':
    unittest.main()
