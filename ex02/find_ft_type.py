def all_thing_is_obj(object: any) -> int:
    object_type = type(object)

    if isinstance(object, str):
        print(f"{object} is in the kitchen : {object_type}")

    elif isinstance(object, (list, tuple, set, dict)):
        object_name = object_type.__name__.capitalize()
        print(f"{object_name} : {object_type}")

    else:
        print("Type not found")

    return 42
