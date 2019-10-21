from android.apk.activity import Activity
from android.apk.intent_filter import IntentFilter

class Components:
    def __init__(self, apk):
        self.apk = apk
        self.activities = []
        self._get_all_activities()
        

    def _get_all_activities(self):
        activities = self.apk.get_all_attribute_value("activity", "name", format_value=False)
        
        for activity_name in activities:
            permission = self._get_activity_attribute(activity_name, "permission")
            exported = self._get_activity_attribute(activity_name, "exported")
            
            activity = Activity(activity_name, permission, exported)

            intent_filters = self.apk.get_intent_filters('activity', activity_name)
            # print(intent_filters)
            if intent_filters:
                actions = intent_filters['action']
                categories = []
                try: 
                    categories = intent_filters['category']
                except KeyError:
                    pass

                activity.intent_filters.append(IntentFilter(actions, categories))
            
            
            self.activities.append(activity)
            
        return activities

    def _get_activity_attribute(self, activity_name, attribute_name):
        return self.apk.get_attribute_value("activity", attribute_name, format_value=False, name=activity_name)