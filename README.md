Ansible Role: X Desktop
=======================

[![Tests](https://github.com/gantsign/ansible-role-xdesktop/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-xdesktop/actions?query=workflow%3ATests)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-xdesktop/master/LICENSE)

Role to install and configure the Gnome desktop to my preference.

Requirements
------------

* Ansible Core >= 2.12

* Linux Distribution

    * Ubuntu

        * Focal (20.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The position of the dockbar
xdesktop_dock_position: LEFT

# Nerd Font version number
xdesktop_nerd_font_version: '3.0.2'

# The SHA256 of the Nerd Font redistributable package
xdesktop_nerd_font_redis_sha256sum: '4991258b7c97071238a7459f0d3bf81a893ae7b0c849dbc47ad52833a8db7f55'

# Directory to store files downloaded
xdesktop_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.xdesktop
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
