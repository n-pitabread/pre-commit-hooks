import argparse
from typing import Any
from typing import Generator
from typing import NamedTuple
from typing import Optional
from typing import Sequence

def _check_main(line) -> bool:
    if "if __name__ == '__main__'" in line:
        return True
    else:
        return False


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--check', action='store_true',
        help=(
            'if this flag is added, the main won\'t be remove.   '
        ),
    )
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    if args.check:
        return 0
    for filename in args.filenames:
        edited_file = []
        with open(filename, encoding='UTF-8') as f:
            found_main = False
            for line in f.readlines():
                if _check_main(line):
                    found_main = True
                    retval = 1

                if not found_main:
                    edited_file.append(line)

        with open(filename, "w") as ff:
            for v in edited_file:
                ff.write(v)
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
