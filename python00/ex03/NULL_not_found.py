def NULL_not_found(object : any) ->int:
    if object and object == object:
        print("Type not Found")
        return 1
    match type(object).__name__:
        case "NoneType":
            print("Nothing: None", type(object))
        case "float":
            print("Cheese: nan", type(object))
        case "int":
            print("Zero: 0", type(object))
        case "str":
            print("Empty:", type(object))
        case "bool":
            print("Fake: False", type(object))
        case _:
            print("Type not Found")
            return 1
    return 0