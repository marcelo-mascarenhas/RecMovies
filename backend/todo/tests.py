from ast import Assert
from django.test import TestCase
import pytest

# Create your tests here.

def test_initial():
  a = 2 + 2
  assert(a) == 4
  
  