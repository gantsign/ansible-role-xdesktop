import pytest

@pytest.mark.parametrize('executable', [
    ('xfce4-about'),
    ('xfce4-mixer'),
    ('xfce4-taskmanager'),
    ('dockx'),
    ('evince'),
    ('gedit'),
    ('gnome-calculator'),
    ('seahorse')
])
def test_for_executables(Command, executable):
    assert Command('which ' + executable).rc == 0

def test_for_libdockbarx(File):
    docx = File('/usr/lib/xfce4/panel/plugins/libdockbarx.so')

    assert docx.exists
    assert docx.is_file
    assert docx.user == 'root'
    assert docx.group == 'root'
    assert oct(docx.mode) == '0644'

@pytest.mark.parametrize('config_path', [
    ('.config/xfce4/panel/dockbarx-9.rc'),
    ('.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml'),
    ('.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml')
])
def test_for_config(File, config_path):
    config_file = File('/home/test_usr/' + config_path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'test_usr'
    assert config_file.group == 'test_usr'
    assert oct(config_file.mode) == '0644'
