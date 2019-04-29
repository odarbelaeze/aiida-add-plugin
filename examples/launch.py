"""
A sample launch plugin.

Usage:
    verdi run examples/launch.py
"""

from __future__ import print_function

from aiida.orm import load_code, Float
from aiida.plugins.factories import CalculationFactory
from aiida.engine import run

import logging


def main():
    # Log to the console
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter("[%(levelname)s] %(name)s : %(message)s"))
    logging.getLogger("add").addHandler(console)
    logging.getLogger("add").setLevel(logging.DEBUG)

    code = load_code(label="add@localhost")
    calculation = CalculationFactory("add.calculation")

    builder = calculation.get_builder()
    builder.code = code
    builder.x = Float(3.0)
    builder.y = Float(3.5)

    builder.metadata.options = {"resources": {"num_machines": 1}}

    results, node = run.get_node(builder)
    print(results, node, sep="\n")


if __name__ == "__main__":
    main()
