import pyotp
def get_totp():
    otp = pyotp.TOTP('AD4SPT634O7E7M7D5G633B2HL5P65SER')
    return otp.now()
get_totp()