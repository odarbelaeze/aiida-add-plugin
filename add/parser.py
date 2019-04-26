import logging
import json

from aiida.common import exceptions
from aiida.orm import Float
from aiida.parsers import Parser


logger = logging.getLogger(__name__)


class AddParser(Parser):
    """
    A parser for the add code output.
    """

    def parse(self, **kwargs):
        """
        There should be some output files in a folder at `self.retrieved`.
        """

        try:
            output_folder = self.retrieved
        except exceptions.NotExistent:
            return self.exit_codes.ERROR_NO_RETRIEVED_FOLDER

        logger.info(
            "This is the contents of the output folder: {}".format(
                output_folder._repository.list_object_names()
            )
        )

        try:
            # Output filename was an option and became an attribute
            with output_folder.open(
                self.node.get_attribute("output_filename"), "r"
            ) as handle:
                result = self.parse_output(handle)
        except (OSError, IOError):
            logger.exception("There was an error reading the expected output")
            return self.exit_codes.ERROR_READING_OUTPUT_FILE
        except json.JSONDecodeError:
            logger.exception("There was an error reading the JSON output")
            return self.exit_codes.ERROR_INVALID_OUTPUT

        if "sum" not in result:
            return self.exit_codes.ERROR_INVALID_OUTPUT

        self.out("sum", Float(result["sum"]))

    @staticmethod
    def parse_output(handle):
        """
        Parse a json output from the file handle.
        """
        return json.load(handle)
