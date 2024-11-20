import json
import pytest
import os

def test_generate_diff(file1, file2):
    diff = generate_diff(file1, file2)
    expected_result = {
        'follow': ('removed', False), 
        'host': ('unchanged', 'hexlet.io'), 
        'proxy': ('removed', '123.234.53.22'), 
        'timeout': ('changed', (50, 20)), 
        'verbose': ('added', True)
        }
    assert diff == expected_result