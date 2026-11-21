$ pytest -q

==================================== ERRORS ====================================
____________________ ERROR collecting tests/test_report.py _____________________
ImportError while importing test module '/work/expense-tracker/tests/test_report.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_report.py:1: in <module>
    from expense_tracker.models import Expense
E   ModuleNotFoundError: No module named 'expense_tracker'
____________________ ERROR collecting tests/test_storage.py ____________________
ImportError while importing test module '/work/expense-tracker/tests/test_storage.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
tests/test_storage.py:1: in <module>
    from expense_tracker import storage
E   ModuleNotFoundError: No module named 'expense_tracker'
=========================== short test summary info ============================
ERROR tests/test_report.py
ERROR tests/test_storage.py
!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!
2 errors in 0.05s
[exit code: 2]
