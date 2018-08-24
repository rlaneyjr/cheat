Attach to a process that is already running inside an existing container.

Examples:
  # Get output from running pod 123456-7890, using the first container by default
  kubectl attach 123456-7890
  
  # Get output from ruby-container from pod 123456-7890
  kubectl attach 123456-7890 -c ruby-container
  
  # Switch to raw terminal mode, sends stdin to 'bash' in ruby-container from pod 123456-7890
  # and sends stdout/stderr from 'bash' back to the client
  kubectl attach 123456-7890 -c ruby-container -i -t
  
  # Get output from the first pod of a ReplicaSet named nginx
  kubectl attach rs/nginx

Options:
  -c, --container='': Container name. If omitted, the first container in the pod will be chosen
      --pod-running-timeout=1m0s: The length of time (like 5s, 2m, or 3h, higher than zero) to wait until at least one pod is running
  -i, --stdin=false: Pass stdin to the container
  -t, --tty=false: Stdin is a TTY

Usage:
  kubectl attach (POD | TYPE/NAME) -c CONTAINER [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
