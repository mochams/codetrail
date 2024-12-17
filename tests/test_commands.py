from codetrail import commands


def test_base_command_has_default_path():
    command = commands.BaseCommand()
    assert command.default_path == "."


def test_set_config_command_returns_section_and_option():
    command = commands.SetConfig(key="user.name", value="chill guy")
    assert command.section == "user"
    assert command.option == "name"
