Ansible Role: X Desktop
=======================

Role to install and configure the Xfce4 desktop to my preference.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Default format for the desktop clock (will be overriden by user specific setting)
xdesktop_default_clock_format: '%d %b, %H:%M'

# Users to configure the desktop for
users: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.xdesktop
      xdesktop_default_clock_format: '%b %d, %H:%M'
      users:
        - username: vagrant
          xdesktop_clock_format: '%d %b, %H:%M'
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
