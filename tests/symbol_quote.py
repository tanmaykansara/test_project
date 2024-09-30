import pytest
from plugins.custom_operators.someOperator import someOperator

def test_get_quote():
    sample_op = someOperator(task_id='testing',quote_objects=('apple','aapl'))
    assert(sample_op.get_quotes(symbol='aapl') > 0)