# coding=utf-8
import os

import pytest
import rospy


def get_output_file(argv):
    for arg in argv:
        if arg.startswith('--gtest_output'):
            return arg.split('=xml:')[1]

    raise RuntimeError('No output file has been passed')


def run_pytest(argv):
    output_file = get_output_file(argv)
    root_dir = os.path.dirname(output_file)
    test_module = rospy.get_param('test_module')
    module_path = os.path.realpath(test_module)

    return pytest.main([module_path, '--junitxml={}'.format(output_file), '--rootdir={}'.format(root_dir)])
