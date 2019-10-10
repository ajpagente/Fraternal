from commands.command import Command
from display.display import display_tabulated
from display.display import display_permissions
from androguard.core.bytecodes import apk
from android.android import get_android_code
from android.android import get_android_ver_num
from android.signature import Signature

class ShowCommand(Command):

    def __init__(self, args):
        Command.__init__(self, args)
        # print(args)
        self.apkFile = args.apk
        
        if args.perm is None:
            self.want_permission = False
        else:
            self.want_permission = True
        
        if args.sign is None:
            self.show_signature = False
        else:
            self.show_signature = True

    def execute(self):
        
        a = apk.APK(self.apkFile)
        
        if self.want_permission:
            self.display_permissions(a)
        elif self.show_signature:
            self.display_sign(a)
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

    # Display signing details
    def display_sign(self, a):
        signature = Signature(a)
        data = []
        data.append(['File', self.apkFile])
        data.append(['Is v1 signed', signature.is_v1])
        data.append(['Is v2 signed', signature.is_v2])
        data.append(['Is v3 signed', signature.is_v3])
        # display_tabulated(data)
        # data.clear

        certs = signature.certificates
        cert_count = len(certs)
        data.append(['', ''])
        data.append(['Certificates', '{} found'.format(cert_count)])
        for cert in certs:
            data.append(['Issuer',cert.issuer])
            data.append(['Subject',cert.subject])
            data.append(['Serial Number',cert.serial_num])
            data.append(['Hash Algorithm',cert.hash_algo])
            data.append(['Signature Algorithm',cert.sign_algo])
            data.append(['Valid not before',cert.valid_not_before])
            data.append(['Valid not after',cert.valid_not_after])
            hashes = cert.hashes
            for _hash in hashes:
                data.append(_hash)
            data.append(['', ''])
        public_keys = signature.public_keys
        key_count = len(public_keys)
        
        data.append(['Public Keys', '{} found'.format(key_count)])
        for key in public_keys:
            data.append(['Algorithm', key.algo])
            data.append(['Bit size', key.bit_size])
            data.append(['Fingerprint', key.fingerprint])
            data.append(['Hash Algorithm', key.hash_algo])
        display_tabulated(data)

    def beautify_api_level(self, version):
        if version is None:
            return version
        return version + " (" + get_android_code(version) + "," + get_android_ver_num(version) + ")"