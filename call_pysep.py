import argparse
from pysep import Pysep

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="?",
                    help="name of file containing event info",
                    default="event_input")
args = parser.parse_args()

sep = Pysep(config_file=args.file+".yaml")
sep.run()
sep.inv
sep.event
