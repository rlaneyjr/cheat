Replace a resource by filename or stdin. 

JSON and YAML formats are accepted. If replacing an existing resource, the complete resource spec must be provided. This can be obtained by 

  $ kubectl get TYPE NAME -o yaml
  
Please refer to the models in https://htmlpreview.github.io/?https://github.com/kubernetes/kubernetes/blob/HEAD/docs/api-reference/v1/definitions.html to find if a field is mutable.

Examples:
  # Replace a pod using the data in pod.json.
  kubectl replace -f ./pod.json
  
  # Replace a pod based on the JSON passed into stdin.
  cat pod.json | kubectl replace -f -
  
  # Update a single-container pod's image version (tag) to v4
  kubectl get pod mypod -o yaml | sed 's/\(image: myimage\):.*$/\1:v4/' | kubectl replace -f -
  
  # Force replace, delete and then re-create the resource
  kubectl replace --force -f ./pod.json

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.
      --cascade=true: If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a ReplicationController).  Default true.
  -f, --filename=[]: to use to replace the resource.
      --force=false: Only used when grace-period=0. If true, immediately remove resources from API and bypass graceful deletion. Note that immediate deletion of some resources may result in inconsistency or data loss and requires confirmation.
      --grace-period=-1: Period of time in seconds given to the resource to terminate gracefully. Ignored if negative. Set to 1 for immediate shutdown. Can only be set to 0 when --force is true (force deletion).
  -o, --output='': Output format. One of: json|yaml|name|go-template|go-template-file|templatefile|template|jsonpath|jsonpath-file.
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.
      --save-config=false: If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --timeout=0s: The length of time to wait before giving up on a delete, zero means determine a timeout from the size of the object
      --validate=true: If true, use a schema to validate the input before sending it
      --wait=false: If true, wait for resources to be gone before returning. This waits for finalizers.

Usage:
  kubectl replace -f FILENAME [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
