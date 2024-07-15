# Install necessary packages
package { ['apache2', 'php5', 'php5-curl']:
  ensure => installed,
}

# Check for missing PHP extension
exec { 'check-php-curl-extension':
  command => 'php -m | grep -q curl',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'php -m | grep -q curl',
  notify  => Exec['install-php-curl-extension'],
}

# Install PHP curl extension if missing
exec { 'install-php-curl-extension':
  command     => 'apt-get install -y php5-curl',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
  notify      => Service['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  require    => [Package['apache2'], Package['php5'], Package['php5-curl']],
}



