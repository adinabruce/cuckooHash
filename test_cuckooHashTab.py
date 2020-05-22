import pytest
from CuckooHashTab import CuckooHashTab
import random

#test that correctly inserts
def test_insert():
      a=CuckooHashTab(10)
      for i in range(26):
            assert a.insert(chr(ord('A')+i),i)==True

#tests that does not insert if key is already there           
def test_insertTwice():
      b=CuckooHashTab(10)
      for i in range(26):
            b.insert(chr(ord('A')+i),i)
      for i in range(26):
            assert b.insert(chr(ord('A')+i),i+1)==False
            
#test that deletes correctly
def test__delete():
      c=CuckooHashTab(10)
      for i in range(26):
            c.insert(chr(ord('A')+i),i) 
      for i in range(26):
            assert c.delete(chr(ord('A')+i))==True
            
#tests that does not delete something if it has not been inserted
def test__deleteNot():
      d=CuckooHashTab(10)
      for i in range(26):
            assert d.delete(chr(ord('A')+i))==False

#tests that returns the correct data for the key      
def test__find():
      e=CuckooHashTab(10)
      for i in range(26):
            e.insert(chr(ord('A')+i),i) 
      for i in range(26):
            assert e.find(chr(ord('A')+i))==i
            
            
pytest.main(["-v", "-s", "test_cuckooHashTab.py"])