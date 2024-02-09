from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

SHA256 = 256
SHA384 = 384
SHA512 = 512

RSA2048 = 2048
RSA3072 = 3072
RSA4096 = 4096

EXP65537 = 65537

class rsa_pss_test:
    def __init__(self, msg):
        self.msg = msg
        print("Init RSA-PSS", msg)

    def rsa_key_gen(self, key_size, pub_exp):
        pri = rsa.generate_private_key(pub_exp, key_size, )
        pub = pri.public_key()
        return (pri, pub)

    def rsa_sign(self, msg, prkey, hash_type):
        if hash_type == SHA256:
            ht = hashes.SHA256()
        sig = prkey.sign( msg, padding.PSS(mgf=padding.MGF1(ht), 
            salt_length=padding.PSS.MAX_LENGTH), ht)
        return sig

    def rsa_verify(self, pkey, sig, hash_type):
        if hash_type == SHA256:
            ht = hashes.SHA256()
            msg1 = b"A message I want to sig"
        try:
            out = pkey.verify(sig, self.msg, padding.PSS(mgf=padding.MGF1(ht),
                salt_length=padding.PSS.MAX_LENGTH), ht)
        except Exception as e:
            out = "Failed"
            print("Signature check failed")
        return out



#private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, )
message = b"A message I want to sign"
#signature = private_key.sign( message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
#public_key = private_key.public_key()
#out = public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
#print(out)
rverify = rsa_pss_test(message)
(pri, pub) = rverify.rsa_key_gen(RSA2048, EXP65537)
sig = rverify.rsa_sign(message, pri, SHA256)
print("signature",sig)
print("pubkey", pub)
print("sha", sha)
out = rverify.rsa_verify(pub, sig, SHA256)
print(out)
