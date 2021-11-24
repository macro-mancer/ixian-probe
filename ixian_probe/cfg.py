import graphviz as gv
from ixian_probe.basic_block import BasicBlock
from typing import Dict, Tuple, Optional, Set


class CFG:
    def __init__(self, name: str):
        self.name: str = name

        self.start: Optional[BasicBlock] = None
        self.bblocks: Dict[int, BasicBlock] = {}
        self.edges: Dict[Tuple[int, int], Type[ast.AST]] = {}
        self.cfg: Optional[gv.Digraph] = None

    def show_cfg_source(self):
        self.cfg = gv.Digraph(
            name=self.name, format="pdf", graph_attr={"label": self.name}
        )
        self._traverse_and_build(self.start, set())
        return self.cfg.source

    def _traverse_and_build(self, block: BasicBlock, visited: Set[int]):
        if block.id not in visited:
            visited.add(block.id)
            self.cfg.node(str(block.id), label=str(block.id))

        for next_bb in block.next:
            self._traverse_and_build(self.bblocks[next_bb.id], visited)
            self.cfg.edge(
                str(block.id), str(next_bb.id), label=f"({block.id}, {next_bb.id})"
            )
