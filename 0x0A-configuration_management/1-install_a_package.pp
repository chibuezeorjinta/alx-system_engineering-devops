# Install a package and ensure the version
package{'flask':
  ensure  =>  '2.1.0',
  provider	=>	'pip3',
}
