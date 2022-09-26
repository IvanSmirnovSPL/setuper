import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="A program for generating files for cavitation case")
    parser.add_argument('-n', '--reconstruct_case_path', metavar='', type=str, default='new_case', help="A path to case directory.")

    args = parser.parse_args()

    if args.reconstruct_case_path is not None:
        try:
            os.system('reconstructPar -case {}'.format(args.reconstruct_case_path))
        except Exception:
            print('The case in {} does not exist'.format(args.reconstruct_case_path))


if __name__ == '__main__':
    main()
