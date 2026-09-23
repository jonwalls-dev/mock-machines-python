# Changelog

## 0.2.2

- `Simulation.observe(...).to_pandas()` no longer fails with "Categorical
  categories must be unique" on machines with catalog fields: catalog columns now
  list every catalog entry, not only the ones the entities happen to use.
- New `KnapsackShopping` example scenario and a notebook
  (`examples/notebooks/knapsack_qiskit.ipynb`) that turns its warehouse order
  books into knapsack problems and solves them with Qiskit's QAOA, comparing it
  against an exact solver and OR-Tools.

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
