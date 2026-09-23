"""Load a scenario, walk an entity, and read its state back as Arrow.

Run from anywhere once `mock-machines` is installed:

    python examples/quickstart.py
"""

from pathlib import Path

import mockmachines as mm

SCENARIO = Path(__file__).parent / "scenarios" / "CliffWalkingRL"


def main() -> None:
    sim = mm.load(str(SCENARIO))
    print("machines:", sim.machines)

    sim.reset()  # seed a fresh episode: one Walker on a 4x12 grid of GridCells
    start = sim.observe("Walker").column("current_cell_id")[0].as_py()
    print("walker starts on cell", start)

    for move in ["move_north", "move_east", "move_east", "move_east"]:
        sim.step(target="Walker", event=move)  # one targeted event = one turn
        cell = sim.observe("Walker").column("current_cell_id")[0].as_py()
        print(f"{move:<11} -> cell {cell}")

    # observe() returns a pyarrow.Table, so the whole grid is one call away.
    grid = sim.observe("GridCell")
    kinds = grid.group_by("kind").aggregate([("ID", "count")]).to_pylist()
    print("grid cells by kind:", {row["kind"]: row["ID_count"] for row in kinds})
    sim.close()


if __name__ == "__main__":
    main()
