# /etc/puppet/modules/user_limits/manifests/init.pp
class user_limits {
  exec { 'change-os-configuration-for-holberton-user':
    command => 'ulimit -n 4096 && su - holberton',
    path    => '/bin:/usr/bin:/sbin:/usr/sbin',
    user    => 'root',
    returns => [0, 1],
  }
}


