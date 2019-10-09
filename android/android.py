code_num = {
            '3':['Cupcake','1.5'],
            '4':['Donut','1.6'], 
            '5':['Eclair','2.0-2.1'], 
            '6':['Eclair','2.0-2.1'], 
            '7':['Eclair','2.0-2.1'],
            '8':['Froyo','2.2-2.2.3'],
            '9':['Gingerbread','2.3-2.3.7'],
            '10':['Gingerbread','2.3-2.3.7'],
            '11':['Honeycomb','3.0-3.2.6'],
            '12':['Honeycomb','3.0-3.2.6'],
            '13':['Honeycomb','3.0-3.2.6'],
            '14':['Ice Cream Sandwich','4.0-4.0.4'],
            '15':['Ice Cream Sandwich','4.0-4.0.4'],
            '16':['Jelly Bean','4.1–4.3.1'],
            '17':['Jelly Bean','4.1–4.3.1'],
            '18':['Jelly Bean','4.1–4.3.1'],
            '19':['KitKat','4.4–4.4.4'],
            '20':['KitKat','4.4–4.4.4'],
            '21':['Lollipop','5.0–5.1.1'],
            '22':['Lollipop','5.0–5.1.1'],
            '23':['Marshmallow','6.0–6.0.1'],
            '24':['Nougat','7.0–7.1.2'],
            '25':['Nougat','7.0–7.1.2'],
            '26':['Oreo','8.0–8.1'],
            '27':['Oreo','8.0–8.1'],
            '28':['Pie','9.0'],
            '29':['Android 10','10.0']
}

