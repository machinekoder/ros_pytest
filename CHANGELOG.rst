^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros_pytest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.1 (2021-05-03)
------------------
* Merge pull request `#9 <https://github.com/machinekoder/ros_pytest/issues/9>`_ from jspricke/missing_dependencies
  Add dependency on python-pytest-cov
* Contributors: Alexander Rössler, Jochen Sprickerhof

0.2.0 (2020-08-12)
------------------
* Merge pull request `#7 <https://github.com/machinekoder/ros_pytest/issues/7>`_ from machinekoder/fix-folders
* Bugfix for pytest folder tests
* Merge pull request `#5 <https://github.com/machinekoder/ros_pytest/issues/5>`_ from sfalexrog/python3_compat
* Merge pull request `#6 <https://github.com/machinekoder/ros_pytest/issues/6>`_ from PilzDE/feature/add_coverage
* Remove comment
* Added reasoning and integrate if CATKIN_TEST_COVERAGE is set
* Create subfolder for .coverage for each test
* Add  flag to pytest execution
* Add coverage for pytest
* package.xml: Use conditional dependencies
* CMakeLists: Use catkin_install_python for script installation
* Contributors: Alexander Gutenkunst, Alexander Rössler, Alexey Rogachevskiy, hslusarek

0.1.2 (2018-11-15)
------------------
* Added add_pytests cmake macro
* enable passing of additional commands
* Contributors: Alexander Rössler, Markus Grimm

0.1.1 (2018-10-07)
------------------
* Release for melodic

0.1.0
-----
This is the first release the ros_pytest package.

It contains everything necessary to run pytests with rostest.

