# mockmachines

Drive the [Mock Machines](https://app.mockmachines.dev) simulation engine from
Python — the fastest, simplest bridge between Python and the engine. The engine
runs **in-process** as a CGo shared library loaded via cffi (no network, no
subprocess), and entity state crosses into Python **zero-copy** through the Apache
Arrow C Data Interface.

This package is intentionally minimal. It is *not* a reinforcement-learning
framework: it loads a scenario, seeds episodes, steps the simulation (optionally
with a targeted action), and hands back entity state as `pyarrow` tables. You
build the observation vector, reward, action policy, and training loop yourself —
see the worked [CliffWalking DQN notebook](https://github.com/jonwalls-dev/mock-machines-python/tree/main/examples/notebooks).

## Install

```bash
pip install mock-machines        # or: uv pip install mock-machines
```

Prebuilt wheels ship the engine shared library and the `mm` CLI binary, so **no
Go toolchain or C compiler is needed**. Wheels are published for Linux (x86_64,
aarch64), macOS 12+ (arm64, x86_64), and Windows (x86_64), and one wheel serves
every Python ≥ 3.10.

The distribution is named **`mock-machines`**; the import name is **`mockmachines`**:

```python
import mockmachines as mm
```

## Quick start

The [examples](https://github.com/jonwalls-dev/mock-machines-python/tree/main/examples)
ship a `CliffWalkingRL` scenario — a walker on a 4×12 grid with a cliff and a goal:

```python
import mockmachines as mm

sim = mm.load("examples/scenarios/CliffWalkingRL")  # a scenario directory, .yaml file, or YAML text
sim.reset()                                   # seed a fresh episode (1 walker)
sim.step(target="Walker", event="move_north")  # one targeted event = one turn
table = sim.observe("Walker")                 # pyarrow.Table of the walker's state
print(table)
```

Run the complete version with `python examples/quickstart.py`.

## The `mm` CLI

The wheel also installs `mm`, the engine's command-line runner, for batch runs
that export their data to disk:

```bash
mm -run 50 -out results/ examples/scenarios/CliffWalkingRL/CliffWalkingRL.yaml
mm -run 200 -format parquet -out results/ my_scenario.yaml
mm --help
```

Flags come **before** the scenario path.

## License

`mock-machines` is proprietary software, free to install and use (including
commercially) under the terms in
[`LICENSE`](https://github.com/jonwalls-dev/mock-machines-python/blob/main/LICENSE).
The bundled engine binaries may not be reverse engineered, modified, or
redistributed outside the published wheels.

Questions and bug reports:
[github.com/jonwalls-dev/mock-machines-python/issues](https://github.com/jonwalls-dev/mock-machines-python/issues).
