from dataclasses import dataclass


@dataclass
class RegistrationData:
    email : str
    password : str