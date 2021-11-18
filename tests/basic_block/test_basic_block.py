import pytest
from ixian_probe.basic_block import BasicBlock


@pytest.fixture()
def a_bb():
    """Return a BasicBlock"""
    return BasicBlock(42)


def test_create_basic_block():
    """BasicBlock(bbid) should return a basic block whose id is equal to bbid"""
    basic_block = BasicBlock(99)
    assert basic_block.id == 99


def test_empty_basic_block(a_bb):
    """BasicBlock is empty (i.e., a basic block with no statements) at first"""
    assert a_bb.is_empty()


def test_basic_block_with_no_prevs(a_bb):
    """After creation, BasicBlock has no previous BBs (that lead to it)/incoming edges"""
    assert a_bb.has_prev() == False


def test_basic_block_with_prevs(a_bb):
    """A BasicBlock is able to tell whether it has any BBs (that lead to it)/incoming edges"""
    a_bb.add_prev(41)
    a_bb.add_prev(40)
    assert a_bb.has_prev()
    assert a_bb.prev_no() == 2


def test_basic_block_with_nexts(a_bb):
    """A BasicBlock is abnle to tell whether it has any BB that 
    come after it in the CFG (i.e., outcoming edges) 
    as well as how many there are
    """
    a_bb.add_prev(41)  # this shouldn't change anything
    a_bb.add_next(43)
    a_bb.add_next(44)
    assert a_bb.has_next()
    a_bb.add_next(45)
    assert a_bb.next_no() == 3
