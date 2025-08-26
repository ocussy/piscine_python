def all_thing_is_obj(object: any) -> int:
    match type(object).__name__:
        case "list":
            print("List :", type(object))
        case "tuple":
            print("Tuple :", type(object))
        case "set":
            print("Set :", type(object))
        case "dict":
            print("Dict :", type(object))
        case "str":
            print(f"{object} is in the kitchen")
        case _:
            print("Type not found")
    return 42