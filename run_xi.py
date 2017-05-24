import argparse
from XiWrapper import XiWrapper
import logging


class Runner(object):
    """
    class that initializes the parser and executes the search
    """
    def __init__(self):
        self._args = self.init_parser()

    def init_parser(self):
        parser = argparse.ArgumentParser(
            description="""Script to execute Xi Searches.""")
        parser.add_argument('-p', '--peak_files', type=str, nargs='+', required=True,
                            # action='append',
                            help="peak files either from MaxQuant or in mgf format")
        parser.add_argument('-f', '--fasta_dbs', type=str, nargs='+', required=True,
                            # action='append',
                            help="on or more fasta protein databases to search on")
        parser.add_argument('xi_config', type=str,
                            help="config file for the Xi search")
        parser.add_argument('-o', '--output', type=str, default="./xi_results.csv",
                            help="output folder [default='./xi_results.csv']")
        parser.add_argument('-m', '--memory', type=str, default=None,
                            help="""how much memory to allocate to xiSearch. (i.e. 1G / 128M / 1024K)
                                 [default=let java decide]""")
        parser.add_argument('--add_xi_cmd', type=list, nargs='*', default=[],
                            help="""additional parameters to hand to xi""")
        parser.add_argument('-v', '--verbosity', default=1, type=int,
                            help='set level of logging (int: 0-50)')
        return parser.parse_args()

    @staticmethod
    def set_up_logging(verbosity):
        if verbosity < 0:
            verbosity = 0
        logging.basicConfig(level=verbosity,
                            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    def run(self):
        if self._args.verbosity != 0:
            Runner.set_up_logging(self._args.verbosity)
        XiWrapper.xi_execution(
            xi_config=self._args.xi_config,
            peak_files=self._args.peak_files,
            fasta_files=self._args.fasta_dbs,
            memory=self._args.memory,
            output_file=self._args.output,
            additional_parameters=self._args.add_xi_cmd
        )


if __name__ == "__main__":
    runner = Runner()

    runner.run()
