#!/usr/bin/env python3
"""Create encrypted private-case-study payloads for the static portfolio.

Usage (PowerShell):
  $env:RM_EYE_ACCESS_CODE = 'a-long-random-code'; python scripts/encrypt_case_study.py <input> [output]

The access code is deliberately never written to the repository. The output can be
committed safely; it is AES-256-GCM encrypted and can only be opened by a visitor
who knows the code.
"""

from __future__ import annotations

import hashlib
import os
import secrets
import sys
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC = b"RMEYE1"
ITERATIONS = 600_000
DEFAULT_OUTPUT = Path("assets/rm-eye-case-study.enc")


def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit("Usage: python scripts/encrypt_case_study.py <input> [output]")
    code = os.environ.get("RM_EYE_ACCESS_CODE")
    if not code:
        raise SystemExit("Set RM_EYE_ACCESS_CODE before running this script.")

    source = Path(sys.argv[1])
    if not source.is_file():
        raise SystemExit("Input must be an existing file.")
    output = Path(sys.argv[2]) if len(sys.argv) == 3 else DEFAULT_OUTPUT

    salt = secrets.token_bytes(16)
    nonce = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", code.encode("utf-8"), salt, ITERATIONS, dklen=32)
    encrypted = AESGCM(key).encrypt(nonce, source.read_bytes(), None)

    output.parent.mkdir(exist_ok=True)
    output.write_bytes(MAGIC + salt + nonce + encrypted)
    print(f"Wrote {output} ({output.stat().st_size:,} encrypted bytes)")


if __name__ == "__main__":
    main()
