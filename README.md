<a href="https://docker.com">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Docker_(container_engine)_logo.png" alt="docker logo" title="docker" align="right" height="60" />
</a>

Ansible Role: docker
====================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-docker.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-docker) [![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.docker-blue.svg)](https://galaxy.ansible.com/SoInteractive/docker/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-docker.svg)](https://github.com/SoInteractive/ansible-docker/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

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