import random

# Generate random key, alphanumeric with length 8
def generate_key():
    key = ''
    for i in range(8):
        key += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return key
