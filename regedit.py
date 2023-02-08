import winreg

       
path = winreg.HKEY_CURRENT_USER

software = winreg.OpenKeyEx(path, r"SOFTWARE\\")

old_Key = winreg.DeleteKey(software, "Elea")
new_key = winreg.CreateKey(software, "ELea")

winreg.SetValueEx(new_key, "VALOR ACTUAL !!!!!!!!!!!!!!!!", 0, winreg.REG_SZ, "0")

if new_key:
    winreg.CloseKey(new_key)