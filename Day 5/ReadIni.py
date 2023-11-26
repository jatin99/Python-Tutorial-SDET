import configparser 

#pip install configparser 

config = configparser.ConfigParser()

config.read("./Day 5/config.ini") 

host = config.get("Database","host")

print("data", host)

print(f"data {host}")