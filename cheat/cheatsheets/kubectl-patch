Update field(s) of a resource using strategic merge patch, a JSON merge patch, or a JSON patch. 

JSON and YAML formats are accepted. 

Please refer to the models in https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/docs/api-reference/v1/definitions.html to find if a field is mutable.

Examples:
  # Partially update a node using a strategic merge patch. Specify the patch as JSON.
  kubectl patch node k8s-node-1 -p '{"spec":{"unschedulable":true}}'
  
  # Partially update a node using a strategic merge patch. Specify the patch as YAML.
  kubectl patch node k8s-node-1 -p $'spec:\n unschedulable: true'
  
  # Partially update a node identified by the type and name specified in "node.json" using strategic merge patch.
  kubectl patch -f node.json -p '{"spec":{"unschedulable":true}}'
  
  # Update a container's image; spec.containers[*].name is required because it's a merge key.
  kubectl patch pod valid-pod -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'
  
  # Update a container's image using a json patch with positional arrays.
  kubectl patch pod valid-pod --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.
      --dry-run=false: If true, only print the object that would be sent, without sending it.
  -f, --filename=[]: Filename, directory, or URL to files identifying the resource to update
      --local=false: If true, patch will operate on the content of the file, not the server-side resource.
  -o, --output='': Output format. One of: json|yaml|name|template|go-template|go-template-file|templatefile|jsonpath|jsonpath-file.
  -p, --patch='': The patch to be applied to the resource JSON file.
      --record=false: Record current kubectl command in the resource annotation. If set to false, do not record the command. If set to true, record the command. If not set, default to updating the existing annotation value only if one already exists.
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --type='strategic': The type of patch being provided; one of [json merge strategic]

Usage:
  kubectl patch (-f FILENAME | TYPE NAME) -p PATCH [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
