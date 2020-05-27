from server import ServerSocket
import logging
import cv2
import time

logging.basicConfig(level=logging.WARN, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ShowImage = False

class Daemon:

    recentImage = None
    serverInstance = None
    yoloInstance = None

    def __init__(self):
        # 서버 데몬이 시작할 때 시작
        logger.info('Starting Server Daemon...')

        self.recentImage = []


    def start(self):
        logger.info('Starting ImageStreaming Server')
        self.serverInstance = ServerSocket('0.0.0.0', 4444)
        self.serverInstance.startReceiveRecentImage(self.recentImage)
        logger.info('Started Image Streaming Server')

        while True:
            logger.debug('Receving Image')

            if len(self.recentImage):

                if ShowImage:
                    logger.debug('Show Recent Image')
                    cv2.imshow('image', self.recentImage[0])
                    cv2.waitKey(1)

            time.sleep(0.5)

daemon = Daemon()
daemon.start()












