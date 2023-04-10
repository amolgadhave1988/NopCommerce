import inspect
import logging

class CustLogger:
    @staticmethod
    def custlogger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(".\\Logs\\Auto.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    # class LogGen:
    #     @staticmethod
    #     def loggen():
    #         logging.basicConfig(filename=".\\Logs\\Automation.log",
    #                             format='%(asctime)s: %(levelname)s: %(message)s',
    #                             filemode='w', datefmt='%m/%d/%Y %I:%M:%S %p')
    #         logger = logging.getLogger()
    #         logger.setLevel(logging.INFO)
    #         return logger