perm_info = {
            'ACCEPT_HANDOVER':['Dangerous','28','NA'],
            'ACCESS_BACKGROUND_LOCATION':['Dangerous','29','NA'], 
            'ACCESS_CHECKIN_PROPERTIES':['System','1', 'NA'], 
            'ACCESS_COARSE_LOCATION':['Dangerous','1','NA'], 
            'ACCESS_FINE_LOCATION':['Dangerous','1','NA'],
            'ACCESS_LOCATION_EXTRA_COMMANDS':['Normal','1','NA'],
            'ACCESS_MEDIA_LOCATION':['Dangerous','29','NA'],
            'ACCESS_NETWORK_STATE':['Normal','1','NA'],
            'ACCESS_NOTIFICATION_POLICY':['Normal','23','NA'],
            'ACCESS_WIFI_STATE':['Normal','1','NA'],
            'ACCOUNT_MANAGER':['System','5','NA'],
            'ACTIVITY_RECOGNITION':['Dangerous','29','NA'],
            'ADD_VOICEMAIL':['Dangerous','14','NA'],
            'ANSWER_PHONE_CALLS':['Dangerous','26','NA'],
            'BATTERY_STATS':['Sign|Priv|Devt','1','NA'],
            'BIND_ACCESSIBILITY_SERVICE':['Signature','16','NA'],
            'BIND_APPWIDGET':['System','3','NA'],
            'BIND_AUTOFILL_SERVICE':['Signature','26','NA'],
            'BIND_CALL_REDIRECTION_SERVICE':['Sign|Priv','29','NA'],
            'BIND_CARRIER_MESSAGING_CLIENT_SERVICE':['Signature','29','NA'],
            'BIND_CARRIER_MESSAGING_SERVICE':['Sign|Priv','22','23'],
            'BIND_CARRIER_SERVICES':['Sign|Priv','23','NA'],
            'BIND_CHOOSER_TARGET_SERVICE':['Signature','23','NA'],
            'BIND_CONDITION_PROVIDER_SERVICE':['Signature','24','NA'],
            'BIND_DEVICE_ADMIN':['Signature','8','NA'],
            'BIND_DREAM_SERVICE':['Signature','21','NA'],
            'BIND_INCALL_SERVICE':['Sign|Priv','23','NA'],
            'BIND_INPUT_METHOD':['Signature','3','NA'],
            'BIND_MIDI_DEVICE_SERVICE':['Signature','23','NA'],
            'BIND_NFC_SERVICE':['Signature','19','NA'],
            'BIND_NOTIFICATION_LISTENER_SERVICE':['Signature','18','NA'],
            'BIND_PRINT_SERVICE':['Signature','19','NA'],
            'BIND_QUICK_SETTINGS_TILE':['System','24','NA'],
            'BIND_REMOTEVIEWS':['Sign|Priv','11','NA'],
            'BIND_SCREENING_SERVICE':['Sign|Priv','24','NA'],
            'BIND_TELECOM_CONNECTION_SERVICE':['Sign|Priv','23','NA'],
            'BIND_TEXT_SERVICE':['Signature','14','NA'],
            'BIND_TV_INPUT':['Sign|Priv','21','NA'],
            'BIND_VISUAL_VOICEMAIL_SERVICE':['Sign|Priv','26','NA'],
            'BIND_VOICE_INTERACTION':['Signature','21','NA'],
            'BIND_VPN_SERVICE':['Signature','14','NA'],
            'BIND_VR_LISTENER_SERVICE':['Signature','24','NA'],
            'BIND_WALLPAPER':['Sign|Priv','8','NA'],
            'BLUETOOTH':['Normal','1','NA'],
            'BLUETOOTH_ADMIN':['Normal','1','NA'],
            'BLUETOOTH_PRIVILEGED':['System','19','NA'],
            'BODY_SENSORS':['Dangerous','20','NA'],
            'BROADCAST_PACKAGE_REMOVED':['System','1','NA'],
            'BROADCAST_SMS':['System','2','NA'],
            'BROADCAST_STICKY':['Normal','1','NA'],
            'BROADCAST_WAP_PUSH':['System','2','NA'],
            'CALL_COMPANION_APP':['Normal','29','NA'],
            'CALL_PHONE':['Dangerous','1','NA'],
            'CALL_PRIVILEGED':['System','1','NA'],
            'CAMERA':['Dangerous','1','NA'],
            'CAPTURE_AUDIO_OUTPUT':['System','19','NA'],
            'CHANGE_COMPONENT_ENABLED_STATE':['System','1','NA'],
            'CHANGE_CONFIGURATION':['Sign|Priv|Devt','1','NA'],
            'CHANGE_NETWORK_STATE':['Normal','1','NA'],
            'CHANGE_WIFI_MULTICAST_STATE':['Normal','4','NA'],
            'CHANGE_WIFI_STATE':['Normal','1','NA'],
            'CLEAR_APP_CACHE':['Sign|Priv','1','NA'],
            'CONTROL_LOCATION_UPDATES':['System','1','NA'],
            'DELETE_CACHE_FILES':['Sign|Priv','1','NA'],
            'DELETE_PACKAGES':['System','1','NA'],
            'DIAGNOSTIC':['System','1','NA'],
            'DISABLE_KEYGUARD':['Normal','1','NA'],
            'DUMP':['System','1','NA'],
            'EXPAND_STATUS_BAR':['Normal','1','NA'],
            'FACTORY_TEST':['System','1','NA'],
            'FOREGROUND_SERVICE':['Normal','28','NA'],
            'GET_ACCOUNTS':['Dangerous','1','NA'],
            'GET_ACCOUNTS_PRIVILEGED':['Sign|Priv','23','NA'],
            'GET_PACKAGE_SIZE':['Normal','1','NA'],
            'GET_TASKS':['NA','1','21'],
            'GLOBAL_SEARCH':['Sign|Priv','4','NA'],
            'INSTALL_LOCATION_PROVIDER':['System','4','NA'],
            'INSTALL_PACKAGES':['System','1','NA'],
            'INSTALL_SHORTCUT':['Normal','19','NA'],
            'INSTANT_APP_FOREGROUND_SERVICE':['Sign|Devt|Ins|Appop','26','NA'],
            'INTERNET':['Normal','1','NA'],
            'KILL_BACKGROUND_PROCESSES':['Normal','8','NA'],
            'LOCATION_HARDWARE':['System','18','NA'],
            'MANAGE_DOCUMENTS':['System','19','NA'],
            'MANAGE_OWN_CALLS':['Normal','26','NA'],
            'MASTER_CLEAR':['System','1','NA'],
            'MEDIA_CONTENT_CONTROL':['System','19','NA'],
            'MODIFY_AUDIO_SETTINGS':['Normal','1','NA'],
            'MODIFY_PHONE_STATE':['System','1','NA'],
            'MOUNT_FORMAT_FILESYSTEMS':['System','3','NA'],
            'MOUNT_UNMOUNT_FILESYSTEMS':['System','1','NA'],
            'NFC':['Normal','9','NA'],
            'NFC_TRANSACTION_EVENT':['Normal','28','NA'],
            'PACKAGE_USAGE_STATS':['Sign|Priv|Devt|Appop','23','NA'],
            'PERSISTENT_ACTIVITY':['NA','1','15'],
            'PROCESS_OUTGOING_CALLS':['Dangerous','1','29'],
            'READ_CALENDAR':['Dangerous','1','NA'],
            'READ_CALL_LOG':['Dangerous','16','NA'],
            'READ_CONTACTS':['Dangerous','1','NA'],
            'READ_EXTERNAL_STORAGE':['Dangerous','16','NA'],
            'READ_INPUT_STATE':['System','1','16'],
            'READ_LOGS':['System','1','NA'],
            'READ_PHONE_NUMBERS':['Dangerous','26','NA'],
            'READ_PHONE_STATE':['Dangerous','1','NA'],
            'READ_SMS':['Dangerous','1','NA'],
            'READ_SYNC_SETTINGS':['Normal','1','NA'],
            'READ_SYNC_STATS':['Normal','1','NA'],
            'READ_VOICEMAIL':['Sign|Priv','21','NA'],
            'REBOOT':['System','1','NA'],
            'RECEIVE_BOOT_COMPLETED':['Normal','1','NA'],
            'RECEIVE_MMS':['Dangerous','1','NA'],
            'RECEIVE_SMS':['Dangerous','1','NA'],
            'RECEIVE_WAP_PUSH':['Dangerous','1','NA'],
            'RECORD_AUDIO':['Dangerous','1','NA'],
            'REORDER_TASKS':['Normal','1','NA'],
            'REQUEST_COMPANION_RUN_IN_BACKGROUND':['Normal','26','NA'],
            'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND':['Normal','26','NA'],
            'REQUEST_DELETE_PACKAGES':['Normal','26','NA'],
            'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS':['Normal','23','NA'],
            'REQUEST_INSTALL_PACKAGES':['Signature','23','NA'],
            'REQUEST_PASSWORD_COMPLEXITY':['Normal','29','NA'],
            'RESTART_PACKAGES':['NA','1','15'],
            'SEND_RESPOND_VIA_MESSAGE':['System','18','NA'],
            'SEND_SMS':['Dangerous','1','NA'],
            'SET_ALARM':['Normal','9','NA'],
            'SET_ALWAYS_FINISH':['System','1','NA'],
            'SET_ANIMATION_SCALE':['System','1','NA'],
            'SET_DEBUG_APP':['System','1','NA'],
            'SET_PREFERRED_APPLICATIONS':['NA','1','15'],
            'SET_PROCESS_LIMIT':['System','1','NA'],
            'SET_TIME':['System','8','NA'],
            'SET_TIME_ZONE':['System','1','NA'],
            'SET_WALLPAPER':['Normal','1','NA'],
            'SET_WALLPAPER_HINTS':['Normal','1','NA'],
            'SIGNAL_PERSISTENT_PROCESSES':['System','1','NA'],
            'SMS_FINANCIAL_TRANSACTIONS':['Sign|Appop','29','NA'],
            'START_VIEW_PERMISSION_USAGE':['Sign|Inst','29','NA'],
            'STATUS_BAR':['System','1','NA'],
            'SYSTEM_ALERT_WINDOW':['Sign|Pre|Appop|Pre23|Devt','1','NA'],
            'TRANSMIT_IR':['Normal','19','NA'],
            'UNINSTALL_SHORTCUT':['NA','19','No Support'],
            'UPDATE_DEVICE_STATS':['System','3','NA'],
            'USE_BIOMETRIC':['Normal','28','NA'],
            'USE_FINGERPRINT':['Normal','23','28'],
            'USE_FULL_SCREEN_INTENT':['Normal','29','NA'],
            'USE_SIP':['Dangerous','9','NA'],
            'VIBRATE':['Normal','1','NA'],
            'WAKE_LOCK':['Normal','1','NA'],
            'WRITE_APN_SETTINGS':['System','1','NA'],
            'WRITE_CALENDAR':['Dangerous','1','NA'],
            'WRITE_CALL_LOG':['Dangerous','16','NA'],
            'WRITE_CONTACTS':['Dangerous','1','NA'],
            'WRITE_EXTERNAL_STORAGE':['Dangerous','4','NA'],
            'WRITE_GSERVICES':['System','1','NA'],
            'WRITE_SECURE_SETTINGS':['System','3','NA'],
            'WRITE_SETTINGS':['Sign|Pre|Appop|Pre23','1','NA'],
            'WRITE_SYNC_SETTINGS':['Normal','1','NA'],
            'WRITE_VOICEMAIL':['Sign|Priv','21','NA'],
}

def get_android_code(api_level):
    code,_ = code_num[api_level]
    return code

def get_android_ver_num(api_level):
    _,ver_num = code_num[api_level]
    return ver_num

def get_permission_protection_level(permission):
    try:
        protection_level,_,_ = perm_info[permission]
        return protection_level
    except KeyError:
        return None

def get_permission_added(permission):
    try:
        _,added,_ = perm_info[permission]
        return added
    except KeyError:
        return None

def get_permission_deprecated(permission):    
    try:
        _,_,deprecated = perm_info[permission]
        return deprecated
    except KeyError:
        return None

def is_permission_dangerous(permission):
    pass







