def NULL_not_found(object: any) -> int:
    object_type = type(object)

    if object:
        if isinstance(object, float) and object == float("NaN"):
            print(f"Cheese: {object} {object_type}")
        else:
            print("Type not Found")
            return 1
    else:
        if object is None:
            print(f"Nothing: {object} {object_type}")
        elif isinstance(object, int):
            print(f"Zero: {object} {object_type}")
        elif isinstance(object, str):
            print(f"Empty: {object_type}")
        elif isinstance(object, bool):
            print(f"Fake: {object} {object_type}")
        else:
            print("Type not Found")
            return 1
    return 0
