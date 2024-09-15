import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s] "
log_dir = "logs" 
log_filepath = os.path.join(log_dir,"running_logs.logs")
os.makedirs(log_dir, exit_ok=True)

logging.basicConfig(
    Level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Text_Summarization_ProjectLogger")
