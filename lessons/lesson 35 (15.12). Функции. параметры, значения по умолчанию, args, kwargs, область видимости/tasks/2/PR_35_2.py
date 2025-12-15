
#config1 = update_widget_settings(42, "часы", is_active=False, position=(100, 50), custom_colors=None)
#print(config1)
def update_widget_settings(user_id, widget_name, is_active=True, position=(0, 0), custom_colors= None):
    if custom_colors is None:
        colors_to_use = ["синий", "белый"]
    else:
        colors_to_use = custom_colors

    config = {
        'user_id': user_id,
        'widget': widget_name,
        'is_active': is_active,
        'position': position,
        'colors': colors_to_use
    }
    return config
config1 = update_widget_settings(42, "часы", is_active=False, position=(100, 50), custom_colors=["красный", "черный"])
print(config1)

config2 = update_widget_settings("user_001", "погода")
print(config2)

config3 = update_widget_settings(15, "новости", position=(200, 30))
print(config3)

