# -*- coding: utf-8 -*-

from inspect import signature
import unittest
import numpy as np
from main import identity, double, addition

class TestCase(unittest.TestCase):

    def test_identity(self):
        sig = signature(identity)
        self.assertEqual(len(sig.parameters), 1)
        for _ in range(10):
            rv = np.random.randn(1)[0]
            self.assertEqual(rv, identity(rv))

    def test_double(self):
        sig = signature(double)
        self.assertEqual(len(sig.parameters), 1)
        for _ in range(10):
            rv = np.random.randn(1)[0]
            self.assertEqual(2 * rv, double(rv))

    def test_addition(self):
        sig = signature(addition)
        self.assertEqual(len(sig.parameters), 2)
        for _ in range(10):
            rvs = np.random.randn(2)
            self.assertEqual(rvs[0] + rvs[1], addition(rvs[0], rvs[1]))

if __name__ == "__main__":
    unittest.main()
