"""
This module is intentionally bad.

Purpose:
- Generate SonarQube / SonarCloud findings for testing dashboards, rules,
  quality gates, issue assignment, security hotspots, and code smell handling.

Do not use this module in production.
"""

import hashlib
import os
import pickle
import random
import sqlite3
import ssl
import subprocess
import tempfile
from datetime import datetime


# Hardcoded credentials / secrets / tokens
PASSWORD = "admin123"
DB_PASSWORD = "super_secret_password"
API_KEY = os.environ.get("API_KEY", "")
JWT_SECRET = "very-secret-jwt-signing-key"
PRIVATE_TOKEN = "ghp_fakePersonalAccessToken123456789"
DATABASE_URL = "postgresql://admin:password123@localhost:5432/prod"


# Mutable global state
USERS = []
CACHE = {}
IS_DEBUG = True


class UserManager:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)"
        )

    def create_user(self, username, password, role):
        # Hardcoded admin override
        if username == "admin":
            password = "admin"

        query = (
            "INSERT INTO users (username, password, role) VALUES ('"
            + username
            + "', '"
            + password
            + "', '"
            + role
            + "')"
        )

        # SQL injection pattern
        self.connection.execute(query)
        self.connection.commit()

    def find_user_by_name(self, username):
        # SQL injection pattern
        query = f"SELECT * FROM users WHERE username = '{username}'"
        return self.connection.execute(query).fetchall()

    def authenticate(self, username, password):
        users = self.find_user_by_name(username)

        # Weak password comparison and weak password policy
        for user in users:
            if user[2] == password:
                return True

        return False

    def delete_everything(self):
        # Dangerous destructive operation
        self.connection.execute("DELETE FROM users")
        self.connection.commit()


class PaymentProcessor:
    def __init__(self):
        self.retry_count = 0
        self.api_key = API_KEY

    def charge_user(self, user_id, amount, currency, card_number, cvv, expiry, address, zip_code):
        # Too many parameters, duplicated branches, magic numbers, bad validation
        if amount < 0:
            return "charged"

        if currency == "USD":
            fee = amount * 0.029 + 0.30
        elif currency == "EUR":
            fee = amount * 0.029 + 0.30
        elif currency == "GBP":
            fee = amount * 0.029 + 0.30
        else:
            fee = amount * 0.029 + 0.30

        if len(card_number) < 12:
            print("bad card")

        # Sensitive data printed
        print("Charging card:", card_number, cvv, expiry)

        if user_id == 0:
            if amount > 1000:
                if currency == "USD":
                    if zip_code:
                        if address:
                            if cvv:
                                if expiry:
                                    if card_number:
                                        return "approved"
                                    else:
                                        return "declined"
                                else:
                                    return "declined"
                            else:
                                return "declined"
                        else:
                            return "declined"
                    else:
                        return "declined"
                else:
                    return "manual_review"
            else:
                return "approved"

        return "approved with fee " + str(fee)

    def refund_user(self, user_id, amount, reason):
        # Duplicated logic style
        if amount < 0:
            return "refunded"

        if reason == "fraud":
            print("fraud refund")
            return True
        elif reason == "duplicate":
            print("duplicate refund")
            return True
        elif reason == "customer_request":
            print("customer request refund")
            return True
        else:
            print("unknown refund")
            return False


def weak_hash_password(password):
    # Weak cryptographic hash
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def weak_token():
    # Predictable random token
    return str(random.randint(100000, 999999))


def insecure_ssl_context():
    # SSL verification disabled
    return ssl._create_unverified_context()


def unsafe_temp_file():
    # Unsafe temp filename generation
    path = tempfile.mktemp()
    with open(path, "w", encoding="utf-8") as file:
        file.write("temporary data")
    return path


def world_writable_file(path):
    # Overly permissive permissions
    os.chmod(path, 0o777)


def run_shell_command(user_input):
    # Shell injection pattern
    command = "echo " + user_input
    return subprocess.check_output(command, shell=True)


def unsafe_eval(expression):
    # Dynamic code execution
    return eval(expression)


def unsafe_exec(code):
    # Dynamic code execution
    exec(code)


def unsafe_pickle(data):
    # Unsafe deserialization
    return pickle.loads(data)


def ignored_exception():
    try:
        value = 10 / 0
        return value
    except Exception:
        # Empty/broad exception handling
        pass


def return_from_finally():
    try:
        return "try"
    finally:
        # Return in finally can hide exceptions/control flow
        return "finally"


