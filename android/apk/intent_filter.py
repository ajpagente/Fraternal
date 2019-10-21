class IntentFilter:
    def __init__(self, actions, categories=[]):
        """
            action - the value of the action attribute android:name
            category - the value of the category attribute android:name
        """
        self.actions = actions
        self.categories = categories