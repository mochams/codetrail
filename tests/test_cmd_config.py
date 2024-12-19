import logging
import pytest

from codetrail import commands
from codetrail import exceptions
from codetrail.cmd_config import get_config, set_config


def initialize_repository_command(path):
    return commands.InitializeRepository(path=path)


@pytest.mark.usefixtures("default_path")
class TestSetConfig:
    """Tests for `set_config` function."""

    def test_can_set_name_for_a_user(
        self,
        code_repository,
        config_parser,
    ):
        """Test sets user name in config."""
        set_config(commands.SetConfig(key="user.name", value="Chill Guy"))
        config_path = code_repository.config_path
        config_parser.read(config_path)

        assert config_parser.has_section("user")
        assert config_parser.has_option("user", "name")
        assert config_parser.get("user", "name") == "Chill Guy"

    def test_raises_exception_on_unsupported_section(
        self,
        code_repository,
        config_parser,
    ):
        """Test with wrong section."""
        with pytest.raises(exceptions.UnsupportedConfigError):
            set_config(commands.SetConfig(key="users.name", value="Chill Guy"))

    def test_raises_exception_on_unsupported_option(
        self,
        code_repository,
        config_parser,
    ):
        """Test with wrong option."""
        with pytest.raises(exceptions.UnsupportedConfigError):
            set_config(commands.SetConfig(key="user.names", value="Chill Guy"))


@pytest.mark.usefixtures("default_path")
class TestGetConfig:
    """Tests for `get_config` function."""

    def test_can_get_name_for_a_user(self, code_repository, config_parser, caplog):
        """Test gets user name from config."""
        set_config(commands.SetConfig(key="user.name", value="Chill Guy"))

        with caplog.at_level(logging.INFO):
            get_config(commands.GetConfig(key="user.name"))
            assert "Chill Guy" in caplog.text

    def test_raises_exception_on_unsupported_section(
        self,
        code_repository,
        config_parser,
    ):
        """Test with wrong section."""
        with pytest.raises(exceptions.UnsupportedConfigError):
            get_config(commands.GetConfig(key="users.name"))

    def test_raises_exception_on_unsupported_option(
        self,
        code_repository,
        config_parser,
    ):
        """Test with wrong option."""
        with pytest.raises(exceptions.UnsupportedConfigError):
            get_config(commands.GetConfig(key="user.names"))
