# https://puppet.com/docs/puppet/3.8/type.html#exec
# Kills a process
exec {  'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
