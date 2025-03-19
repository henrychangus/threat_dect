import os 
import logging 
import torch
import json  

# Set up logging configuration 
def get_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 
    logger = logging.getLogger(__name__) 
    return logger

logger = get_logger()

config_file_loc = '/Users/henrychang/sys_security_ai/config/config.json'

def check_and_set_device():
    try:
        # Check and set the device once at the beginning 
        if torch.backends.mps.is_available(): 
            device = 0  # For MPS, use device ID 0 
            logger.info("Using MPS") 
        else: 
            device = -1  # For CPU, use device ID -1 
            logger.info("Using CPU")
    except Exception as e:
        logger.error(f"Unexpected error checking or setting device: {e}")
        device = -1  # Default to CPU in case of any error
    return device
  
def load_config(config_path):
    try:
        logger.info(f"Path for configuration file: {config_path}")
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        logger.info("Configuration file loaded successfully")
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {config_path}")
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from the configuration file: {config_path}")
    except Exception as e:
        logger.error(f"Unexpected error loading configuration: {e}")

def set_working_directory(desired_directory):
    try:
        # Set the desired working directory
        os.chdir(desired_directory)
        # Verify the change 
        current_directory = os.getcwd()
        logger.info(f"Current Working Directory: {current_directory}")
        return current_directory
    except FileNotFoundError:
        logger.error(f"Directory not found: {desired_directory}")
    except Exception as e:
        logger.error(f"Unexpected error setting working directory: {e}")