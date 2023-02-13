import winreg
       
path = winreg.HKEY_CURRENT_USER

software = winreg.OpenKeyEx(path, r"SOFTWARE\Elea\Elea2\\")
open_key = winreg.CreateKey(software, "ELea3")
winreg.SetValueEx(open_key, "VALOR ", 0, winreg.REG_SZ, "122333")



old_Key = winreg.DeleteKey(software, "Elea")
new_key = winreg.CreateKey(software, "ELea")

winreg.SetValueEx(new_key, "VALOR ACTUAL !!!!!!!!!!!!!!!!", 0, winreg.REG_SZ, "0")

# if new_key:
#     winreg.CloseKey(new_key)
#Commit
