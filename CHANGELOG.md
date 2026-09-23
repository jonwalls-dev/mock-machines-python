# Changelog

## 0.2.1

First release on PyPI.

- Wheels for macOS x86_64 (Intel) and Windows x86_64, alongside Linux x86_64 /
  aarch64 and macOS arm64.
- The `mm` command now works: earlier wheels bundled a non-executable file in
  its place.
- macOS wheels declare their real minimum, macOS 12.
- Licensed as proprietary, free-to-use software (see `LICENSE`); previously
  mislabelled Apache-2.0.
- `examples/quickstart.py` and a self-contained `CliffWalkingRL` scenario under
  `examples/scenarios/`.

## 0.2.0

TestPyPI preview: in-process engine via cffi, zero-copy Arrow observations, and
the CliffWalking DQN notebook.
