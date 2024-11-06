# Demo App

## Build, run and test locally

```bash

docker build -t myimage .
docker run -e DEMOOPS="" -p 8080:8080 myimage

curl -X POST http://0.0.0.0:8080/ -H 'Content-Type: application/json' -d '{"input_1":12, "input_2":1}'
> {"output":[12,1]}
```

```bash
docker run -e DEMOOPS="add" -p 8080:8080 myimage

curl -X POST http://0.0.0.0:8080/ -H 'Content-Type: application/json' -d '{"input_1":12, "input_2":1}'
> {"output":13}
```

## Test on Kubernetes

```bash
kubectl port-forward svc/backend 8080
```

```bash
curl -X POST http://0.0.0.0:8080/ -H 'Content-Type: application/json' -d '{"input_1":12, "input_2":1}'
> {"output":[12,1]}
```
### Change operation

1. Update configMap for key: `operation` to one of following values `{"", "add", "mul"}` in file [./apps/backend/overlays/dev/kustomization.yaml](../apps/backend/overlays/dev/kustomization.yaml)
    - `operation="add"`
1. Add changes to git and commit, Push changes to remote repository
1. Wait for FluxCD to pickup the changes and apply them to the cluster
1. Test the new operation

```bash
curl -X POST http://0.0.0.0:8080/ -H 'Content-Type: application/json' -d '{"input_1":12, "input_2":1}'
> {"output":13}
```
