from commands.command import Command
from display.display import display_tabulated
from display.display import display_permissions
from androguard.core.bytecodes import apk
from android.android import get_android_code
from android.android import get_android_ver_num


class ShowCommand(Command):

    def __init__(self, args):
        Command.__init__(self, args)
        # print(args)
        self.apkFile = args.apk
        
        if args.perm is None:
            self.want_permission = False
        else:
            self.want_permission = True

    def execute(self):
        
        a = apk.APK(self.apkFile)
        
        if self.want_permission:
            self.display_permissions(a)
        else:
            self.display_basic(a)

    def display_permissions(self, a):
        permissions = a.get_permissions()
        permissions.sort()
        # print(type(permissions))
        display_permissions(permissions)

    def display_basic(self, a):
        appname = a.get_app_name()
        package = a.get_package()
        ver_code = a.get_androidversion_code()
        ver_name = a.get_androidversion_name()
        min_sdk_ver = a.get_min_sdk_version()
        min_sdk_ver = self.beautify_api_level(min_sdk_ver)
        max_sdk_ver = a.get_max_sdk_version()
        max_sdk_ver = self.beautify_api_level(max_sdk_ver)
        tgt_sdk_ver = a.get_target_sdk_version()
        tgt_sdk_ver = self.beautify_api_level(tgt_sdk_ver)
        platform_build_ver_code = a.get_attribute_value("manifest", "platformBuildVersionCode")
        platform_build_ver_code = self.beautify_api_level(platform_build_ver_code)
        platform_build_ver_name = a.get_attribute_value("manifest", "platformBuildVersionName")
        
        data = []
        data.append(['File', self.apkFile])
        data.append(['App Name', appname])
        data.append(['Package', package])
        data.append(['Version Code', ver_code])
        data.append(['Version Name', ver_name])
        data.append(['Min SDK Version', min_sdk_ver])
        data.append(['Max SDK Version', max_sdk_ver])
        data.append(['Target SDK Version', tgt_sdk_ver])
        data.append(['Platform Build Version Code', platform_build_ver_code])
        data.append(['Platform Build Version Name', platform_build_ver_name])
        display_tabulated(data)    

    def beautify_api_level(self, version):
        if version is None:
            return version
        return version + " (" + get_android_code(version) + "," + get_android_ver_num(version) + ")"