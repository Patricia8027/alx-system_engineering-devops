# Update package lists
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  before  => Package['php5-curl'],
}

# Install necessary packages
package { ['apache2', 'php5']:
  ensure => installed,
}

# Install php5-curl package
package { 'php5-curl':
  ensure   => installed,
  provider => apt,
  require  => Exec['apt-get update'],
}

# Restart Apache service
service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  subscribe  => [
    Package['php5'],
    Package['php5-curl'],
  ],
}



