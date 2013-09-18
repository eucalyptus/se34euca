##Description of test suites:

UI-manual-tests suite checks major functionality of Instance operations, Storage operations, Security Group operations, IP Address operations, Key Pair operations and Image operations.

This suite can be run in parts: UI-manual-tests-part-1, UI-manual-tests-part-2, UI-manual-tests-part-3 run all test cases from UI-manual-tests in 3 shorter sequences.

Auto Scaling operations and  Launch Configuration operations can be tested by Auto-scaling-suite which is located in directory named AutoScaling.

##To run the Selenium IDE test suite: 


Selenium IDE is a Firefox plug-in. You can download it here: http://docs.seleniumhq.org/download/.

To run Selenium IDE open your Firefox browser and from "Tools" menu select "Selenium IDE"

To run a test suite: From "Files" menu in Selenium IDE select "Open test suite".

## Best practices:

Click on the little sand clock picture to enable automatic wait for element to be present on web page.

I recommend setting speed somewhat below "fast" to avoid Selenium IDE throwing an error caused by page components failing to load/respond quickly enough. 

## How to contribute

You can find our code submission framework here: https://github.com/eucalyptus/se34euca/wiki/Guidelines-to-contributing-to-se34euca-project

Tutorial on creating a Selenium IDE test: https://www.cs.drexel.edu/~spiros/teaching/SE320/slides/selenium.pdf  

  


Descrition of all Selenium IDE tests in alphabetical order.


allocate-ip -- Dashboard -> Network & security -> Allocate IP -> Allocate 1 IP

associate-ip-land-inst -- Dashboard -> Instances -> Associate IP to an instance

associate-ip-land-ip -- Dashboard -> Network & security -> IP Addresses -> Associate IP to instance

attach-volume-from-inst-page -- Dashboard -> Instances -> Attach volume to instance

attach-volume-from-volumes-page -- Dashboard -> Storage -> Volumes -> Attach volume to instance


chk-allocate-ip -- Verifies IP address count on Dashboard is 2

chk-allocate-ip-1 -- Verifies IP address count on Dashboard is 1

chk-attach-volume -- Verifies there is a volume in "attached" state on Volumes Landing Page

chk-create-key-pair -- Verifies key pair count on Dashboard is 1

chk-create-secutity-group -- Verifies security group count on Dashboard is 2

chk-create-volume -- Verifies volume count on Dashboard is 1

chk-create-volume-v -- Verifies that there is a volume named "v" on volumes landing page, verifies volume count on Dashboard is 1

chk-delete-key-pair -- Verifies key pair count on Dashboard is 0

chk-delete-security-group -- Verifies security count on Dashboard is 1

chk-delete-volume -- Verifies volume count on Dashboard is 0

chk-disas-ip-land-inst -- Prints instance id of instance that was associated and what is visible on IP addresses landing page at the monemt for comparison.

chk-launch-inst-from-images -- Verifies running instance count on Dashboard is 1

chk-launch-inst-from-instances -- Verifies running instance count on Dashboard is 1

chk-launch-instance-from-dboard -- Verifies running instance count on Dashboard is 2

chk-launch-more-like-this -- Verifies running instance count on Dashboard is 2

chk-launch-myinst -- Verifies that instance named "myinst" shows up on Instances Landing Page filtered by running instances

chk-release-ip -- Verifies that IP address count on Dashboard is 0

chk-security-gr-add-rules -- Opens security group expando and prints protocol #4

chk-terminate-instance -- Verifies that running instance count on Dashboard is 0

chk-terminate-instance-1 -- Verifies that running instance count on Dashboard is 1

create-key-pair -- Dashboard -> Network & security -> Key pairs -> Create new key pair

create-sec-group-with-rules -- Dashboard -> Network & security -> Create new security group -> Group created -> Create with SSH, HTTP, and ICMP rules enabled

create-secutity-group -- Dashboard -> Network & security -> Create new security group -> Group created -> Create an empty group

create-snapshot-register-as-inst -- Dashboard -> Storage -> Snapshots -> Create Snapshot ->  Create Image from snapshot

create-volume -- Dashboard -> Storage -> Volumes -> Create volume

create-volume-v -- Dashboard -> Storage -> Volumes -> Create volume named v

delete-all-instances -- Dashboard -> Instances -> Terminate all instances

delete-key-pair -- Dashboard -> Network & security -> Key pairs -> Delete a key pair

delete-security-group -- Dashboard -> Network & security -> Delete a security group 

delete-snapshots-all -- Dashboard -> Storage -> Snapshots -> Delete all snapshots

delete-volume -- Dashboard -> Storage -> Volumes -> Delete volume

delete-volumes-all -- Dashboard -> Storage -> Volumes -> Delete all volumes

detach-volume -- Dashboard -> Storage -> Volumes -> Detach volume

detach-volume-inst-page -- Dashboard -> Instances -> Detach volume

disassociate-ip-land-instances -- Dashboard -> Instances -> Disassociate IP

disassociate-ip-land-ip -- Dashboard -> Network & security -> IP Addresses -> Disassociate IP

import-key-pair -- Dashboard -> Network & security -> Import keypair

launch-inst-from-images -- Dashboard -> Images -> Launch instance

launch-inst-from-instances -- Dashboard -> Instances -> Launch instance

launch-inst-name-myinst  -- Dashboard ->  Launch instance, name it "myinst"

launch-instance-from-dboard -- Dashboard -> Launch instance

launch-more-like-this -- Dashboard -> Instances -> Launch more like this one

release-ip-to-cloud -- Dashboard -> Network & security -> IP Addresses -> Release IP to cloud

release-ip-while-associated -- Dashboard -> Network & security -> IP Addresses -> Release IP to cloud while associated to instance

security-gr-add-rules -- Dashboard -> Network & security -> Modify Security group -> Add SSH, HTTP, and ICMP rules

snapshot-from-snap-page -- Dashboard -> Snapshots -> Create new snaposhot

snapshot-from-volume -- Dashboard -> Storage -> Volumes -> Create snapshot from volume

snapshot-to-volume -- Dashboard -> Storage -> Snapshots -> Create volume from snapshot

terminate-instance -- Dashboard -> Instances -> Terminate instance


