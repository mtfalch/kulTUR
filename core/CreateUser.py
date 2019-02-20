import email_validator as eval


class CreateUser:

    def __init__(
            self,
            first_name,
            last_name,
            email,
            tlf,
            password,
            username):

        self.first_name = first_name
        self.last_name = last_name
        self.email = CreateUser.set_email(email)
        self.tlf = CreateUser.set_tlf(tlf)
        self.password = CreateUser.set_password(password)
        self.username = CreateUser.set_username(username)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def set_email(email):
        CreateUser.email_check(email)
        return email

    @staticmethod
    def email_check(email):
        """Checks if the email CAN be a real email adress"""
        # TODO check if the email IS a real email through validation?
        eval.validate_email(email, allow_smtputf8=True, check_deliverability=True)

    @staticmethod
    def set_tlf(tlf):
        if CreateUser.check_tlf(tlf):
            return tlf
        raise Exception('Invalid phone number')

    @staticmethod
    def check_tlf(tlf):
        if len(tlf) == 8 and tlf.isdigit():
            return True
        return False

    @staticmethod
    def set_password(password):
        if CreateUser.check_password(password):
            return password
        raise Exception('The password must be at least 8 characters long, contain at least one uppercase letter and at '
                        'least one number.')

    @staticmethod
    def check_password(password):
        length = False
        uppercase = False
        digit = False

        if len(password) >= 8:
            length = True

        if any(l.isupper() for l in password):
            uppercase = True

        if any(l.isdigit() for l in password):
            digit = True

        if length and uppercase and digit:
            return True
        return False

    @staticmethod
    def set_username(username):
        if CreateUser.check_username(username):
            return username
        raise Exception('{} is already taken'.format(username))

    @staticmethod
    def check_username(username):
        # TODO check that the username is unique. Here we will need to access the database.
        return True

    def info(self):
        print('\nName: {}\nEmail: {}\nPhone: {}\nUsername: {}\nPassord: {}'.format(self.full_name(),
                                                                                   self.email,
                                                                                   self.tlf,
                                                                                   self.username,
                                                                                   self.password))



gunnar = CreateUser('Gunnar', 'Gunnarson', 'gønnegunnar@gmail.com', '12345678', 'Passord1', 'GønneGunnar')
gunnar.info()

