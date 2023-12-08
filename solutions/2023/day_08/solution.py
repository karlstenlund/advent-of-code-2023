# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

from sympy import lcm_list
from ...base import StrSplitSolution, answer

class Solution(StrSplitSolution):
    _year = 2023
    _day = 8

    @answer(21251)
    def part_1(self) -> int:
        instructions = self.input[0]
        lr_nodes = self.input[2:]
        nodes = {}
        for lr_node in lr_nodes:
            node = Node(lr_node)
            nodes[node.name] = node
        
        ack = 0
        instruction_count = len(instructions)
        current_node = nodes['AAA']
        while True:
            if current_node.name == 'ZZZ':
                break
            if instructions[ack % instruction_count] == 'L':
                current_node = nodes[current_node.left]
            else:
                current_node = nodes[current_node.right]
            ack += 1
        return ack
        
        

    # @answer(1234)
    def part_2(self) -> int:
        instructions = self.input[0]
        lr_nodes = self.input[2:]
        nodes = {}
        for lr_node in lr_nodes:
            node = Node(lr_node)
            nodes[node.name] = node
        nodes = {name: node.update_nodes(nodes) for name, node in nodes.items()}
        instruction_count = len(instructions)
        starting_nodes = [node for node in nodes.values() if node.name.endswith('A')]
        step_counts = []
        for node in starting_nodes:
            steps = 0
            while True:
                if node.name.endswith('Z'):
                    step_counts.append(steps)
                    break
                instruction = instructions[steps % instruction_count]
                node = node.follow_instruction(instruction)
                steps += 1
        return lcm_list(step_counts)

class Node():
    def __init__(self, lr_node) -> None:
        lr_node = lr_node.split(' ')
        self.name = lr_node[0]
        self.left = lr_node[2][1:-1]
        self.right = lr_node[3][:-1]

    def __repr__(self) -> str:
        return f'{self.name}'
    
    def follow_instruction(self, instruction: str) -> str:
        if instruction == 'L':
            return self.left
        else:
            return self.right
        
    def update_nodes(self, nodes):
        self.left = nodes[self.left]
        self.right = nodes[self.right]
        return self



