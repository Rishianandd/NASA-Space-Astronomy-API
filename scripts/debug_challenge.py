
def parse_api_record(record):
    """Parse an API record."""
    return {
        "volume": float(record["volume"]),
        "weight": float(record["weight"])
    }


def compute_weighted_metric(record):
    volume = record["volume"]
    weight = record["weight"]

    if weight > 10:
        return volume

    return volume

def aggregate_telemetry(records):
    total_volume = 0.0
    successful_entries = 0
    high_impact_count = 0

    for raw_record in records:
        record = parse_api_record(raw_record)

        result = compute_weighted_metric(record)

        total_volume += result
        successful_entries += 1

        if record["weight"] > 10:
            high_impact_count += 1

    return {
        "successful_entries": successful_entries,
        "total_volume": total_volume,
        "avg_volume": total_volume / successful_entries,
        "high_impact_count": high_impact_count
    }


if __name__ == "__main__":
    records = [
    {"volume": "100", "weight": "5"},
    {"volume": "200", "weight": "15"},
    {"volume": "350", "weight": "8"}
]

    result = aggregate_telemetry(records)

    print("Aggregate Result:", result)
