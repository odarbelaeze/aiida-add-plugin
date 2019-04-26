import six
from aiida.orm import NumericType
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
            "metadata.options.input_filename",
            valid_type=six.string_types,
            default="aiida.in",
            non_db=True,
        )
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
        spec.input("x", valid_type=NumericType, help="The left operand")
        spec.input("y", valid_type=NumericType, help="The rigth operand")
        spec.output(
            "sum", valid_type=NumericType, help="The sum of the left and right operands"
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
        self.write_input_files(folder, self.input.x, self.input.y)
