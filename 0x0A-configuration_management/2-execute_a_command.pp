# Using Puppet, create a manifest that kills a process named killmenow
exex { 'killmenow'
  command  => 'pkill killmenow',
  provider => '/usr/bin/'
}
