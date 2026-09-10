def ecosystem_health_score(values: dict[str, float]) -> float:
    """Normalize the weighted ecosystem health formula to a 0-100 score."""
    score = (
        values["species_diversity"] * 0.30
        + values["population_stability"] * 0.25
        + values["habitat_quality"] * 0.20
        + values["endangered_status"] * 0.15
        + values["environmental_conditions"] * 0.10
    )
    return round(score, 2)


def shannon_diversity(counts: list[int]) -> float:
    total = sum(counts)
    if total <= 0:
        return 0.0
    return round(-sum((count / total) * __import__("math").log(count / total) for count in counts if count), 4)


def simpson_diversity(counts: list[int]) -> float:
    total = sum(counts)
    if total <= 0:
        return 0.0
    return round(1 - sum((count / total) ** 2 for count in counts), 4)
