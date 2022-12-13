from typing import List
from argparse import ArgumentParser


def get_packages_with_wildcards(pipfile_path: str) -> List[str]:
    # Read Pipfile
    with open(pipfile_path) as f:
        pipfile = f.read()
    packages: List[str] = []
    # Loop over all lines and check for "*"
    for line in pipfile.splitlines():
        if line.startswith("["):
            continue
        if '"*"' in line:
            packages.append(line.split("=")[0].strip().replace('"', "").replace("'", ""))
    return packages


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument(
        "-pf",
        "--pipfile",
        dest="pipfile_path",
        help="Alternative path for Pipfile",
        required=False,
        nargs="?",
        default="Pipfile",
    )
    known_args, unkown_args = parser.parse_known_args()
    pipfile_path = known_args.pipfile_path if known_args.pipfile_path else "Pipfile"

    packages = get_packages_with_wildcards(pipfile_path=pipfile_path)
    if len(packages) > 0:
        print("The following (dev-)packages contain a wildcard:")
        for package in packages:
            print(f"  {package}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
