se34euca
========

Selenium 34 Eucalyptus -- Eucalyptus User Console Test Framework Based on Selenium

### CLASS
lib_euca_ui_test.py  		- Main Library for Exported Selenium Scripts
testcase_view_page.py 		- Test Cases for Viewing Pages
testcase_instance.py 		- Test Cases for Instance
testcase_keypair.py		- Test Cases for Keypair
testcase_volume.py		- Test Cases for Volume
testcase_snapshot.py		- Test Cases for Snapshot
testcase_security_group.py	- Test Cases for Security Group
testcase_ip_address.py		- Test Cases for IP Address

### EXECUTABLE
runtest_view_page.py
runtest_instance.py
runtest_keypair.py
runtest_volume.py
runtest_snapshot.py
runtest_security_group.py
runtest_ip_address.py

## USAGE

### PRE-REQ

export DISPLAY=:0

### PER TEST CASE

---
./runtest_view_page.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

       [ check_login_and_logout, view_keypairs_page, view_running_page, view_volumes_page, view_secuirty_groups_page, view_all_page, get_dashboard_source ]

Ex.

export DISPLAY=:0

./runtest_view_page.py -i 192.168.51.131 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t view_all_page

./runtest_view_page.py -i 192.168.51.131 -p 8888 -a ui-test-acct-03 -u admin -w mypassword6 -t view_keypairs_page

./runtest_view_page.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t get_dashboard_source

---


---

./runtest_instance.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

	[ launch_instance_basic, terminate_instance_basic ]

Ex.

export DISPLAY=:0

./runtest_instance.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t launch_instance_basic

./runtest_instance.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t terminate_instance_basic

---


---
./runtest_keypair.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

	[ generate_keypair, delete_keypair ]

Ex.

export DISPLAY=:0

./runtest_keypair.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t generate_keypair

./runtest_keypair.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_keypair

---

---
./runtest_volume.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

        [ create_volume, delete_volume, create_snapshot_from_volume ]

Ex.

export DISPLAY=:0

./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_volume

./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_volume

./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_snapshot_from_volume

---


---
./runtest_snapshot.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

        [ delete_snapshot ]

Ex.

export DISPLAY=:0

./runtest_snapshot.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_snapshot

./runtest_snapshot.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_volume_from_snapshot

---


---
./runtest_security_group.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

        [ create_security_group, delete_security_group ]

Ex.

export DISPLAY=:0

./runtest_security_group.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_security_group

./runtest_security_group.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_security_group

---

---
./runtest_ip_address.py -i <ui_ip> -p <port> -a <accountname> -u <username> -w <password> -t <testcase>

where <testcase>:

        [ allocate_two_ip_addresses, release_ip_address ]

Ex.

export DISPLAY=:0

./runtest_ip_address.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t allocate_two_ip_addresses

./runtest_ip_address.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t release_ip_address

---

