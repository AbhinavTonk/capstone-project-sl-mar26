#1- Imports
import logging
import os

#2- Create Output Folder to save the logs for Observability
os.makedirs("output", exist_ok="True")

#3- Create Logging Configuration
logging.basicConfig(
    filename="output/agentic_ai.log",
    level=logging.DEBUG,
    filemode="w", #Overwrite the log file
    format="%(asctime)s | %(levelname)s | %(message)s"
)

#4- Getting Logger Instance
logger = logging.getLogger()