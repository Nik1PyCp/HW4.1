import logging
infologging=input("Веддіть свій логін: ")
password=input("Веддіть свій пароль: ")
logging.basicConfig(
    level=logging.INFO,
    filename = 'logs.log',
    filemode='a',
    format=f'[%(asctime)s] %(message)s'
)
logging.info(infologging)
logging.info(password)
logging.debug("DEBUG!")
logging.warning("WARNING!")
logging.error("ERROR!")
logging.critical("CRITICAL!")
