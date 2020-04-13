"""Visualisation functions.

Don't edit this file!
"""

def show_vegetation_type(vegetation_type: list):
    """Show an image of the vegetation type.

    Don't edit this function!
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.patches import Patch

    entries = [
        'No Vegetation',
        'Open Forest',
        'Forest',
        'Open Woodland',
        'Woodland',
        'Pine Forest',
        'Arboretum',
        'Grassland',
        'Shrubland',
        'Golf Course',
        'Urban Vegetation',
    ]
    numbers = {
        'No Vegetation': 0,
        'Open Forest': 1,
        'Forest': 2,
        'Open Woodland': 3,
        'Woodland': 4,
        'Pine Forest': 5,
        'Arboretum': 6,
        'Grassland': 7,
        'Shrubland': 8,
        'Golf Course': 9,
        'Urban Vegetation': 10,
    }
    colours = [
        '#000000',
        '#a6cee3',
        '#1f78b4',
        '#b2df8a',
        '#33a02c',
        '#fb9a99',
        '#e31a1c',
        '#fdbf6f',
        '#ff7f00',
        '#cab2d6',
        '#6a3d9a',
    ]

    vegetation_type = np.array(vegetation_type)
    colour_map = np.zeros_like(vegetation_type, dtype='float')
    for type_, number in numbers.items():
        colour_map[vegetation_type == type_] = number
    plt.imshow(
        colour_map,
        cmap=LinearSegmentedColormap.from_list(
            'vegetation_type', colours))
    plt.legend(
        handles=[
            Patch(color=colours[i], label=entries[i]) for i in range(1, 11)],
        loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def force_float(x):
    try:
        return float(x)
    except Exception:
        pass
    return float('nan')


def show_vegetation_density(vegetation_density: list):
    """Show an image of the vegetation density.

    Don't edit this function!
    """
    import numpy as np
    import matplotlib.pyplot as plt
    vegetation_density = [[force_float(ele) for ele in row]
                          for row in vegetation_density]
    vegetation_density = np.array(vegetation_density)
    plt.imshow(
        vegetation_density,
        cmap='Greens')
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def show_wind_speed(wind_speed: list):
    """Show an image of the wind speed.

    Don't edit this function!
    """
    import numpy as np
    import matplotlib.pyplot as plt
    wind_speed = [[force_float(ele) for ele in row]
                          for row in wind_speed]
    wind_speed = np.array(wind_speed)
    #print(wind_speed)
    plt.imshow(
        wind_speed,
        #cmap='magma_r',
        cmap='gist_heat_r',
        vmin=4.3)
    cb = plt.colorbar()
    cb.set_label('Average wind speed (km h$^{-1}$)')
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def show_bushfire(bushfire: list):
    """Show an image of the bushfire.
    
    Don't edit this function!
    """
    import numpy as np
    import matplotlib.pyplot as plt
    bushfire = [[force_float(ele) for ele in row] for row in bushfire]
    plt.imshow(np.array(bushfire, dtype=float), cmap='cool')
    plt.show()


def show_fire_risk(
        fire_risk,
        vegetation_type: list,
        vegetation_density: list,
        wind_speed: list):
    """Show an image of the fire risk.

    Don't edit this function!
    """
    import numpy as np
    import matplotlib.pyplot as plt
    fire_risk_map = []
    for y in range(len(wind_speed)):
        fire_risk_map_ = []
        for x in range(len(wind_speed[0])):
            fire_risk_map_.append(fire_risk(
                x, y, vegetation_type, vegetation_density, wind_speed))
        fire_risk_map.append(fire_risk_map_)
    plt.imshow(
        fire_risk_map,
        cmap='hot')
    plt.axis('off')
    cb = plt.colorbar()
    cb.set_label('Fire risk')
    plt.tight_layout()
    plt.show()
