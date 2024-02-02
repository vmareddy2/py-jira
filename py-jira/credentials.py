import keyring
import os
import logging
logger = logging.getLogger(__name__)

def getUsernamePassword(service_name) -> (str, str):
    try:
        username = os.getenv("USER")
        # Attempt to retrieve the password from the keychain
        password = keyring.get_password(service_name, username)

        if password is not None:
            #logger.debug(f"Password for {username} in {service_name}: {password}")
            return (username, password)
        else:
            logger.error(f"No password found for {username} in {service_name}")
            return None
    except Exception as e:
        logger.error(f"Error retrieving password: {e}")
        return None