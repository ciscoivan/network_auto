import  logging
import netmiko
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')