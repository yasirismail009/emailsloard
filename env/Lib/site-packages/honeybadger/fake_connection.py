import logging

logger = logging.getLogger(__name__)

def send_notice(config, payload):
    logger.info('Development mode is enabled; this error will be reported if it occurs after you deploy your app.')
    logger.debug('The config used is {} with payload {}'.format(config, payload))
