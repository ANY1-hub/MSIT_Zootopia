import json

def load_data(file_path):
    """ Load data from json file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
searched_fields  = ['name', 'diet', 'type', 'location']

# def print_animals(animals):
#     values_to_print = {}
#     for animal in animals:
#         characteristics = animal.get("characteristics")
#         values_to_print["Name"] = animal.get("name")
#         values_to_print["Diet"] = characteristics.get("diet") if characteristics else None
#         values_to_print["Locations"] = animal.get("locations")[0] if animal.get("locations") else None
#         values_to_print["Type"] = characteristics.get("type") if characteristics else None
#         for label, value in values_to_print.items():
#             if value is not None:
#                 print(f"{label}: {value}")
#         print()
# print_animals(animals_data)

# def print_animals_2(animals):
#     values_to_print = list(map(lambda x:
#                                {'Name':  x.get("name"),
#                                 'Diet': x.get('characteristics').get("diet") if  x.get('characteristics') else None,
#                                 'Locations': x.get("locations")[0] if x.get("locations") else None,
#                                 'Type': x.get('characteristics').get('type') if  x.get('characteristics') else None
#                                 }
#                                ,animals
#                                )
#                            )
#     print(values_to_print)
# print_animals_2(animals_data)
#     # values_to_print = list(map(lambda x: {key: x.get("key") for key in lookup_keys}))

def transform_animal(animal ):
    """
    Extraxts the required data form the animal_record
    :param animal: complex dictionary of all data on an animal
    :return: extracted, flattened animal data dict
    """
    characteristics = animal.get('characteristics')
    return {
        'Name': animal.get('name'),
        'Diet': characteristics.get('diet') if characteristics else None,
        'Type': characteristics.get('type') if characteristics else None,
        'Locations': animal.get('locations')[0] if animal.get('locations') else None
    }


values_to_print = map(transform_animal, animals_data)

def print_animal_values(values_to_print):
    """
    prints all values from received list, if not None
    :param values_to_print: list of dictionaries with animal data
    :return: None
    """
    for animal in values_to_print:
        print()
        if animal:
            for label, value in animal.items():
                if value:
                    print(f'{label.capitalize()}: {value}')

print_animal_values(values_to_print)