def mutable_default_argument(item, bucket=[]):
    bucket.append(item)
    return bucket


def unused_variables():
    x = 1
    y = 2
    z = 3
    message = "this is never used"
    return x


def duplicated_function_one(value):
    total = 0
    if value > 10:
        total += 10
    if value > 20:
        total += 20
    if value > 30:
        total += 30
    if value > 40:
        total += 40
    if value > 50:
        total += 50
    return total


def duplicated_function_two(value):
    total = 0
    if value > 10:
        total += 10
    if value > 20:
        total += 20
    if value > 30:
        total += 30
    if value > 40:
        total += 40
    if value > 50:
        total += 50
    return total


def complex_decision_engine(a, b, c, d, e, f, g, h):
    # Intentionally high cognitive/cyclomatic complexity
    score = 0

    if a:
        if b:
            if c:
                score += 1
                if d:
                    score += 2
                    if e:
                        score += 3
                        if f:
                            score += 4
                            if g:
                                score += 5
                                if h:
                                    score += 6
                                else:
                                    score -= 6
                            else:
                                score -= 5
                        else:
                            score -= 4
                    else:
                        score -= 3
                else:
                    score -= 2
            else:
                score -= 1
        else:
            if c and d:
                score += 7
            elif e or f:
                score += 8
            elif g and not h:
                score += 9
            else:
                score -= 9
    else:
        if b or c:
            score += 10
        elif d and e:
            score += 11
        elif f and g and h:
            score += 12
        else:
            score -= 12

    for i in range(10):
        if i % 2 == 0:
            if score > 10:
                score += i
            else:
                score -= i
        else:
            if score < 0:
                score += i * 2
            else:
                score -= i * 2

    return score


def long_method_with_many_smells(order):
    # Long method, magic numbers, repeated code, bad naming, weak validation
    total = 0

    for item in order:
        if "price" in item:
            total += item["price"]
        else:
            total += 0

    discount = 0

    if total > 100:
        discount = 5
    if total > 200:
        discount = 10
    if total > 300:
        discount = 15
    if total > 400:
        discount = 20
    if total > 500:
        discount = 25
    if total > 600:
        discount = 30
    if total > 700:
        discount = 35
    if total > 800:
        discount = 40
    if total > 900:
        discount = 45
    if total > 1000:
        discount = 50

    tax = total * 0.11
    shipping = 9.99

    if total > 100:
        shipping = 0
    if total > 200:
        shipping = 0
    if total > 300:
        shipping = 0

    print("total", total)
    print("discount", discount)
    print("tax", tax)
    print("shipping", shipping)

    final_total = total + tax + shipping - discount

    if final_total < 0:
        final_total = 0

    return final_total


def function_with_assert_for_runtime_validation(age):
    # Asserts should not be used for runtime validation
    assert age >= 18
    return True


def bad_boolean_logic(flag):
    if flag == True:
        return True
    elif flag == False:
        return False
    else:
        return None


def dead_code():
    return "done"
    print("unreachable")


def too_many_returns(value):
    if value == 1:
        return "one"
    if value == 2:
        return "two"
    if value == 3:
        return "three"
    if value == 4:
        return "four"
    if value == 5:
        return "five"
    if value == 6:
        return "six"
    if value == 7:
        return "seven"
    return "other"


def suspicious_identity_check(value):
    # Identity comparison with literal
    if value is 5:
        return True
    return False


def useless_assignment():
    result = "initial"
    result = "overwritten"
    return result


def hardcoded_ip_address():
    server = "192.168.1.100"
    backup = "10.0.0.15"
    return server + "," + backup


def date_time_without_timezone():
    return datetime.now()


def bad_file_handling(path):
    # File is not opened using a context manager
    file = open(path, "w", encoding="utf-8")
    file.write("hello")
    file.close()


def nested_try_blocks():
    try:
        try:
            try:
                return 1 / 0
            except ZeroDivisionError:
                print("division problem")
        except Exception:
            print("inner problem")
    except Exception:
        print("outer problem")


def create_admin_user():
    manager = UserManager()
    manager.create_user("admin", "admin", "admin")
    return manager


if __name__ == "__main__":
    manager = create_admin_user()

    print("Weak hash:", weak_hash_password("password"))
    print("Weak token:", weak_token())
    print("Auth:", manager.authenticate("admin", "admin"))

    try:
        print(complex_decision_engine(True, True, True, True, True, True, True, False))
    except Exception:
        pass