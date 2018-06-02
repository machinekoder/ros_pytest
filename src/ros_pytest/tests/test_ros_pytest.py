# -*- coding: utf-8 -*-
import pytest

import ros_pytest


def test_output_file_is_correctly_extracted_from_argv():
    output = ros_pytest.get_output_file(['runner.py', '--gtest_output=xml:~/junit_output.xml'])

    assert output == '~/junit_output.xml'


def test_not_passing_output_file_throws_runtime_error():
    with pytest.raises(RuntimeError):
        ros_pytest.get_output_file(['main.py', '--file', 'random.txt'])
