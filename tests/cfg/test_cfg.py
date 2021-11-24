import pytest
from ixian_probe.cfg import CFG
from ixian_probe.basic_block import BasicBlock


@pytest.fixture()
def bb1():
    return BasicBlock(1)


@pytest.fixture()
def bb2():
    return BasicBlock(2)


def test_cfg_after_creation():
    """CFG(name) should return a CFG whose name/label is equal to name"""
    a_cfg = CFG("method-name")
    # at first there is no starting node
    assert a_cfg.start == None
    # there are no nodes/bbs
    assert a_cfg.bblocks == {}
    # accordingly, no edges
    assert a_cfg.edges == {}
    # and no dot representation
    assert a_cfg.cfg == None


def test_cfg_after_setting_start_bb(bb1):
    """After creating an instance of CFG (cfg) and setting the starting 
    node/BB (bb1), cfg.start should return that BB (bb1)"""
    a_cfg = CFG("method-name")
    a_cfg.start = bb1
    a_cfg.bblocks[bb1.id] = bb1
    assert a_cfg.start.id == 1
    assert len(a_cfg.bblocks) == 1
    assert a_cfg.bblocks[1] == bb1


def test_cfg_with_more_than_one_bb(bb1, bb2):
    cfg1 = CFG("I have two nodes")
    cfg1.start = bb1
    cfg1.bblocks[bb1.id] = bb1
    # add edge from bb1 to bb2
    bb1.add_next(bb2)
    # add bb2 to cfg
    cfg1.bblocks[bb2.id] = bb2
    assert len(cfg1.bblocks) == 2


def test_cfg_source(bb1, bb2):
    cfg1 = CFG("CFG-with-2-nodes")
    cfg1.start = bb1
    cfg1.bblocks[bb1.id] = bb1
    # add edge from bb1 to bb2
    bb1.add_next(bb2)
    # add bb2 to cfg
    cfg1.bblocks[bb2.id] = bb2
    dot_repr = 'digraph "CFG-with-2-nodes" {\n\tgraph [label="CFG-with-2-nodes"]\n\t1 [label=1]\n\t2 [label=2]\n\t1 -> 2 [label="(1, 2)"]\n}\n'
    assert cfg1.show_cfg_source() == dot_repr


def test_cfg_source_2(bb1, bb2):
    cfg1 = CFG("CFG-with-3-nodes")
    cfg1.start = bb1
    cfg1.bblocks[bb1.id] = bb1
    # add edge from bb1 to bb2
    bb1.add_next(bb2)
    # add bb2 to cfg
    cfg1.bblocks[bb2.id] = bb2
    # add edge from bb2 to bb3
    bb3 = BasicBlock(3)
    bb2.add_next(bb3)
    # add bb3 to cfg
    cfg1.bblocks[bb3.id] = bb3
    dot_repr = 'digraph "CFG-with-3-nodes" {\n\tgraph [label="CFG-with-3-nodes"]\n\t1 [label=1]\n\t2 [label=2]\n\t3 [label=3]\n\t2 -> 3 [label="(2, 3)"]\n\t1 -> 2 [label="(1, 2)"]\n}\n'
    assert cfg1.show_cfg_source() == dot_repr
