from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivymd.toast import toast
from kivy.clock import Clock
from notify import Notify
from sale import GridImage, DaiBox, Main_screen,S_popup,Sale_box
from profile import Profile,CustomDropDown,Review_card
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.uix.popup import Popup
from kivy.uix.button import Button


class MainApp(MDApp):
    gridi = None
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True,
        )



    def build(self):


        self.saturday = DaiBox()
        self.sunday = DaiBox()
        self.monday = DaiBox()
        self.tuesday = DaiBox()
        self.wednesday = DaiBox()
        self.thursday = DaiBox()
        self.friday = DaiBox()
        self.day = {
            'Saturday': self.saturday,
            'Sunday': self.sunday,
            'Monday': self.monday,
            'Tuesday': self.tuesday,
            'Wednesday': self.wednesday,
            'Thursday': self.thursday,
            'Friday': self.friday,

        }
        self.main_screen = Main_screen()
        self.s = self.main_screen.ids.scroll
        self.b = self.main_screen.ids.sale_box
        self.pro = self.main_screen.ids.profile
        self.pro_scr = self.pro.ids.pro_scr
        self.pro_scr.current = "review"
        self.category = self.b.ids.category
        self.titl = self.b.ids.title
        self.desc = self.b.ids.description
        self.amnt = self.b.ids.amount
        self.price = self.b.ids.price


        return self.main_screen


    def s_pop(self,*args):
        self.s_pop = S_popup()
        self.s_pop.open()

    def close_spopup(self,*args):
        self.s_pop.dismiss()



    def bottom_sheet(self,*args):
        self.b_menu = MDListBottomSheet(radius=15,radius_from="top")
        self.b_menu.add_item(text="Change Profile Photo",callback=self.pro_photo)
        self.b_menu.add_item(text="Change Cover Photo", callback=self.pro_photo)
        self.b_menu.open()


    def pro_photo(self,*args):
        print("Okk")

    def dailouge(self, id, *args):
        self.recent_day = self.day[id.text]
        self.modal = ModalView(size_hint=(0.95, 0.5), auto_dismiss=False)
        self.modal.add_widget(self.recent_day)
        self.modal.open()

    def dai_ok(self):
        self.modal.dismiss()
        Clock.schedule_once(self.daii_ok, 0.2)

    def daii_ok(self, *args):
        self.modal.clear_widgets()
        del self.modal

    def submit(self, *args):
        self.sat = [self.saturday.ids.a.active, self.saturday.ids.b.active, self.saturday.ids.c.active,
                    self.saturday.ids.d.active, self.saturday.ids.e.active]
        self.sun = [self.sunday.ids.a.active, self.sunday.ids.b.active, self.sunday.ids.c.active,
                    self.sunday.ids.d.active, self.sunday.ids.e.active]
        self.mon = [self.monday.ids.a.active, self.monday.ids.b.active, self.monday.ids.c.active,
                    self.monday.ids.d.active, self.monday.ids.e.active]
        self.tue = [self.tuesday.ids.a.active, self.tuesday.ids.b.active, self.tuesday.ids.c.active,
                    self.tuesday.ids.d.active, self.tuesday.ids.e.active]
        self.wed = [self.wednesday.ids.a.active, self.wednesday.ids.b.active, self.wednesday.ids.c.active,
                    self.wednesday.ids.d.active, self.wednesday.ids.e.active]
        self.thu = [self.thursday.ids.a.active, self.thursday.ids.b.active, self.thursday.ids.c.active,
                    self.thursday.ids.d.active, self.thursday.ids.e.active]
        self.fri = [self.friday.ids.a.active, self.friday.ids.b.active, self.friday.ids.c.active,
                    self.friday.ids.d.active, self.friday.ids.e.active]
        self.sat = [str(i) for i in self.sat]
        self.sun = [str(i) for i in self.sun]
        self.mon = [str(i) for i in self.mon]
        self.tue = [str(i) for i in self.tue]
        self.wed = [str(i) for i in self.wed]
        self.thu = [str(i) for i in self.thu]
        self.fri = [str(i) for i in self.fri]
        self.result = {}
        self.result["category"] = self.category.text
        self.result["title"] = self.titl.text
        self.result["description"] = self.desc.text
        self.result["amount"] = self.amnt.text
        self.result["Saturday"] = self.sat
        self.result["Sunday"] = self.sun
        self.result["Monday"] = self.mon
        self.result["Tuesday"] = self.tue
        self.result["Wednesday"] = self.wed
        self.result["Thursday"] = self.thu
        self.result["Friday"] = self.fri
        print(self.result)

    def file_manager_open(self):
        if self.gridi == None:
            self.file_manager.show('/storage/emulated/0/')
            self.manager_open = True
        else:
            toast("Only 1 Photo!")

    def select_path(self, path):
        if self.gridi == None:
            self.path = str(path)
            self.gridi = self.b.ids.grid_img
            self.grdimg = GridImage()
            self.img = self.grdimg.ids.img
            self.img.source = self.path
            self.gridi.add_widget(self.grdimg)
            self.exit_manager()
            toast(path)
        else:
            self.exit_manager()
            toast("Only 1 Photo!")


    def close_image(self, *args):
        self.gridi.remove_widget(self.grdimg)
        del self.grdimg
        del self.img
        self.gridi = None


    def exit_manager(self, *args):

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


MainApp().run()
