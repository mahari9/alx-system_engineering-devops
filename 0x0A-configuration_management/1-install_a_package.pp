# Install an especific version of flask (2.1.0)

exec {'install python packages':
  command => 'pip3 install flask==2.1.0 Werkzeug==3.0.2',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/test -f /usr/local/lib/python3.8/dist-packages/flask/app.py',
  }
