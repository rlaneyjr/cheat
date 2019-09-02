## Tips

Sources:

* [15 Docker Tips in 5 minutes](http://sssslide.com/speakerdeck.com/bmorearty/15-docker-tips-in-5-minutes)
* [CodeFresh Everyday Hacks Docker](https://codefresh.io/blog/everyday-hacks-docker/)

### Prune

The new [Data Management Commands](https://github.com/docker/docker/pull/26108) have landed as of Docker 1.13:

* `docker system prune`
* `docker volume prune`
* `docker network prune`
* `docker container prune`
* `docker image prune`

### df

`docker system df` presents a summary of the space currently used by different docker objects.

### Heredoc Docker Container

```
docker build -t htop - << EOF
FROM alpine
RUN apk --no-cache add htop
EOF
```

### Last Ids

```
alias dl='docker ps -l -q'
docker run ubuntu echo hello world
docker commit $(dl) helloworld
```

### Commit with command (needs Dockerfile)

```
docker commit -run='{"Cmd":["postgres", "-too -many -opts"]}' $(dl) postgres
```

### Get IP address

```
docker inspect $(dl) | grep -wm1 IPAddress | cut -d '"' -f 4
```

or with [jq](https://stedolan.github.io/jq/) installed:

```
docker inspect $(dl) | jq -r '.[0].NetworkSettings.IPAddress'
```

or using a [go template](https://docs.docker.com/engine/reference/commandline/inspect):

```
docker inspect -f '{{ .NetworkSettings.IPAddress }}' <container_name>
```

or when building an image from Dockerfile, when you want to pass in a build argument:

```
DOCKER_HOST_IP=`ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d: | head -n1`
echo DOCKER_HOST_IP = $DOCKER_HOST_IP
docker build \
         --build-arg ARTIFACTORY_ADDRESS=$DOCKER_HOST_IP 
         -t sometag \
           some-directory/
           ```

### Get port mapping

           ```
           docker inspect -f '{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' <containername>
           ```

### Find containers by regular expression

           ```
           for i in $(docker ps -a | grep "REGEXP_PATTERN" | cut -f1 -d" "); do echo $i; done
           ```

### Get Environment Settings

           ```
           docker run --rm ubuntu env
           ```

### Kill running containers

  ```
docker kill $(docker ps -q)
  ```

### Delete all containers (force!! running or stopped containers)

  ```
docker rm -f $(docker ps -qa)
  ```

### Delete old containers

  ```
  docker ps -a | grep 'weeks ago' | awk '{print $1}' | xargs docker rm
  ```

### Delete stopped containers

  ```
docker rm -v $(docker ps -a -q -f status=exited)
  ```

### Delete containers after stopping

  ```
docker stop $(docker ps -aq) && docker rm -v $(docker ps -aq)
  ```

### Delete dangling images

  ```
docker rmi $(docker images -q -f dangling=true)
  ```

### Delete all images

  ```
docker rmi $(docker images -q)
  ```

### Delete dangling volumes

  As of Docker 1.9:

  ```
docker volume rm $(docker volume ls -q -f dangling=true)
  ```

  In 1.9.0, the filter `dangling=false` does _not_ work - it is ignored and will list all volumes.

### Show image dependencies

  ```
  docker images -viz | dot -Tpng -o docker.png
  ```

### Slimming down Docker containers

  - Cleaning APT in a RUN layer

  This should be done in the same layer as other apt commands.
  Otherwise, the previous layers still persist the original information and your images will still be fat.

  ```
  RUN {apt commands} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
                                   ```

                                   - Flatten an image
                                   ```
                                   ID=$(docker run -d image-name /bin/bash)
                                   docker export $ID | docker import – flat-image-name
                                   ```

                                   - For backup
                                   ```
                                   ID=$(docker run -d image-name /bin/bash)
                                   (docker export $ID | gzip -c > image.tgz)
                                   gzip -dc image.tgz | docker import - flat-image-name
                                   ```

### Monitor system resource utilization for running containers

To check the CPU, memory, and network I/O usage of a single container, you can use:
```
docker stats <container>
```

For all containers listed by id:
```
docker stats $(docker ps -q)
```

For all containers listed by name:
```
docker stats $(docker ps --format '{{.Names}}')
```

For all containers listed by image:
```
docker ps -a -f ancestor=ubuntu
```

Remove all untagged images:
```
docker rmi $(docker images | grep “^” | awk '{split($0,a," "); print a[3]}')
```

Remove container by a regular expression:
```
docker ps -a | grep wildfly | awk '{print $1}' | xargs docker rm -f
```

Remove all exited containers:
```
docker rm -f $(docker ps -a | grep Exit | awk '{ print $1 }')
```

### Volumes can be files

Be aware that you can mount files as volumes. For example you can inject a configuration file like this:

``` bash
# copy file from container
docker run --rm httpd cat /usr/local/apache2/conf/httpd.conf > httpd.conf

# edit file
vim httpd.conf

# start container with modified configuration
docker run --rm -it -v "$PWD/httpd.conf:/usr/local/apache2/conf/httpd.conf:ro" -p "80:80" httpd
```
