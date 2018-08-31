

kube-inject manually injects envoy sidecar into kubernetes
workloads. Unsupported resources are left unmodified so it is safe to
run kube-inject over a single file that contains multiple Service,
ConfigMap, Deployment, etc. definitions for a complex application. Its
best to do this when the resource is initially created.

k8s.io/docs/concepts/workloads/pods/pod-overview/#pod-templates is
updated for Job, DaemonSet, ReplicaSet, Pod and Deployment YAML resource
documents. Support for additional pod-based resource types can be
added as necessary.

The Istio project is continually evolving so the Istio sidecar
configuration may change unannounced. When in doubt re-run istioctl
kube-inject on deployments to get the most up-to-date changes.

To override the sidecar injection template built into istioctl, the
parameters --injectConfigFile or --injectConfigMapName can be used.
Both options override any other template configuration parameters, eg.
--hub and --tag.  These options would typically be used with the
file/configmap created with a new Istio release.

Usage:
  istioctl kube-inject [flags]

Examples:

# Update resources on the fly before applying.
kubectl apply -f <(istioctl kube-inject -f <resource.yaml>)

# Create a persistent version of the deployment with Envoy sidecar
# injected.
istioctl kube-inject -f deployment.yaml -o deployment-injected.yaml

# Update an existing deployment.
kubectl get deployment -o yaml | istioctl kube-inject -f - | kubectl apply -f -

# Create a persistent version of the deployment with Envoy sidecar
# injected configuration from kubernetes configmap 'istio-inject'
istioctl kube-inject -f deployment.yaml -o deployment-injected.yaml --injectConfigMapName istio-inject


Flags:
  -f, --filename string              Input Kubernetes resource filename
  -h, --help                         help for kube-inject
      --injectConfigFile string      injection configuration filename. Cannot be used with --injectConfigMapName
      --injectConfigMapName string   ConfigMap name for Istio sidecar injection, key should be "config".This option overrides any other sidecar injection config options, eg. --hub (default "istio-sidecar-injector")
      --meshConfigFile string        mesh configuration filename. Takes precedence over --meshConfigMapName if set
      --meshConfigMapName string     ConfigMap name for Istio mesh configuration, key should be "mesh" (default "istio")
  -o, --output string                Modified output Kubernetes resource filename

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
