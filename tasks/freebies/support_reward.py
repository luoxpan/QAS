from module.base.timer import Timer
from module.logger import logger
from tasks.base.assets.assets_base_page import CHECK_MAIN,CHECK_STORE,MAIN_GOTO_STORE
from tasks.base.assets.assets_base_popup import POPUP_GET_REWARD
from tasks.base.page import page_menu
from tasks.base.ui import UI
from module.ocr.ocr import DigitCounter
from tasks.freebies.assets.assets_freebies_support_reward import (
    GET_FRIENDSHIP_REWARD,
    STORE_GOTO_EXCHANGE,
    EXCHANGE_GOTO_FRIENDSHIP,
)


class SupportReward(UI):

    def run(self):
        """
        Run get support reward task
        """
        logger.hr('Support reward', level=1)
        self.ui_ensure(page_menu)
        self._goto_friendship()
        # self._goto_profile()
        self._get_reward()
        self._goto_menu()

    def _goto_friendship(self):
        """
        Pages:
            in: MENU
            out: FRIENDSHIP
        """
        skip_first_screenshot = False
        logger.info('Going to store')
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(GET_FRIENDSHIP_REWARD):
                logger.info('Successfully in friendship reward')
                return True
            
            if self.appear_then_click(MAIN_GOTO_STORE):
                continue

            if self.appear_then_click(STORE_GOTO_EXCHANGE):
                continue

            if self.appear_then_click(EXCHANGE_GOTO_FRIENDSHIP):
                continue


    def _get_reward(self, skip_first_screenshot=True):
        """
        Pages:
            in: STORE
            out: reward_appear()
        """
        logger.info('Getting reward')
        claimed = False
        empty = Timer(0.3, count=1).start()
        timeout = Timer(5).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(POPUP_GET_REWARD):
                logger.info('Got reward popup')
                break
            if timeout.reached():
                logger.warning('Get support reward timeout')
                break

            if self.appear_then_click(GET_FRIENDSHIP_REWARD, similarity=0.70, interval=2):
                claimed = True
                timeout.reset()
                continue

    def _goto_menu(self):
        """
        Pages:
            in: PROFILE or reward_appear
            out: MENU
        """
        skip_first_screenshot = False
        logger.info('Going to menu')
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(CHECK_MAIN):
                return True

            if self.appear_then_click(POPUP_GET_REWARD, interval=2):
                logger.info('Clicked on reward popup')
                # logger.info(f'{REWARD_POPUP} - {CLOSE}')
                # self.device.click(CLOSE)
                continue
            if self.handle_ui_close(CHECK_STORE, interval=2):
                continue
            # if self.handle_reward(click_button=CAN_GET_REWARD):
            #     # Avoid clicking on some other buttons
            #     continue


if __name__ == '__main__':
    self = SupportReward('src')
    self.device.screenshot()
    self.run()
