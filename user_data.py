class UserData:
    def __init__(self):
        self.users = {
            "admin": "password123"  # Добавляем тестового пользователя с паролем
        }

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

    def get_progress(self, username):
        if username in self.users:
            return self.users[username].get("progress", {})
        return {}

    def get_test_results(self, username):
        if username in self.users:
            return self.users[username].get("test_results", {})
        return {}

    def update_progress(self, username, chapter):
        if username in self.users:
            if "progress" not in self.users[username]:
                self.users[username]["progress"] = {}
            self.users[username]["progress"][chapter] = True

    def update_test_result(self, username, chapter, result):
        if username in self.users:
            if "test_results" not in self.users[username]:
                self.users[username]["test_results"] = {}
            self.users[username]["test_results"][chapter] = result
