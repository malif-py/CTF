out0 = "FHFgao}v}dZxcshuuly`ZxbyvqChym`teCmpeuix"
str1 = "dJaVaDjAvAdJaVaDjAvAdJaVaDjAvAdJaVaDjAvA"
str2 = "aVaJdAvAjDaVaJdAvAjDaVaJdAvAjDaVaJdAvAjD"

for i in range(len(str1)):
    print(chr(ord(out0[i]) ^ ord(str1[i]) ^ ord(str2[i])), end='')