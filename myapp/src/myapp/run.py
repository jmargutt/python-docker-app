import datetime
import logging
logging.basicConfig()
ch = logging.getLogger()
ch.setLevel(logging.WARNING)
from myapp.utils import print_welcome_message


def main():
    """
    template of a python app: print a message and exit
    """

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    try:
        print_welcome_message()
    except Exception as e:
        logging.error('Error in print_welcome_message')
        logging.error(e)

    logging.info('my-app ran at %s', utc_timestamp)


if __name__ == "__main__":
    main()
