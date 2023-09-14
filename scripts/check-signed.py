import os
import sys
from typing import Optional, Iterable


def _get_signatures() -> Iterable[str]:
    with open("static/SIGNATURE.txt", "r") as signature_file:
        return [line.strip() for line in signature_file.readlines()]


def _check_signed() -> bool:
    github_actor: Optional[str] = os.environ.get("GITHUB_ACTOR")
    if not github_actor:
        print("Missing GitHub Actor!")
        return False
    if github_actor == "dependabot":
        print("dependabot is exempt from signature.")
        return True
    for signature in _get_signatures():
        if signature == github_actor:
            print("You are all set!")
            return True
    print("Please sign with your GitHub name in `SIGNATURE`.")
    return False


if __name__ == "__main__":
    sys.exit(0 if _check_signed() else 1)
