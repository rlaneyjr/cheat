Convert config files between different API versions. Both YAML and JSON formats are accepted. 

The command takes filename, directory, or URL as input, and convert it into format of version specified by --output-version flag. If target version is not specified or not supported, convert to latest version. 

The default output will be printed to stdout in YAML format. One can use -o option to change to output destination.

Examples:
  # Convert 'pod.yaml' to latest version and print to stdout.
  kubectl convert -f pod.yaml
  
  # Convert the live state of the resource specified by 'pod.yaml' to the latest version
  # and print to stdout in JSON format.
  kubectl convert -f pod.yaml --local -o json
  
  # Convert all files under current directory to latest version and create them all.
  kubectl convert -f . | kubectl create -f -

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.
  -f, --filename=[]: Filename, directory, or URL to files to need to get converted.
      --local=true: If true, convert will NOT try to contact api-server but run locally.
  -o, --output='yaml': Output format. One of: json|yaml|name|template|go-template|go-template-file|templatefile|jsonpath|jsonpath-file.
      --output-version='': Output the formatted object with the given group version (for ex: 'extensions/v1beta1').)
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --validate=true: If true, use a schema to validate the input before sending it

Usage:
  kubectl convert -f FILENAME [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
