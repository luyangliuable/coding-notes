# Kubernetes
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Kubernetes](#kubernetes)
    - [Pods](#pods)
    - [Service](#service)
    - [Nodes](#nodes)
    - [Clusters](#clusters)
    - [Kubectl](#kubectl)
    - [Minicube](#minicube)
    - [Aliasing kubectl](#aliasing-kubectl)

<!-- markdown-toc end -->

* Get all kubernete service
```ps1
kubectl get all
```

## GUI for kubernetes
* K9S

## Pods
 Wrapper for container typically runs a single applicaiton, provides some kubernetes specific config.

pod.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
    name: getting-started
    labels:
        name: getting-started
    spec:
        containers:
            name: getting-started
            image: getting-started
            imagePullPolicy: server
            ...TODO
```


## Service
Basically a load balancer used to route traffic to pods.

## Nodes
Runs the pods

## Clusters
A colleciton of Nodes, containers  one master node and one or mode "worker" nodes.

## Kubectl
* $kubectl

* Check Kubernetes versio
```sh
kubectl version
```

* View cluster info.
```sh
kubectl cluster-info
```


* View Retrieve info about Kubernetes Pods, deployment, services and more.

```sh
kubectl get all
```


* View Retrieve info about Kubernetes all Pods.

```sh
kubectl get pod -a
```

```sh
kubectl run [container-name] --image=[image-name]
```

* Forward a port to allow external access
```sh
kubectl port-forward [pod] [ports]
```


* Expose a port for a deployment/pod
```sh
kubectl expose
```


* Create a resource
```sh
kubectl create [resource]
```


* Create a resource
    * The resource is often the pod.yaml file.
```sh
Kubectl apply [resource]
```

## Minicube

## Aliasing kubectl
* These helps with saving time

```ps1
Set-Alias -Name k -Value kubectl
```


```ps1
Set-Alias -Name d -Value docker
```

```ps1
Set-Alias -Name dc -Value docker-compose
```

Set-Alias -Name gitkey -Value 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
