Retrieve policies and rules

Usage:
  istioctl get <type> [<name>] [flags]

Examples:
# List all virtual services
istioctl get virtualservices

# List all destination rules
istioctl get destinationrules

# Get a specific virtual service named bookinfo
istioctl get virtualservice bookinfo


Flags:
      --all-namespaces   If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.
  -h, --help             help for get
  -o, --output string    Output format. One of:yaml|short (default "short")

Global Flags:
      --context string                The name of the kubeconfig context to use
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
