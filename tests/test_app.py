import os

def test_env_variable_default():
    os.environ.pop("APP_ENV", None)
    assert os.getenv("APP_ENV", "Dev") == "Dev"

def test_env_variable_set():
    os.environ["APP_ENV"] = "QA"
    assert os.getenv("APP_ENV") == "QA"