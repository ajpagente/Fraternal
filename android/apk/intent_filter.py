class IntentFilter:
    def __init__(self, action, category=None):
        """
            action - the value of the action attribute android:name
            category - the value of the category attribute android:name
        """
        self.action = action
        self.category = category