import logging

class LogWrapper:
    def __init__(self, filename='app.log', level=logging.DEBUG):
        """
        Initializes the LogWrapper with specified filename and logging level.

        Args:
        filename (str): The name of the file to log to.
        level (logging.LEVEL): The logging level.
        """
        self.filename = filename
        self.level = level
        self.setup_logging()

    def setup_logging(self):
        """
        Sets up the basic configuration for logging.
        """
        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(self.level)

        # Create handlers
        file_handler = logging.FileHandler(self.filename)
        console_handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    def get_logger(self, name):
        """
        Returns a logger instance with the specified name.

        Args:
        name (str): The name of the logger.

        Returns:
        logging.Logger: A configured logger instance.
        """
        return logging.getLogger(name)
