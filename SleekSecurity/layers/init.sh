#! /bin/sh
#! /bin/bash
echo WELCOME , WE ARE FSOCIETY
echo GitHub '(Personal)' : https://github.com/AdroitAnurag
./pythonnmap.sh 2>/dev/null 
./rkinstall.sh 2>/dev/null  
./ufwinit.sh 2>/dev/null    
./avinit.sh 2>/dev/null     
./bvinit.sh 2>/dev/null
sudo ./passwordlesslogin.sh 2>/dev/null
./rkhunterscan.sh 2>/dev/null
read -p "Enter The Site :" sitename
./analyze_hosts.sh -s $sitename
./ssminit.sh 2>/dev/null
python wascan.py --url $sitename --scan [1,4]

