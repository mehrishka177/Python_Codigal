fruits_by_color = {
    'Yellow': {'Banana', 'Pineapple', 'Passion_Fruit'},
    'Green': {'Avocado', 'Lime', 'Water_melon'},
    'Red': {'Strawberries', 'Apples', 'RaspBerries', 'Pomegranate'},
}


def build_fruit_and_colors():
    fruit_and_colors = {}
    for color, colored_fruits in fruits_by_color.items():
        to_add = {one_fruit: color for one_fruit in colored_fruits}
        fruit_and_colors.update(to_add)
    return fruit_and_colors


def fruit_color(fruit, fruits_and_colors):
    try:
        print('The color of', fruit, 'is', fruits_and_colors[fruit])
    except KeyError:
        print('There is no such fruit in our data base.')

fruit_and_colors = build_fruit_and_colors()

fruit_color('Banana', fruit_and_colors)
fruit_color('banana', fruit_and_colors) 
fruit_color('potato', fruit_and_colors)