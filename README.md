<a href="https://docker.com">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Docker_(container_engine)_logo.png" alt="docker logo" title="docker" align="right" height="60" />
</a>

Ansible Role: docker
====================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/docker/master)](https://ci.devops.sosoftware.pl/job/SoInteractive/docker/master) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18218.svg)](https://galaxy.ansible.com/SoInteractive/docker/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role adds repositories, installs, and configures docker. It can also manage docker containers and install cAdvisor for monitoring purposes.

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.docker
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO:
-----
* creating docker-swarm in docker > 1.12.
* centos 7 support
