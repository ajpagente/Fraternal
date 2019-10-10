from androguard.util import get_certificate_name_string
from asn1crypto import x509
from oscrypto import asymmetric
import hashlib
import binascii

class Signature:
    is_v1 = False
    is_v2 = False
    is_v3 = False
    certificates = []
    public_keys  = []

    def __init__ (self, apk):
        self.is_v1 = apk.is_signed_v1()
        self.is_v2 = apk.is_signed_v2()
        self.is_v3 = apk.is_signed_v3()
        certs = set(apk.get_certificates_der_v3() + apk.get_certificates_der_v2() + [apk.get_certificate_der(x) for x in apk.get_signature_names()])
        
        for cert in certs:           
            # print(type(cert))
            # print(type(x509_cert))
            self.certificates.append(Certificate(cert))

        pkeys = set(apk.get_public_keys_der_v3() + apk.get_public_keys_der_v2())
        for public_key in pkeys:
            x509_public_key = asymmetric.load_public_key(public_key)
            self.public_keys.append(PublicKey(x509_public_key))

class Certificate:
    issuer = None
    subject = None
    serial_num = None
    hash_algo = None
    sign_algo = None
    valid_not_before = None
    valid_not_after = None
    hashes = []

    # cert is of type <class 'bytes'>
    def __init__ (self, cert):
        x509_cert = x509.Certificate.load(cert)
        self.issuer = get_certificate_name_string(x509_cert.issuer, short=True)
        self.subject = get_certificate_name_string(x509_cert.subject, short=True)
        self.serial_num = hex(x509_cert.serial_number)
        self.hash_algo = x509_cert.hash_algo
        self.sign_algo = x509_cert.signature_algo
        self.valid_not_before = x509_cert['tbs_certificate']['validity']['not_before'].native
        self.valid_not_after = x509_cert['tbs_certificate']['validity']['not_after'].native
        self.hashes = self.__compute_hashes__(cert)

    def __compute_hashes__(self, x509_cert):
        hashfunctions = dict(md5=hashlib.md5,
                         sha1=hashlib.sha1,
                         sha256=hashlib.sha256,
                         sha512=hashlib.sha512,)
        hashes = []
        for k, v in hashfunctions.items():
            hashes.append([k, v(x509_cert).hexdigest()])
        return hashes

class PublicKey:
    algo = None
    bit_size = None
    fingerprint = None # A public key fingerprint is a short sequence of bytes used to identify a longer public key.
    hash_algo = None

    def __init__ (self, x509_public_key):
        self.algo = x509_public_key.algorithm
        self.bit_size = x509_public_key.bit_size
        self.fingerprint = binascii.hexlify(x509_public_key.fingerprint).decode('utf-8')
        try:
            self.hash_algo = x509_public_key.hash_algo
        except (ValueError, AttributeError):
            # RSA pkey does not have an hash algorithm
            pass

        