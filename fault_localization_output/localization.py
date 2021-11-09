"""Fault localization calculations."""


import collections
import math


ExecutionCounts = collections.namedtuple(
    "ExecutionCounts",
    "positive_cases negative_cases"
)

LINE_EXECUTIONS = collections.defaultdict(
    lambda: ExecutionCounts(
        positive_cases=0,
        negative_cases=0,
    )
)

LINE_NOT_EXECUTIONS = collections.defaultdict(
    lambda: ExecutionCounts(
        positive_cases=0,
        negative_cases=0,
    )
)


def update_executions(lines, failed, line_executions=LINE_EXECUTIONS):
    """Update line executions to reflect test results."""
    for line in lines:
        # print("Current line: ")
        # print(line)
        
        prev_executions = line_executions[line]
        # print("prev_executions: ")
        # print(prev_executions)
        line_executions[line] = ExecutionCounts(
            positive_cases=prev_executions.positive_cases + int(not failed),
            negative_cases=prev_executions.negative_cases + int(failed)
        )


PRIOR = ExecutionCounts(
    positive_cases=1,
    negative_cases=0
)


def calc_scores(failed, line_executions=LINE_EXECUTIONS, prior=PRIOR):
    """Return 'fault' score for each line, given prior and observations."""
    """This is the original method, I think it is Jaccard"""
    return {
        line: float(
            execution_counts.negative_cases + prior.negative_cases
        ) / (
            execution_counts.positive_cases + prior.positive_cases
            + execution_counts.negative_cases + prior.negative_cases
        )
        for line, execution_counts in line_executions.items()
    }

# def calc_scores(failed, line_executions=LINE_EXECUTIONS, prior=PRIOR):
#     """Return 'fault' score for each line, given prior and observations."""
#     """McCon method"""
#     return {
#         line: float(
#             (execution_counts.negative_cases**2) - (failed - execution_counts.negative_cases)*execution_counts.positive_cases
#         ) / (
#             (execution_counts.negative_cases + (failed - execution_counts.negative_cases))*(execution_counts.negative_cases * execution_counts.positive_cases+prior.positive_cases)
#         )
#         for line, execution_counts in line_executions.items()
#     }

# def calc_scores(failed, line_executions=LINE_EXECUTIONS, prior=PRIOR):
#     """Return 'fault' score for each line, given prior and observations."""
#     """Kulczynski2 method test"""
#     return {
#         line: float(
#             0.5
#         ) * (
#             (execution_counts.negative_cases)
#             /(execution_counts.negative_cases + (failed - execution_counts.negative_cases)) 
#             +
#             (execution_counts.negative_cases)
#             /(execution_counts.negative_cases + execution_counts.positive_cases)
#         )
#         for line, execution_counts in line_executions.items()
#     }

# def calc_scores(failed, line_executions=LINE_EXECUTIONS, prior=PRIOR):
#     """Return 'fault' score for each line, given prior and observations."""
#     """Ochiai, [hightlight the buggy lines]"""
#     return {
#         line: float(
#             execution_counts.negative_cases
#         ) / (
#             math.sqrt((execution_counts.negative_cases + failed-execution_counts.negative_cases) * 
#             (execution_counts.negative_cases + execution_counts.positive_cases))
#         )
#         for line, execution_counts in line_executions.items()
#     }

# def calc_scores(failed, line_executions=LINE_EXECUTIONS, prior=PRIOR):
#     """Return 'fault' score for each line, given prior and observations."""
#     """Zoltar version [very very highlight the buggy lines]"""
#     # print(math.sqrt((execution_counts.negative_cases +prior.negative_cases) * (execution_counts.positive_cases + prior.negative_cases)))
#     return {
#         line: float(
#             execution_counts.negative_cases
#         ) / (
#             execution_counts.negative_cases + (failed - execution_counts.negative_cases) + execution_counts.positive_cases + 10000 * (
#                 (failed - execution_counts.negative_cases) * execution_counts.positive_cases
#             ) / (
#                 execution_counts.negative_cases
#             )
#         )
#         for line, execution_counts in line_executions.items()
#     }
