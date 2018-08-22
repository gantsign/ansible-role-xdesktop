Ansible Role: X Desktop
=======================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-xdesktop.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-xdesktop)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-xdesktop/master/LICENSE)

Role to install and configure the Xfce4 desktop to my preference.

Requirements
------------

* Ansible >= 2.4

* Linux Distribution

    * Ubuntu

        * Xenial (16.04)

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The desktop environment to install (unity or xfce4)
xdesktop_desktop: unity

# The format for the desktop clock (applies to xfce4 only)
xdesktop_clock_format:

# Users to configure the desktop for
users: []
```

Example Playbooks
-----------------

Unity playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.xdesktop
      xdesktop_desktop: unity
```

Xfce4 playbook:

```yaml
- hosts: servers
  roles:
    - role: gantsign.xdesktop
      xdesktop_desktop: xfce4
      xdesktop_clock_format: '%b %d, %H:%M'
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

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
