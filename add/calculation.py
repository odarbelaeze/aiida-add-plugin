import json
import six

from aiida.orm import Float
from aiida.common import CalcInfo, CodeInfo
from aiida.engine import CalcJob


class AddCalculation(CalcJob):
    """
    Add calculation plugin for the futures
    """

    @classmethod
    def define(cls, spec):
        super(AddCalculation, cls).define(spec)
        spec.input(
            "metadata.options.output_filename",
            valid_type=six.string_types,
            default="aiida.out",
            non_db=True,
        )
        spec.input(
            "metadata.options.parser_name",
            valid_type=six.string_types,
            default="add.parser",
            non_db=True,
        )
        spec.input("x", valid_type=Float, help="The left operand")
        spec.input("y", valid_type=Float, help="The rigth operand")
        spec.output(
            "sum", valid_type=Float, help="The sum of the left and right operands"
        )
        spec.exit_code(
            100,
            "ERROR_NO_RETRIEVED_FOLDER",
            message="The retrieved folder data node could not be accessed",
        )
        spec.exit_code(
            110,
            "ERROR_READING_OUTPUT_FILE",
            message="The output file could not be read from the retrieved folder",
        )
        spec.exit_code(
            120,
            "ERROR_INVALID_OUTPUT",
            message="The output file contains invalid output",
        )

    def prepare_for_submission(self, folder):
        """
        Get ready.
        """

        # We wont write anything to the `folder` since the program takes
        # input as commandline parameters

        code_info = CodeInfo()
        code_info.cmdline_params = [str(self.inputs.x.value), str(self.inputs.y.value)]
        code_info.stdout_name = self.options.output_filename
        code_info.code_uuid = self.inputs.code.uuid

        calc_info = CalcInfo()
        calc_info.uuid = str(self.node.uuid)  # ?
        calc_info.codes_info = [code_info]
        calc_info.retrieve_list = [self.options.output_filename]
        calc_info.local_copy_list = []  # Anything that we have localy and could use
        calc_info.remote_copy_list = []  # Anything that we have remotely and could use

        return calc_info
