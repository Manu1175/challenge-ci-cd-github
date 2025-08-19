import os
import pytest

# ----------------------------
# Pure functions to test
# ----------------------------

def get_env_config(env: str = None):
    """Return config for environment."""
    env = (env or os.getenv("APP_ENV", "dev")).lower()
    config = {"title": "Unknown Environment", "bg_color": "white", "status": "unknown"}

    if env == "dev":
        config.update({"title": "Dev Environment", "bg_color": "lightgreen", "status": "success"})
    elif env == "prod":
        config.update({"title": "Production Environment", "bg_color": "lightcoral", "status": "error"})

    return config

def check_api_key(env: str = None):
    """Return API key info without exposing the key."""
    env = env or os.getenv("APP_ENV", "dev")
    api_key = os.getenv("APP_KEY", "")
    return {"env": env, "has_key": bool(api_key), "key_length": len(api_key)}


# ----------------------------
# Tests (Production Only)
# ----------------------------

@pytest.mark.prod
@pytest.mark.parametrize(
    "env,expected_title,expected_color,expected_status",
    [
        ("dev", "Dev Environment", "lightgreen", "success"),
        ("prod", "Production Environment", "lightcoral", "error"),
        ("unknown", "Unknown Environment", "white", "unknown"),
    ],
)
def test_get_env_config(env, expected_title, expected_color, expected_status):
    config = get_env_config(env)
    assert config["title"] == expected_title
    assert config["bg_color"] == expected_color
    assert config["status"] == expected_status

@pytest.mark.prod
def test_env_default():
    os.environ.pop("APP_ENV", None)
    config = get_env_config()
    assert config["title"] == "Dev Environment"
    assert config["bg_color"] == "lightgreen"

@pytest.mark.prod
def test_api_key_missing(monkeypatch):
    monkeypatch.delenv("APP_KEY", raising=False)
    result = check_api_key("prod")
    assert result["env"] == "prod"
    assert not result["has_key"]
    assert result["key_length"] == 0

@pytest.mark.prod
def test_api_key_present(monkeypatch):
    monkeypatch.setenv("APP_KEY", "dummy-secret-key")
    result = check_api_key("prod")
    assert result["env"] == "prod"
    assert result["has_key"]
    assert result["key_length"] == len("dummy-secret-key")