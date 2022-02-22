# Configuration management

### Resources:

1. [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
2. [puppet-lint](http://puppet-lint.com/)
3. [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
4. [Puppet docs](https://puppet.com/docs/puppet/3.8/index.html)

### Installing `puppet-lint`

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

### Running a manifest

```
puppet apply some_file.pp
```

### Using puppet-lint

```
puppet-lint some_file.pp

```



# Tasks


- ### 0-create_a_file.pp
This Puppet manifest creates a file in `/tmp`.<br>

- Requirements:
  - File path is `/tmp/holberton`
  - File permission is `0744`
  - File owner is `www-data`
  - File group is `www-data`
  - File contains `I love Puppet`

- ### 1-install_a_package.pp
This Puppet manifest installs `puppet-lint`.<br>

- Requirements:
  - Install `puppet-lint`
  - Version must be `2.1.1`

- ### 2-execute_a_command.pp
This Puppet manifest kills a process named `killmenow`.<br>
- Requirements
  - Must be the `exec` Puppet resource
  - Must use `pkill`

<br>
<br>

<img src="https://puppet.com/images/logos/puppet-logo-black.svg" width="160" height=auto/>
