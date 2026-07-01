
from Crypto import Random 
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA





print("=========================")

print("     Crypto Toolkit     ")

print("=========================")

aes_encrypted_data = None
rsa_encrypted_data = None
public_key = None
private_key = None

# key = Random.new().read(16)
# print(key)

encrypted_data = None
key =b'4\xfec\x05\xdd\xc7\xb1>\x13\xb9KJ\x8e|1\xa8'

def aes_encrypt():
    data = input("Enter text: ").encode()
    print("You entered:" , data)

    counter = Counter.new(128)
    c = AES.new(key , AES.MODE_CTR , counter=counter)

    encrypted_data = c.encrypt(data)
    print("Encrypted data: ", encrypted_data)
    return encrypted_data


def aes_decrypt(encrypted_data):
    counter = Counter.new(128)
    c = AES.new(key , AES.MODE_CTR , counter=counter)

    plaintext = c.decrypt(encrypted_data).decode()
    print("Decrypted data: ", plaintext)


def generate_rsa_keys():
    # bothKeys = RSA.generate(2028)
    # privateKey = bothKeys.exportKey()
    #publicKey = bothKeys.publickey().exportKey()
    

    # # print(privateKey)3
    # print("===================================")
    # print(publicKey)

    private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEjwIBAAKB/gzMm+FlK0zPVw2fj332mpnBdwpO9hu9/bJRwG0B8mSUrU7nhJG5\nurwBS18aKBCFdct3JpGd3NOIkn0/yFwHmtAMU2Dki9GgNJX4cGymUJKVMfyLxoA4\nrcvfemBlNwQ+yjgeCJotuGjtS03KababZWfrEOr4iIfeXT5UebWLrStRBkx2VGlR\nTcyZRgor5ko4dKrQBsTL4iLz0NRePcChJX2AkpwZ8naLs7bPB8KN4rzQRZ89iAeh\n6Bq7p2QpLQGJnKxr/u8qXdfGO/uXK+mXwD+MOLpe8bDGHvEGWFiricueMHwugAnX\nWXizNBj8Hvzp6l8T61a5yLCGwXGQyuI3AgMBAAECgf4GFjXZUjHt1Lqa/XMRXbm2\n/iS8z8FFfyxLZYpjrKXXxEbI+9v1K0TNDLaJ0xgTh0x2BsNeQ5sVM+EqVC9V6L3s\nS7hJH1cIyS3I1j2sxckSdIYxik1Lg+jOyAfcGLY5vByR5GKF49FLgPGrXGO6lhr6\n+PRyMeBH8O0Z67V3qyWeeeFv+FNOg7pk95c1JurkNTIHmxRLv1ULCU18NpbDRmRq\n8KoWCB1cw/QLIPSpRFPwdow1bVMKkvOz3NcG32Ai68y+S3RkKbK8Ng86L+M3uFcW\nAcbv2/At5bP6sIfHI4Tt/k2RJy5fqwJrBksEjzOl1IYaPBWyRsEyChZzRpE5WQJ/\nNhogtdPmIrl0h9AO3S/tJLRbhjxrgmlayPZV4YCqdPg5rRmDvxmvuMO6cD2P2bMK\nho15oTwkfy+apWbiyioELQpZUK/QQ64e0hIA4izi3NzTYNXEuGedYaWzo6EiTmMv\nX7oeehAouzmgQO4GYJNJ3PddTLGMdRaw10X3+0wj/wJ/PJA/9dEDuMNx/uM/9Fq+\ngqIpfJxls4pMmiXwZttbKx+0gRuCBpGFioEa5b0O2qq+OyzUkkrHeaekikIqvD53\n84FwqbZ2qY0D4x7cFq1f6Zk8RFD8gIM37MsUkPoVtxBx5BaBabXeFX/HryBcC/S7\nHHUt8W34aRyxAX+pO6FhyQJ/JYgKmRje1cgB5xWWuiq9QHE97OmNS3L6397DxSQV\nG//3QvYoRzHyjSJ6+9I5MLTb4GvUrN2kE/daONQfEFAFhZlgTHEq8UihaOnEYyLw\nXndyzAJ/7c0ziMIC1Mi7m9WCz821xsfe+cMIQQLeubBz1S5lMwcYgUG0fCK13Ub8\n0QJ/DGQzQfdW/Jm4nD8g2b0rV40YUe+p+1cjnzJ+An2FJMii5Puc2f0yRolt2G2b\nOXBP5cmhYKE+OQzs5IDvP37EiiUEySSVGNHKZtDslRM6GZCJvSyYzS6L5b4TYipZ\nARCzTMiyB8/3NYzkbVeAnc2f7w2mrcwjVFZTfQwCszmsyQJ/Gobc6nyR+95FmQd4\nawY0cFeT8Y5BPiDiYhb3jHGvLx2wtZyINhtGRn071NnpS2XryM2BWqhFIR1St+SR\n0EgpNKrO12/1CgEANEsH3XqouzAz6RucJN5AuiPpzJOJkxsOiJSLoC335mvnlHcG\n+aPSAKXAATn2+w1N5CORdlpaPA==\n-----END RSA PRIVATE KEY-----'
    public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBHjANBgkqhkiG9w0BAQEFAAOCAQsAMIIBBgKB/gzMm+FlK0zPVw2fj332mpnB\ndwpO9hu9/bJRwG0B8mSUrU7nhJG5urwBS18aKBCFdct3JpGd3NOIkn0/yFwHmtAM\nU2Dki9GgNJX4cGymUJKVMfyLxoA4rcvfemBlNwQ+yjgeCJotuGjtS03KababZWfr\nEOr4iIfeXT5UebWLrStRBkx2VGlRTcyZRgor5ko4dKrQBsTL4iLz0NRePcChJX2A\nkpwZ8naLs7bPB8KN4rzQRZ89iAeh6Bq7p2QpLQGJnKxr/u8qXdfGO/uXK+mXwD+M\nOLpe8bDGHvEGWFiricueMHwugAnXWXizNBj8Hvzp6l8T61a5yLCGwXGQyuI3AgMB\nAAE=\n-----END PUBLIC KEY-----'
    return public_key, private_key
    
def rsa_encrypt(public_key):
    public_key_new = RSA.import_key(public_key)
    data = input("Enter text: ").encode()
    c =PKCS1_OAEP.new(public_key_new) 
    encrypted_data = c.encrypt(data)
    return encrypted_data

def rsa_decrypt(private_key, encrypted_data):
    private_key_new = RSA.import_key(private_key)
    c =PKCS1_OAEP.new(private_key_new)
    plaintext = c.decrypt(encrypted_data).decode()
    print("Decrypted data: ", plaintext)



while True:
    print("1- AES Encrypt Text")
    print("2- AES Decrypt Text")
    print("3- RSA Encrypt Text")
    print("4- RSA Decrypt Text") 
    print("5- Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
       aes_encrypted_data = aes_encrypt()
      
    elif choice == "2":
        if aes_encrypted_data is not None:
            aes_decrypt(aes_encrypted_data)
        else:
            print("No encrypted data found.")

    elif choice == "3":
       public_key, private_key = generate_rsa_keys()
       rsa_encrypted_data = rsa_encrypt(public_key)
        
    elif choice == "4":
        if rsa_encrypted_data is not None:
            rsa_decrypt(private_key, rsa_encrypted_data)
        else:
            print("No RSA encrypted data found.")
    elif choice == "5":
        break
    else:
        print("Invalid Choice")

