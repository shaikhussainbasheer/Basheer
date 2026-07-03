from configparser import ConfigParser


config= ConfigParser()
config.read("config.ini")

url_retrieve=config.get("basic info","url")
print(url_retrieve)

