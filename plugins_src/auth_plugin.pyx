from pluggy import HookimplMarker

hookimpl = HookimplMarker("datalab")

@hookimpl
def plugin_check():
    return True

@hookimpl
def plugin_install(gui_context):
    gui_context.status_label.config(text="Installing Auth Plugin...")
