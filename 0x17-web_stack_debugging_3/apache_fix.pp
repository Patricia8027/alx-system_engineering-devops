# This Puppet manifest ensures the proper configuration of the Apache web server

# Install the Apache package
package { 'apache2':
  ensure => installed,
}

# Configure the Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  content => template('apache/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Template for the Apache configuration file
template 'apache/apache2.conf.erb' {
  content => @(END)
    # This is the main Apache server configuration file.
    # It contains the configuration directives that
    # give the server its instructions.

    # Global Configuration
    ServerRoot "/etc/apache2"
    PidFile ${APACHE_PID_FILE}
    Timeout 300
    KeepAlive On
    MaxKeepAliveRequests 100
    KeepAliveTimeout 5

    # Multi-Processing Module (MPM)
    IncludeOptional mods-enabled/*.load
    IncludeOptional mods-enabled/*.conf

    # Modules
    LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
    LoadModule authz_core_module modules/mod_authz_core.so
    LoadModule auth_basic_module modules/mod_auth_basic.so
    LoadModule unixd_module modules/mod_unixd.so
    LoadModule dir_module modules/mod_dir.so
    LoadModule mime_module modules/mod_mime.so

    # Virtual Hosts
    IncludeOptional sites-enabled/*.conf
  END
}

# Ensure the Apache service is running and enabled
service { 'apache2':
  ensure => running,
  enable => true,
}



