import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()
x = 10
name  = "Poonam"
name  = 10 
# Read the INI file
config.read('./Day 5/config.ini')

# Access valuescl
username = config.get('Settings', 'username')
password = config.get('Settings', 'password')
host = config.get('Database', 'host')
port = config.getint('Database', 'port')  # Use getint for integer values

# Print the values
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Host: {host}")
print(f"Port: {port}")
