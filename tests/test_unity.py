import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('dir_path', [
    '/usr/share/X11/xorg.conf.d',
    '/usr/share/glib-2.0/schemas'
])
def test_for_config_dirs(File, dir_path):
    dir = File(dir_path)

    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'
    assert oct(dir.mode) == '0755'

@pytest.mark.parametrize('config_path', [
    '/usr/share/X11/xorg.conf.d/60-ansible-screensaver.conf',
    '/usr/share/glib-2.0/schemas/20_ansible_screensaver.gschema.override',
    '/usr/share/glib-2.0/schemas/20_ansible_lockscreen.gschema.override'
])
def test_for_config(File, config_path):
    config_file = File(config_path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert oct(config_file.mode) == '0644'
