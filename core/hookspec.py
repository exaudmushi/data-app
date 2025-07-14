import pluggy

hookspec = pluggy.HookspecMarker("datalab")

class DataLabSpecs:
    @hookspec
    def plugin_install(self, gui_context): pass

    @hookspec
    def plugin_check(): pass

    @hookspec
    def run_analysis(data): pass
