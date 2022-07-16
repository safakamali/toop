from os import system, listdir
from requests import get, post
from Resources.config import DEFAULT_INSTALLED_PLUGINS
import configure
from Resources.appresorces import *

@Command("clear")
def clear(args):
    system(configure.ScreenClear_command)

@Command("echo")
def echo(args):
    print(args[0])

@Command("request")
def request(args):
    if args[0] == "post":
        req = post(args[1])
    else:
        req = get(args[1])
    print(req)
    print(req.content)

@Command("exit")
def exit(args):
    raise Exit

@Command("list")
def list(args):
    print(listdir())

@Command(">plugin")
def Plugin(args):
    def list():
        print(DEFAULT_INSTALLED_PLUGINS)
    def add(plugin):
        DEFAULT_INSTALLED_PLUGINS.append(plugin)
        LoadPlugins()
    
    if args[0] == 'list':
        list()
    elif args[0] == 'add':
        add(args[1])
        print("Plugin Installed")


def LoadPlugins():
    for plugin in DEFAULT_INSTALLED_PLUGINS:
        __import__("Resources.plugins." + plugin)

LoadPlugins()