def get_value_map(obj, mapping):
    value_map = {}
    for field_name, fn in mapping.items():
        field_value = getattr(obj, field_name, None)
        if field_value:
            value_map[field_value] = fn
    return value_map
