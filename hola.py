
import kivy 
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

    
class Aplicacion(App):
    def build(self):
        Window.size = (500, 700)
        return FloatLayout()
    Builder.load_file('estilo.kv')
        



if __name__=="__main__":
    Aplicacion().run()





