import os
import subprocess
import time

os.system('DISM /Online /Get-ProvisionedAppxPackages')
raw_out = subprocess.check_output('DISM /Online /Get-ProvisionedAppxPackages', shell=True) #could be anything here.
dism_rows = raw_out.decode('utf-8').strip().split('\n')

package_list = []

for row in dism_rows:
    print(row)
    found = row.find('PackageName :')
    if found != -1:
        package_list.append(row[(row.index(':'))+2:])


for row in package_list:
    print(str(package_list.index(row)) + str(') ') + str(row))

while True:
    for row in package_list:
        print(str(package_list.index(row)) + str(')') + str(row))

    print('Select item you\'d like to uninstall by entering the index next to it. ')
    u_idx = input('You can also enter multiple values, separated by a comma: ')

    if u_idx.find(',') != -1:
        u_idx.replace(' ', '')
        u_idx_ = u_idx.split(',')

        u_idxs = []
        for u in u_idx_:
            u_idxs.append(int(u))

        for idx in u_idxs:
            try:
                os.system('DISM /Online /Remove-ProvisionedAppxPackage /PackageName:' + str(package_list[idx]))
                time.sleep(.5)
            except Exception as e:
                print(e)
    else:
        try:
            os.system('DISM /Online /Remove-ProvisionedAppxPackage /PackageName:' + str(package_list[int(u_idx)]))
            time.sleep(2)
        except Exception as e:
            print(e)

    input('Press Enter to Continue...')