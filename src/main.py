from linkedIn.linkedIn_site import LinkedInSite
from log_wrapper import LogWrapper

# Initialize the LogWrapper
log_wrapper = LogWrapper()

# Create a logger for the current module
logger = log_wrapper.get_logger(__name__)

# Example usage
logger.debug('Debugging information')
logger.info('Informational message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical issue')


def main():
    linkedIn_site = LinkedInSite()
    #linkedIn_site.login()  # Log in to LinkedIn
    # You can add more actions after logging in
    input("Press Enter to exit...")
    
if __name__ == "__main__":
    main()
