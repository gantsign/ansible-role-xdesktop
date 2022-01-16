Ansible Role: X Desktop
=======================

[![Tests](https://github.com/gantsign/ansible-role-xdesktop/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-xdesktop/actions?query=workflow%3ATests)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-xdesktop/master/LICENSE)

Role to install and configure the Gnome desktop to my preference.

Requirements
------------

* Ansible >= 5.2

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
xdesktop_nerd_font_version: '2.1.0'

# The SHA256 of the Nerd Font redistributable package
xdesktop_nerd_font_redis_sha256sum: '842013fa44b6896d4eb91635a81ef75244d78d7f61ff866c9dfd3315a67788cd'

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

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
