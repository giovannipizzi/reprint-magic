reprint-magic
-------------

A module that registers and defines a jupyter ipython magic 
to run and reprint on output the code.

Usage
+++++

First, you need to load the extension. If you do not want
to change your ipython configuration to load it by default,
run the following command at the top of your notebook::

   %% load_ext reprint_magic

Use the ``%%reprint`` cell magic as follows::

    %%reprint
    def double_number(number):
        return 2*number

This will both output the source code of the cell in the output, and run the code.

The code will have a thin border around it. If you don't like it, use instead ``%%reprint --no-box`` or, equivalently, ``%%reprint -n``.

This is particularly useful when used in combination with the `appmode`_.

Demo
++++

To see a demo, look into the jupyter notebook ``demo/demo.ipynb`` or see it live
using binder (click below).

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/giovannipizzi/reprint-magic/master?filepath=apps%2Fdemo%2Fdemo.ipynb


.. _appmode: https://github.com/oschuett/appmode