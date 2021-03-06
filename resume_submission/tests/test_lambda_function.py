import pytest
from resume_submission.lambda_function import solve_puzzle, \
    create_final_output_list, create_sorted_list, create_relationship, solved_puzzle_string, \
    extract_puzzle_details

'''
Few ways that would help solve problem:
Fill in the blanks
Use BST

'''


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                '''Please solve this puzzle:
ABCD
A->--
B-=--
C>---
D-<--''',
                ''' ABCD
A=>>>
B<=<>
C<>=>
D<<<='''
        ),
        (
                "Please solve this puzzle: ABCD A=--- B<--- C>--- D-->-",
                ''' ABCD
A=><<
B<=<<
C>>=<
D>>>='''
        ),
    ],
)
def test_return_output(input, expected_result):
    assert solve_puzzle(input=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                ["ABCD", "A-<--", "B-=--", "C->--", "D-->-"],
                {2: 1, 3: 2, 4: 3}
        ),

        (
                ["ABCD", "A--->", "B-=--", "C-<--", "D->--"],
                {1: 4, 2: 3, 4: 2}
        ),
        (
                ["ABCD", "A--->", "B---<", "C>---", "D---="],
                {1: 4, 4: 2, 3: 1}
        ),
    ],
)
def test_create_relationship_dict(input, expected_result):
    assert create_relationship(input=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                ["ABCD", "A-<--", "B-=--", "C->--", "D-->-"],
                {2: 1, 3: 2, 4: 3}
        ),

        (
                ["ABCD", "A--->", "B-=--", "C-<--", "D->--"],
                {1: 4, 2: 3, 4: 2}
        ),
        (
                ["ABCD", "A--->", "B---<", "C>---", "D---="],
                {1: 4, 4: 2, 3: 1}
        ),
    ],
)
def test_create_relationship(input, expected_result):
    assert create_relationship(input=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                {2: 1},
                [2, 1]
        ),
        (
                {1: 2},
                [1, 2]
        ),
        (
                {1: 2, 2: 3},
                [1, 2, 3]
        ),
        (
                {2: 1, 3: 2},
                [3, 2, 1]
        ),
        (
                {2: 1, 3: 2, 4: 3},
                [4, 3, 2, 1]
        ),

        (
                {1: 4, 2: 3, 4: 2},
                [1, 4, 2, 3]
        ),
        (
                {2: 3, 1: 4, 4: 2},
                [1, 4, 2, 3]
        ),
        (
                {1: 4, 4: 2, 3: 1},
                [3, 1, 4, 2]
        ),
    ],
)
def test_create_max_min_list(input, expected_result):
    assert create_sorted_list(relationship=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                [2, 1],
                [[' ', 'A', 'B'], ['A', "=", "<"], ['B', ">", "="]]
        ),
        (
                [1, 2],
                [[' ', 'A', 'B'], ['A', "=", ">"], ['B', "<", "="]]
        ),
        (
                [1, 2, 3],
                [[' ', 'A', 'B', 'C'], ['A', "=", ">", ">"], ['B', "<", "=", ">"], ['C', "<", "<", "="]]
        ),
        (
                [1, 2, 3, 4],
                [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", ">", ">"], ['B', "<", "=", ">", ">"],
                 ['C', "<", "<", "=", ">"], ['D', "<", "<", "<", "="]]
        ),
        (
                [4, 3, 2, 1],
                [[' ', 'A', 'B', 'C', 'D'], ['A', "=", "<", "<", "<"], ['B', ">", "=", "<", "<"],
                 ['C', ">", ">", "=", "<"], ['D', ">", ">", ">", "="]]
        ),
        (
                [4, 3, 2, 1],
                [[' ', 'A', 'B', 'C', 'D'], ['A', "=", "<", "<", "<"], ['B', ">", "=", "<", "<"],
                 ['C', ">", ">", "=", "<"], ['D', ">", ">", ">", "="]]
        ),
        (
                [3, 2, 1],
                [[' ', 'A', 'B', 'C'], ['A', "=", "<", "<"], ['B', ">", "=", "<"],
                 ['C', ">", ">", "="]]
        ),
        (
                [1, 4, 2, 3],
                [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", ">", ">"], ['B', "<", "=", ">", "<"],
                 ['C', "<", "<", "=", "<"], ['D', "<", ">", ">", "="]]
        ),
        (
                [3, 1, 4, 2],
                [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", "<", ">"], ['B', "<", "=", "<", "<"],
                 ['C', ">", ">", "=", ">"], ['D', "<", ">", "<", "="]]
        ),
    ],
)
def test_create_final_output(input, expected_result):
    assert create_final_output_list(input=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                [[' ', 'A', 'B'], ['A', "=", "<"], ['B', ">", "="]],
                ''' AB
A=<
B>='''
        ),
        (
                [[' ', 'A', 'B'], ['A', "=", ">"], ['B', "<", "="]],
                ''' AB
A=>
B<='''
        ),
        (
                [[' ', 'A', 'B', 'C'], ['A', "=", ">", ">"], ['B', "<", "=", ">"], ['C', "<", "<", "="]],
                ''' ABC
A=>>
B<=>
C<<='''
        ),
        # (
        #         [1, 2, 3, 4],
        #         [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", ">", ">"], ['B', "<", "=", ">", ">"], ['C', "<", "<", "=", ">"], ['D', "<", "<", "<", "="]]
        # ),
        # (
        #         [4, 3, 2, 1],
        #         [[' ', 'A', 'B', 'C', 'D'], ['A', "=", "<", "<", "<"], ['B', ">", "=", "<", "<"],
        #          ['C', ">", ">", "=", "<"], ['D', ">", ">", ">", "="]]
        # ),
        # (
        #         [4, 3, 2, 1],
        #         [[' ', 'A', 'B', 'C', 'D'], ['A', "=", "<", "<", "<"], ['B', ">", "=", "<", "<"],
        #          ['C', ">", ">", "=", "<"], ['D', ">", ">", ">", "="]]
        # ),
        # (
        #         [3, 2, 1],
        #         [[' ', 'A', 'B', 'C'], ['A', "=", "<", "<"], ['B', ">", "=", "<"],
        #          ['C', ">", ">", "="]]
        # ),
        # (
        #         [1, 4, 2, 3],
        #         [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", ">", ">"], ['B', "<", "=", ">", "<"], ['C', "<", "<", "=", "<"], ['D', "<", ">", ">", "="]]
        # ),
        # (
        #         [3, 1, 4, 2],
        #         [[' ', 'A', 'B', 'C', 'D'], ['A', "=", ">", "<", ">"], ['B', "<", "=", "<", "<"], ['C', ">", ">", "=", ">"], ['D', "<", ">", "<", "="]]
        # ),
    ],
)
def test_convert_lol_final_result(input, expected_result):
    assert solved_puzzle_string(input=input) == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
                '''Please solve this puzzle:
ABCD
A->--
B-=--
C>---
D-<--''',
                ["ABCD", "A->--", "B-=--", "C>---", "D-<--"]
        )
    ],
)
def test_return_output(input, expected_result):
    assert extract_puzzle_details(input=input) == expected_result
