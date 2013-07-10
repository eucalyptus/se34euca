se34euca
========

Selenium 34 Eucalyptus -- Eucalyptus User Console Test Framework Based on Selenium

### TEST LIB CLASS
Directory: ./se34euca/lib/

Description: These classes hold the implementation of operations and interactions on the UI via Selenium Web-Driver
<pre>
EucaUITestLib_Base.py
EucaUITestLib_Image.py
EucaUITestLib_Instance.py
EucaUITestLib_IP_Address.py
EucaUITestLib_Keypair.py
EucaUITestLib_Security_Group.py
EucaUITestLib_Snapshot.py
EucaUITestLib_Volume.py
</pre>

### TEST LIB CONTAINER CLASS
Directory: ./se34euca/lib/

Description: This container class initializes the instances of the TEST LIB classes above
<pre>
EucaUITester.py
</pre>

### TEST CASE CLASS
Directory: ./se34euca/testcase/

Description: These classes arranges various operations in the TEST LIB classes to simulate specific user behaviors
<pre>
testcase_base.py
testcase_view_page.py 		- Test Cases for Viewing Pages
testcase_instance.py 		- Test Cases for Instance
testcase_keypair.py		- Test Cases for Keypair
testcase_volume.py		- Test Cases for Volume
testcase_snapshot.py		- Test Cases for Snapshot
testcase_security_group.py	- Test Cases for Security Group
testcase_ip_address.py		- Test Cases for IP Address
testcase_simulate_user.py	- Test Cases for Simulate User
</pre>

### EXECUTABLE
Directory: ./se34euca/

Description: Executables to run testcases, categorized by cloud resource groups
<pre>
runtest_view_page.py
runtest_instance.py
runtest_keypair.py
runtest_volume.py
runtest_snapshot.py
runtest_security_group.py
runtest_ip_address.py
runtest_simulate_user.py
</pre>

## INSTALLATION GUIDE

### ON CENTOS 6 LINUX OS

<code>
sudo yum -y install git

<code>
git clone git://github.com/eucalyptus/se34euca.git

<code>
cd ./se34euca/etc/

<code>
./installer_se34euca_centos.py

<code>
cd ..

### ON UBUNTU LINUX OS

<code>
sudo apt-get -y install git-core

<code>
git clone git://github.com/eucalyptus/se34euca.git

<code>
cd ./se34euca/etc/

<code>
./installer_se34euca_ubuntu.py

<code>
cd ..

## USAGE

### Prerequisite

1 Run the command below on your console:

<code>
cd ./se34euca

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

  * Or, add the 2 lines above to the file .bash_profile in your home directory.

2 Have the Account, User and its Password Populated.
  * Se34Euca scripts do not automatically create a user for testing.

### View Page Test

<code>
./runtest_view_page.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is: 

     [ check_login_and_logout, view_keypairs_page, view_running_page, view_volumes_page, view_secuirty_groups_page, view_all_page, view_all_page_in_loop, get_dashboard_source ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_view_page.py -i 192.168.51.131 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t view_all_page

<code>
./runtest_view_page.py -i 192.168.51.131 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t view_keypairs_page

<code>
./runtest_view_page.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t get_dashboard_source

<code>
./runtest_view_page.py -i 192.168.51.131 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t view_all_page_in_loop


### Instance Test

<code>
./runtest_instance.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

	[ launch_instance_basic, terminate_instance_basic, terminate_instance_all ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_instance.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t launch_instance_basic

<code>
./runtest_instance.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t terminate_instance_basic

<code>
./runtest_instance.py -i 192.168.51.158 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t terminate_instance_all


### Keypair Test

<code>
./runtest_keypair.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

	[ generate_keypair, delete_keypair ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_keypair.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t generate_keypair

<code>
./runtest_keypair.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_keypair

<code>
./runtest_keypair.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_keypair_all

### Volume Test

<code>
./runtest_volume.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

        [ create_volume, delete_volume, create_snapshot_from_volume ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_volume

<code>
./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_volume

<code>
./runtest_volume.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_snapshot_from_volume

### Snapshot Test

<code>
./runtest_snapshot.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

        [ delete_snapshot, create_volume_from_snapshot ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_snapshot.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_snapshot

<code>
./runtest_snapshot.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_volume_from_snapshot

### Security Group Test

<code>
./runtest_security_group.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

        [ create_security_group, delete_security_group ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_security_group.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t create_security_group

<code>
./runtest_security_group.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_security_group

<code>
./runtest_security_group.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t delete_security_group_all

### IP Address Test

<code>
./runtest_ip_address.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

        [ allocate_two_ip_addresses, release_ip_address ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_ip_address.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t allocate_two_ip_addresses

<code>
./runtest_ip_address.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t release_ip_address

### SIMULATE USER

<code>
./runtest_simulate.py -i [ui_ip] -p [port] -a [accountname] -u [username] -w [password] -t [testcase]

, where [testcase] is:

        [ simulate_user_case_00 ]

Example.

<code>
export PYTHONPATH=$PYTHONPATH:/root/ui-test/se34euca

<code>
export DISPLAY=:0

<code>
./runtest_simulate_user.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t simulate_user_case_00

<code>
./runtest_simulate_user.py -i 192.168.51.106 -p 8888 -a ui-test-acct-00 -u user00 -w mypassword1 -t simulate_user_case_00_in_loop

## Contact

Please contact developers for any questions or suggestions:

Kyo Lee

kyo.lee@eucalyptus.com

Alice

alice@eucalyptus.com



