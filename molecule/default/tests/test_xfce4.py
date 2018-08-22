import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('executable', [
    'xfce4-about',
    'xfce4-taskmanager',
    'dockx',
    'evince',
    'gedit',
    'gnome-calculator',
    'meld',
    'seahorse'
])
def test_for_executables(host, executable):
    assert host.run('which ' + executable).rc == 0


def test_for_libdockbarx(host):
    docx = host.file('/usr/lib/xfce4/panel/plugins/libdockbarx.so')

    assert docx.exists
    assert docx.is_file
    assert docx.user == 'root'
    assert docx.group == 'root'
    assert oct(docx.mode) == '0644'


@pytest.mark.parametrize('dir_path', [
    '/etc/xdg/ansible-xdesktop',
    '/etc/xdg/ansible-xdesktop/xfce4',
    '/etc/xdg/ansible-xdesktop/xfce4/panel',
    '/etc/xdg/ansible-xdesktop/xfce4/xfconf',
    '/etc/xdg/ansible-xdesktop/xfce4/xfconf/xfce-perchannel-xml'
])
def test_for_config_dirs(host, dir_path):
    dir = host.file(dir_path)

    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'
    assert oct(dir.mode) == '0755'


@pytest.mark.parametrize('config_path', [
    'xfce4/panel/dockbarx-9.rc',
    'xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml',
    'xfce4/panel/default.xml'
])
def test_for_config(host, config_path):
    config_file = host.file('/etc/xdg/ansible-xdesktop/' + config_path)

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert oct(config_file.mode) == '0644'


def test_for_x11config(host):
    config_file = host.file('/etc/X11/Xsession.d/70-ansible-xdesktop')

    assert config_file.exists
    assert config_file.is_file
    assert config_file.user == 'root'
    assert config_file.group == 'root'
    assert oct(config_file.mode) == '0644'
