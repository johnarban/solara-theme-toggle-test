import solara
from theme_toggle import ThemeToggle
from solara.components.component_vue import component_vue

clicks = solara.reactive(0)


@component_vue("clear_local_storage.vue")
def _ClearLocalStorage(vars = []):
    pass

@solara.component
def ClearLocalStorage(vars = []):
    return _ClearLocalStorage(vars=vars)
@solara.component
def Page():
    color = "green"
    if clicks.value >= 5:
        color = "red"

    def increment():
        clicks.value += 1
        print("clicks", clicks)  # noqa

    solara.Button(label=f"Clicked: {clicks}", on_click=increment, color=color)
    
    ClearLocalStorage(vars = [":solara:theme.variant"])
    

    
    ThemeToggle(
        on_icon="mdi-weather-night", # dark mode icon
        off_icon="mdi-brightness-7", # light mode icon
        enable_auto=False,
        # default_theme='light',
        default_to_server=True,
        # enforce_default=True,
    )