class Activity:
    def __init__(self, name, permission=None, exported=False, is_main=False):
        self.name = name
        self.exported= exported
        self.permission = permission
        self.is_main_activity = is_main
        self.intent_filters = []
    def append_intent_filter(self, intent_filter):
        self.intent_filters.append(intent_filter)
    def clear_intent_filter(self):
        self.intent_filters.clear()