import traceback

from tasks.base.assets.assets_base_page import *


class Page:
    # Key: str, page name like "page_main"
    # Value: Page, page instance
    all_pages = {}

    @classmethod
    def clear_connection(cls):
        for page in cls.all_pages.values():
            page.parent = None

    @classmethod
    def init_connection(cls, destination):
        """
        Initialize an A* path finding among pages.

        Args:
            destination (Page):
        """
        cls.clear_connection()

        visited = [destination]
        visited = set(visited)
        while 1:
            new = visited.copy()
            for page in visited:
                for link in cls.iter_pages():
                    if link in visited:
                        continue
                    if page in link.links:
                        link.parent = page
                        new.add(link)
            if len(new) == len(visited):
                break
            visited = new

    @classmethod
    def iter_pages(cls):
        return cls.all_pages.values()

    @classmethod
    def iter_check_buttons(cls):
        for page in cls.all_pages.values():
            yield page.check_button

    def __init__(self, check_button):
        self.check_button = check_button
        self.links = {}
        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
        self.parent = None
        Page.all_pages[self.name] = self

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def link(self, button, destination):
        self.links[destination] = button


# Main page
#page_main = Page(MAIN_GOTO_CHARACTER)
page_main = Page(CHECK_MAIN)

# SUMMON 召唤
page_summon = Page(CHECK_SUMMON)
page_summon.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_SUMMON, destination=page_summon)

# WITCHES 魔女
page_witches= Page(CHECK_WITCHES)
page_witches.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_WITCHES, destination=page_witches)

# STARTRACE 星痕
page_startrace = Page(CHECK_STARTRACE)
page_startrace.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_STARTRACE, destination=page_startrace)

# WEAPONRY 唤物
page_weaponry = Page(CHECK_WEAPONRY)
page_weaponry.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_WEAPONRY, destination=page_weaponry)

# GUILD 公会
page_guild = Page(CHECK_GUILD)
page_guild.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_GUILD, destination=page_guild)

# DIVISION 神谕司
page_division = Page(CHECK_DIVISION)
page_division.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_DIVISION, destination=page_division)

# STORE 商店
page_store = Page(CHECK_STORE)
page_store.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_STORE, destination=page_store)

# BATTLE 战斗
page_battle = Page(CHECK_BATTALE)
page_battle.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_BATTLE, destination=page_battle)

# # POWER 星魂力
# page_power = Page(CHECK_POWER)
# page_power.link(POWER_CANCEL, destination=page_main)
# page_main.link(MAIN_GOTO_POWER, destination=page_power)

# TASK 任务
page_tasks = Page(CHECK_TASKS)
page_tasks.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_TASKS, destination=page_tasks)

# EVENT 活动
page_event = Page(CHECK_EVENT)
page_event.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_EVENT, destination=page_event)

# DICE 骰子
page_dice = Page(CHECK_DICE)
page_dice.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_DICE, destination=page_dice)

# MAIL 邮件
page_mail = Page(CHECK_MAIL)
page_mail.link(MAIL_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_MAIL, destination=page_mail)

# REPOSITORY 仓库
page_repository = Page(CHECK_REPOSITORY)
page_repository.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_REPOSITORY, destination=page_repository)

# MEDAL 勋章
page_medal = Page(CHECK_MEDAL)
page_medal.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_MEDAL, destination=page_medal)

# ARCHIVES 档案
page_archives = Page(CHECK_ARCHIVES)
page_archives.link(ANY_BACKTO_MAIN, destination=page_main)
page_main.link(MAIN_GOTO_ARCHIVES, destination=page_archives)

# Menu, entered from phone
# page_menu = Page(MENU_CHECK)
# page_menu.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_MENU, destination=page_menu)

# # Character
# page_character = Page(CHARACTER_CHECK)
# page_character.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_CHARACTER, destination=page_character)

# # Team
# page_team = Page(TEAM_CHECK)
# page_team.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_TEAM, destination=page_team)

# # Item, storage
# page_item = Page(ITEM_CHECK)
# page_item.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_ITEM, destination=page_item)

# # Guide, which includes beginners' guide, daily missions and dungeons
# page_guide = Page(GUIDE_CHECK)
# page_guide.link(GUIDE_CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_GUIDE, destination=page_guide)

# # Gacha
# page_gacha = Page(GACHA_CHECK)
# page_gacha.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_GACHA, destination=page_gacha)

# # Battle Pass
# page_battle_pass = Page(BATTLE_PASS_CHECK)
# page_battle_pass.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_BATTLE_PASS, destination=page_battle_pass)

# # Event
# page_event = Page(EVENT_CHECK)
# page_event.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_EVENT, destination=page_event)

# # Map
# page_map = Page(MAP_CHECK)
# page_map.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_MAP, destination=page_map)

# # page_world, subpage of map, used to choose a world/planet e.g. Herta Space Station
# page_world = Page(WORLD_CHECK)
# page_world.link(BACK, destination=page_map)
# page_map.link(MAP_GOTO_WORLD, destination=page_world)

# # Tutorial
# page_tutorial = Page(TUTORIAL_CHECK)
# page_tutorial.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_TUTORIAL, destination=page_tutorial)

# # Mission
# page_mission = Page(MISSION_CHECK)
# page_mission.link(CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_MISSION, destination=page_mission)

# # Message
# page_message = Page(MESSAGE_CLOSE)
# page_message.link(MESSAGE_CLOSE, destination=page_main)
# page_main.link(MAIN_GOTO_MESSAGE, destination=page_message)

# # Camera
# page_camera = Page(CAMERA_CHECK)
# page_camera.link(CLOSE, destination=page_menu)
# page_menu.link(MENU_GOTO_CAMERA, destination=page_camera)

# # Synthesize
# page_synthesize = Page(SYNTHESIZE_CHECK)
# page_synthesize.link(CLOSE, destination=page_menu)
# page_menu.link(MENU_GOTO_SYNTHESIZE, destination=page_synthesize)

# # Assignment
# page_assignment = Page(ASSIGNMENT_CHECK)
# page_assignment.link(CLOSE, destination=page_main)
# page_menu.link(MENU_GOTO_ASSIGNMENT, destination=page_assignment)

# # Forgotten Hall
# page_forgotten_hall = Page(FORGOTTEN_HALL_CHECK)
# page_forgotten_hall.link(CLOSE, destination=page_main)

# # Rogue, Simulated Universe
# page_rogue = Page(ROGUE_CHECK)
# page_rogue.link(CLOSE, destination=page_main)

# # Planner result
# page_planner = Page(PLANNER_CHECK)
# page_planner.link(CLOSE, destination=page_menu)


