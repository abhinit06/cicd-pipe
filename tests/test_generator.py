import unittest

from buzz import generator

def test_sample_sum():
    sum = generator.sample(2,3)
    sum1=(5,7,9)
    assert sum in sum1
