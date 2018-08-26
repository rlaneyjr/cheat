
Istio configuration command line utility.

Create, list, modify, and delete configuration resources in the Istio
system.

Available routing and traffic management configuration types:

	[virtualservice gateway destinationrule serviceentry httpapispec httpapispecbinding quotaspec quotaspecbinding servicerole servicerolebinding policy]

See https://istio.io/docs/reference/ for an overview of Istio routing.

Usage:
  istioctl [command]

Available Commands:
  authn          Interact with Istio authentication policies
  context-create Create a kubeconfig file suitable for use with istioctl in a non kubernetes environment
  create         Create policies and rules
  delete         Delete policies or rules
  deregister     De-registers a service instance
  experimental   Experimental commands that may be modified or deprecated
  gen-deploy     Generates the configuration for Istio's control plane.
  get            Retrieve policies and rules
  help           Help about any command
  kube-inject    Inject Envoy sidecar into Kubernetes pod resources
  proxy-config   Retrieve information about proxy configuration from Envoy [kube only]
  proxy-status   Retrieves the synchronization status of each Envoy in the mesh [kube only]
  register       Registers a service instance (e.g. VM) joining the mesh
  replace        Replace existing policies and rules
  version        Prints out build version information

Flags:
      --context string                The name of the kubeconfig context to use
  -h, --help                          help for istioctl
  -i, --istioNamespace string         Istio system namespace (default "istio-system")
  -c, --kubeconfig string             Kubernetes configuration file
      --log_as_json                   Whether to format output as JSON or in plain console-friendly format
      --log_caller string             Comma-separated list of scopes for which to include caller information, scopes can be any of [ads, default, model, rbac]
      --log_output_level string       Comma-separated minimum per-scope logging level of messages to output, in the form of <scope>:<level>,<scope>:<level>,... where scope can be one of [ads, default, model, rbac] and level can be one of [debug, info, warn, error, none] (default "default:info")
      --log_rotate string             The path for the optional rotating log file
      --log_rotate_max_age int        The maximum age in days of a log file beyond which the file is rotated (0 indicates no limit) (default 30)
      --log_rotate_max_backups int    The maximum number of log file backups to keep before older files are deleted (0 indicates no limit) (default 1000)
      --log_rotate_max_size int       The maximum size in megabytes of a log file beyond which the file is rotated (default 104857600)
      --log_stacktrace_level string   Comma-separated minimum per-scope logging level at which stack traces are captured, in the form of <scope>:<level>,<scope:level>,... where scope can be one of [ads, default, model, rbac] and level can be one of [debug, info, warn, error, none] (default "default:none")
      --log_target stringArray        The set of paths where to output the log. This can be any path as well as the special values stdout and stderr (default [stdout])
  -n, --namespace string              Config namespace
  -p, --platform string               Istio host platform (default "kube")

Use "istioctl [command] --help" for more information about a command.
