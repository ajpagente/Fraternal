from androguard.misc import AnalyzeAPK
import os
import fnmatch

CURRENT_DIR = '../testApk/'
PATTERN = '*.apk'

def main(directory):
    print("Inside main")
    apks = get_apk_files(directory, PATTERN)
    a, d, dx = AnalyzeAPK(os.path.join(CURRENT_DIR, apks[0]))

    print("App name >>>")
    print(a.get_app_name())

    print("Android version code >>>")
    print(a.get_androidversion_code())

    print("Android version name >>>")
    print(a.get_androidversion_name())

    '''
    The minimum Android version the app supports.
    '''
    print("Minimum SDK version >>>")
    print(a.get_min_sdk_version())  

    '''
    Reference: https://developer.android.com/guide/topics/manifest/uses-sdk-element.html#max
    An integer designating the maximum API Level on which the application is designed to run.

    Future versions of Android (beyond Android 2.0.1) will no longer check or enforce the maxSdkVersion attribute during 
    installation or re-validation. Google Play will continue to use the attribute as a filter, however, when presenting users 
    with applications available for download.

    Warning: Declaring this attribute is not recommended. First, there is no need to set the attribute as means of blocking 
    deployment of your application onto new versions of the Android platform as they are released. 
    '''

    print("Maximum SDK version >>>")
    print(a.get_max_sdk_version())  

    '''
    Reference: https://developer.android.com/distribute/best-practices/develop/target-sdk

    Every new Android version introduces changes that bring significant security and performance improvements 
    – and enhance the user experience of Android overall. Some of these changes only apply to apps that explicitly declare support 
    through their targetSdkVersion manifest attribute (also known as the target API level).

    Configuring your app to target a recent API level ensures that users can benefit from these improvements, 
    while still allowing it to run on older Android versions. Targeting a recent API level also allows your app to take advantage 
    of the platform's latest features to delight your users.
    '''
    print("Target SDK version (Target API level) >>>")
    print(a.get_target_sdk_version())  

    print("Platform Build Version Code >>>")
    print(a.get_attribute_value("manifest", "platformBuildVersionCode"))

    print("Platform Build Version Name >>>")
    print(a.get_attribute_value("manifest", "platformBuildVersionName"))

    print("Debuggable? >>>")
    print(a.get_attribute_value("application", "debuggable"))

    print("-----------------------------------------")
    print("Exported >>>")
    print("Activity >>>>>>>")
    exported = a.get_all_attribute_value("activity", "exported", format_value=False)
    # print(type(exported))
    count = 0
    for export in exported:
        if export=="true":
            count+=1
    print(count)
    print("Provider >>>>>>>")
    exported = a.get_all_attribute_value("provider", "exported", format_value=False)
    count = 0
    for export in exported:
        if export=="true":
            count+=1
    print(count)
    print("Receiver >>>>>>>")
    exported = a.get_all_attribute_value("receiver", "exported", format_value=False)
    count = 0
    for export in exported:
        if export=="true":
            count+=1
    print(count)
    print("Service >>>>>>>")
    exported = a.get_all_attribute_value("service", "exported", format_value=False)
    count = 0
    for export in exported:
        if export=="true":
            count+=1
    print(count)
    print("-----------------------------------------")
    print("Is signed v1: {}".format(a.is_signed_v1()))
    print("Is signed v2: {}".format(a.is_signed_v2()))
    print("Is signed v3: {}".format(a.is_signed_v3()))

    print("Certificates >>>")
    print(a.get_certificates())

    print("-----------------------------------------")
    print("Permissions >>>")
    permissions = a.get_permissions()
    permissions.sort()
    output_files(permissions)

    print("Implied permissions >>>")
    implied_permissions = a.get_uses_implied_permission_list()
    implied_permissions.sort()
    output_files(implied_permissions)

    print("Activities >>> ")
    activities = a.get_activities()
    activities.sort()
    output_files(activities)

    print("Providers >>>")
    providers = a.get_providers()
    providers.sort()
    output_files(providers)

    print("Receivers >>>")
    receivers = a.get_receivers()
    receivers.sort()
    output_files(receivers)

    print("Services >>>")
    services = a.get_services()
    services.sort()
    output_files(services)

    # Analyze the files inside the APK - START
    print("Files and their types >>>")
    files_types = a.get_files_types()
    print(files_types)
    # Analyze the files inside the APK - END

# Reference: https://github.com/realpython/python-scripts/blob/master/scripts/10_find_files_recursively.py
def get_apk_files(filepath, pattern):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames, pattern):
                # matches.append(os.path.join(root, filename))  # full path
                matches.append(os.path.join(filename))  # just file name
        if matches:
            print("Found {} files:".format(len(matches)))
            output_files(matches)
            return matches
        else:
            print("No files found.")
    else:
        print("Sorry that path does not exist. Try again.")

def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)

def is_apk(file):
    print("Check if file is an apk")



if __name__ == '__main__':
    main(CURRENT_DIR)