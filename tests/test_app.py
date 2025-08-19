import os
import pytest

# ----------------------------
# Pure functions to test
# ----------------------------

def get_env_config(env: str = None):
    """Return config for environment."""
    env = (env or os.getenv("APP_ENV", "prod")).lower()
    config = {"title": "Unknown Environment", "bg_color": "white", "status": "unknown"}

    if env == "prod":
        config.update({"title": "Production Environment", "bg_color": "lightcoral", "status": "error"})

    return config

def check_api_key(env: str = None):
    """Return API key info without exposing the key."""
    env = env or os.getenv("APP_ENV", "prod")
    api_key = os.getenv("APP_KEY", "")
    return {"env": env, "has_key": bool(api_key), "key_length": len(api_key)}

# ----------------------------
# Tests for main / prod
# ----------------------------

def test_get_env_config_prod():
    config = get_env_config("prod")
    assert config["title"] == "Production Environment"
    assert config["bg_color"] == "lightcoral"
    assert config["status"] == "error"

def test_env_default_prod():
    os.environ.pop("APP_ENV", None)
    config = get_env_config()
    assert config["title"] == "Production Environment"
    assert config["bg_color"] == "lightcoral"

def test_api_key_missing(monkeypatch):
    monkeypatch.delenv("APP_KEY", raising=False)
    result = check_api_key("prod")
    assert result["env"] == "prod"
    assert result["has_key"] is False
    assert result["key_length"] == 0

def test_api_key_present(monkeypatch):
    monkeypatch.setenv("APP_KEY", "dummy-secret-key")
    result = check_api_key("prod")
    assert result["env"] == "prod"
    assert result["has_key"] is True
    assert result["key_length"] == len("dummy-secret-key")