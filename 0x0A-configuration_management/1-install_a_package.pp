#!/usr/bin/pup
# Define a package resource to install Flask (version 2.1.0)
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  }

# Define a package resource to install Werkzeug (version 2.1.1)
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  }
