# import unittest
# from train import multiply
#
# class TestFirst(unittest.TestCase):
#     @unittest.expectedFailure
#     def test_multiply(self):
#         self.assertEqual(multiply(2,4),9)

# import pytest
# from train import multiply
#
# class TestFirst:
#     @staticmethod
#     @pytest.mark.parametrize(
#         'a, b, c',((2,4,8),(4,6,24),(5,6,30),(5,7,35))
#     )
#     def test_multiply(a,b,c):
#         assert multiply(a,b) == c
import pytest
from train import multiply


class TestFirst:

    @pytest.mark.asyncio
    async def test_multiply(self):
        assert await multiply(2, 4) == 8
 # flake8 --ignore e305 --exclude .get,venv,__pycache__,.idea,alembic --max-line-length 120 .
