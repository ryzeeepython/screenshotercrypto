import config

class Users:
    def check_is_admin(self, user_id):
        admins = config.admins
        for i in range(len(admins)):
            if str(user_id) == str(admins[i]):
                return True
        return False
    
    def check_is_paid(self, user_id, username):
        with open('members.txt', 'r' ) as f:
            for line in f.readlines():
                if str(line.lstrip().replace('\n', '', 1)) == str(user_id) or str(line.lstrip().replace('\n', '', 1)) == str(username):
                    return True
            return False

        
    def add_member(self, user_id):
        with open('members.txt', 'a') as f:
            f.write(f'{user_id}\n')

    def get_members(self):
        res =  ''
        with open('members.txt', 'r') as f:
            for line in f.readlines:
                res += line
        return res