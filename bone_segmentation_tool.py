import os
import argparse
import logging
from core.pipelines.pipelines_controller import (
    get_pipeline_description,
    load_pipeline_dynamically,
)

plid = "bone_segmentation"


def get_description():
    return get_pipeline_description(plid)


def add_parser_arguments(parser):
    parser.add_argument(
        "input",
        metavar="i",
        type=str,
        help="Specify the path to the directory containing the scans in the form of DICOM",
    )
    parser.add_argument(
        "output",
        metavar="o",
        type=str,
        help="Specify the path of a single output file in the form of a glb file",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Set the logging level from INFO to ERROR",
    )
    parser.set_defaults(which=plid)


def run(args):
    input_dir = args.input
    output_path = args.output
    if os.path.exists(output_path):
        raise Exception("Output file location already exists.")
    logging.info("Loading and initializing bone pipeline dynamically")
    pipeline_module = load_pipeline_dynamically(plid)
    pipeline_module.run(input_dir, output_path)
    logging.info("Done.")


def main():
    parser = argparse.ArgumentParser(description=get_description())
    add_parser_arguments(parser)
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.ERROR if args.quiet else logging.INFO,
        format="%(asctime)s - %(module)s:%(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )

    run(args)


if __name__ == "__main__":
    main()
