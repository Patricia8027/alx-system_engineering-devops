# Puppet manifest to change the OS configuration for the holberton user
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 4096 && su - holberton',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  user    => 'root',
  returns => [0, 1],
}



