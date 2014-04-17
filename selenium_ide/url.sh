#!/bin/bash
if [ $console_protocol = "https" ]; then
   echo 'storedVars["url"] = "$console_protocol://$console_ip";' >> Selenium_RC_Plugins/user-extensions.js
else
   echo 'storedVars["url"] = "$console_protocol://$console_ip:8888";' >> Selenium_RC_Plugins/user-extensions.js
fi
