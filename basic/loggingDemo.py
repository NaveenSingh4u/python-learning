# Logging level in Python
# 1. Critical 50
# 2. Error 40
# 3. Warning 30 (Default level)
# 4. Information 20
# 5. Debugging 10
# 6. Notset 0

# Setting Log : Logfile name ,Log message, logging level
# basicConfig function for logging.
import logging
# filemode is optional 'w' means it will overwrite the log file
# level : define that on Debug or above level log message will be stored in the file.
#logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='w')

# basicConfig without constructor will print log message on console.
# In a file we can declare only one basic config of log file.
# by default log level is warning
#logging.basicConfig()

# for formatting with date
# datefmt is optional
# %I for 12 hour use %p (for AM/PM)
# %H for 24 hour format
logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', datefmt='%d %m %Y %I:%M:%S %p')

print("Demo of Simple log message")

logging.debug("Simple log message of debug")
logging.info("Simple log message of info")
logging.warning("Simple log message of warning")
logging.error("Simple log message of error")
logging.critical("Simple log message of critical")

# end
