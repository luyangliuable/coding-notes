# Kubernetes
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Kubernetes](#kubernetes)
    - [Kubectl](#kubectl)

<!-- markdown-toc end -->

* Get all kubernete service
```ps1
kubectl get all
```

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
```sh
Kubectl apply [resource]
```


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


TODO Hold off

git clone https://luyangliuable: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@github.com/wexinc/ps-treasury-bta-bank-transfer.git

git clone https://github.com/wexinc/ps-treasury-bta-bank-transfer.git
