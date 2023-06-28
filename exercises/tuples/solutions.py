def increase_version(version, breaking_change, new_features):
    x, y, z = version
    if breaking_change:
        return (x + 1, 0, 0)
    elif new_features:
        return (x, y + 1, 0)
    else:
        return (x, y, z + 1)
