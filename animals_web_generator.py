import json


searched_fields  = ['name', 'diet', 'type', 'location']
# ==============================================================================
# reading data
# ==============================================================================
def load_data(file_path):
    """ Load data from file"""
    with open(file_path, 'r') as handle:
        if file_path.endswith('json'):
            return json.load(handle)
        elif file_path.endswith('html') or file_path.endswith('htm'):
            return handle.read()

animals_data = load_data('animals_data.json')
html_data = load_data('animals_template.html')

# ==============================================================================
# saving data
# ==============================================================================
def save_data(file_path,text):
    """ Save data to html file """
    with open(file_path, 'w') as target:
        if file_path.endswith('html') or file_path.endswith('htm'):
            target.write(text)

# ==============================================================================
# printing data
# ==============================================================================
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

def transform_animal_data(animal ):
    """
    Extracts the required data form the animal_record
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


values_to_print = map(transform_animal_data, animals_data)

def stringify_animal_values(values_to_print):
    """
    prints all values from received list, if not None
    :param values_to_print: list of dictionaries with animal data
    :return: None
    """
    output = ""
    for animal in values_to_print:
        output += '\n\t<li class="cards__item">\n'
        if animal:
            for label, value in animal.items():
                if label == "Name":
                    output += f'\t\t<div class="card__title">{value}</div>\n'
                    output += f'\t\t\t<p class="card__text">\n'
                if label != "Name":
                    output += f'\t\t\t\t<strong>{label.capitalize()}:</strong> {value}<br>\n'

        output += '\t\t\t</p>\n\t\t</li>'
    return output


# ==================================================================================================

def replace_html_data(template:str, new_text):
    new_html = template.replace('__REPLACE_ANIMALS_INFO__', str(new_text))
    return new_html

# print(replace_html_data(html_data,stringify_animal_values(values_to_print)))

def main():
    new_html = replace_html_data(html_data,stringify_animal_values(values_to_print))
    save_data('animals.html', new_html)

if __name__ == '__main__':
    main()