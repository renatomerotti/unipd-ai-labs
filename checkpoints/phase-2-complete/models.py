from dataclasses import dataclass
import random

TARGET = 2.0
NEUTRAL_RATE = 2.0
NATURAL_UNEMP = 4.5
SEED = 42
WEIGHTS = {"core": 0.70, "food": 0.20, "fuel": 0.04, "energy": 0.06}
PERSIST = {"food": 0.6, "fuel": 0.4, "energy": 0.6}
SHOCK_RANGE = {"demand": 0.3, "food": 1.0, "fuel": 4.0, "energy": 2.0}
SHOCK_ORDER = ("demand", "food", "fuel", "energy")
STRESS_FREE = 0.5
STRESS_K = 0.5
POPULATION_START = 10_029_600
MIGRATION_PER_POINT = 20_000
MISERY_NEUTRAL = 1.0
rng = random.Random(SEED)


@dataclass
class Quarter:
    label: str
    rate: float
    core: float
    food: float
    fuel: float
    energy: float
    gap: float
    unemployment: float
    stress: float
    migration: int
    population: int


def headline(quarter: Quarter) -> float:
    return round(sum(weight * getattr(quarter, name) for name, weight in WEIGHTS.items()), 2)


history: list[Quarter] = [
    Quarter('2023-Q3', 2.0, 2.0, 2.0, 2.0, 2.0, 0.0, 4.5, 0.0, 20000, 10049600),
    Quarter('2023-Q4', 2.0, 2.0, 2.2, 1.5, 2.1, 0.1, 4.46, 0.0, 19400, 10069000),
    Quarter('2024-Q1', 2.0, 2.1, 2.4, 3.0, 2.5, 0.2, 4.42, 0.0, 15600, 10084600),
    Quarter('2024-Q2', 2.0, 2.2, 2.6, 4.0, 3.0, 0.3, 4.38, 0.0, 12000, 10096600),
    Quarter('2024-Q3', 2.0, 2.3, 3.0, 6.0, 4.0, 0.4, 4.34, 0.0, 6200, 10102800),
    Quarter('2024-Q4', 2.0, 2.4, 4.0, 10.0, 7.0, 0.5, 4.3, 0.0, -6000, 10096800),
    Quarter('2025-Q1', 2.0, 2.5, 5.0, 14.0, 10.0, 0.5, 4.3, 0.0, -18200, 10078600),
    Quarter('2025-Q2', 2.0, 2.7, 6.0, 12.0, 12.0, 0.6, 4.26, 0.0, -25800, 10052800),
    Quarter('2025-Q3', 2.0, 2.9, 6.5, 9.0, 11.0, 0.6, 4.26, 0.0, -27000, 10025800),
    Quarter('2025-Q4', 2.0, 3.1, 6.0, 8.0, 10.0, 0.7, 4.22, 0.0, -25800, 10000000),
]
INITIAL = list(history)
