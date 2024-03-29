"""Pytest plugin."""

import os
import sys
import csv

import pytest

from fault_localization_output.tracing import TRACER
from fault_localization_output.localization import update_executions, calc_scores
from fault_localization_output.display import generate_output, generatefile_output


LOCALIZATION_DIR = None
N_LINES = 1


def pytest_addoption(parser):
    group = parser.getgroup('fault-localization', 'fault localization')
    group.addoption('--localize', help="directory in which to localize faults")
    group.addoption('--n-hotspots', type=int, default=1, help="number of top-ranking lines to display")


def pytest_configure(config):
    global LOCALIZATION_DIR
    global N_LINES
    LOCALIZATION_DIR = config.getoption('--localize')
    N_LINES = config.getoption('--n-hotspots')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    if not LOCALIZATION_DIR:
        yield
        return

    sys.settrace(TRACER.trace)
    try:
        yield
    finally:
        sys.settrace(None)


def pytest_runtest_makereport(item, call):
    failed = bool(getattr(call, 'excinfo', False))
    # print(failed)
    update_executions(
        lines=TRACER.flush_buffer(),
        failed=failed
    )


def pytest_terminal_summary(terminalreporter):
    if not LOCALIZATION_DIR:
        return
    abs_localization_dir = os.path.abspath(LOCALIZATION_DIR)

    # get number of pass and failed
    # print('passed amount: ', len(terminalreporter.stats['passed']))
    print('failed amount: ', len(terminalreporter.stats['failed']))
    numOfFailed = len(terminalreporter.stats['failed'])

    terminalreporter.section("Fault Localization Results")
    line_scores = {
        (path, line): score
        for (path, line), score in calc_scores(numOfFailed).items()
        if path.startswith(abs_localization_dir)
    }
    print(line_scores)
    # for line in generate_output(line_scores, n_lines=N_LINES):
    #     print(line)
    list = []
    header = ['code-line', 'percentage of suspicious']
    for output_line in generatefile_output(line_scores, n_lines=N_LINES):
        # print(output_line.split())
        # print(output_line)
        list.append(output_line.split())
    list.pop(0)
    # print("************")
    # print(list)
    # path = '/Users/wuyuxuan/research-local/pytest_simple_example/'
    with open('result.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(list)

    # cwd = os.getcwd()  
      
    # Print the current working   
    # directory (CWD)  
    # print("Current working directory:")
    # print(cwd)  

    # print(list)
    for line in generate_output(line_scores, n_lines=N_LINES):
        terminalreporter.write_line(line)
