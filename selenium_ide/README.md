##Description of test suites:

UI-manual-tests suite checks major functionality of Instance operations, Storage operations, Security Group operations, IP Address operations, Key Pair operations and Image operations.

Descriptiopns of all test cases can be found here: https://github.com/eucalyptus/se34euca/wiki/Description-of-Selenium-IDE-test-cases
This suite can be run in parts: UI-manual-tests-part-1, UI-manual-tests-part-2, UI-manual-tests-part-3 run all test cases from UI-manual-tests in 3 shorter sequences.

Auto Scaling operations and  Launch Configuration operations can be tested by Auto-scaling-suite which is located in directory named AutoScaling.

##To run the Selenium IDE test suite: 


Selenium IDE is a Firefox plug-in. You can download it here: http://docs.seleniumhq.org/download/.

To run Selenium IDE open your Firefox browser and from "Tools" menu select "Selenium IDE"

To run a test suite: From "Files" menu in Selenium IDE select "Open test suite".

###For the suite to run correctly, you have to start with an "empty" Eucalyptus setup, where no resources were created yet.


## Best practices:

Click on the little sand clock picture to enable automatic wait for element to be present on web page.

I recommend setting speed somewhat below "fast" to avoid Selenium IDE throwing an error caused by page components failing to load/respond quickly enough. 

## How to contribute

You can find our code submission framework here: https://github.com/eucalyptus/se34euca/wiki/Guidelines-to-contributing-to-se34euca-project

Tutorial on creating a Selenium IDE test: https://www.cs.drexel.edu/~spiros/teaching/SE320/slides/selenium.pdf  

  


