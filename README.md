# sdu-se-research-talk

SDU SE Research Talk Dec 2024

## Status

- [![Build and push - Demo App to Docker Hub](https://github.com/anbaephd/sdu-se-research-talk/actions/workflows/build-push.yml/badge.svg)](https://github.com/anbaephd/sdu-se-research-talk/actions/workflows/build-push.yml)
- [![Dependabot Updates](https://github.com/anbaephd/sdu-se-research-talk/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/anbaephd/sdu-se-research-talk/actions/workflows/dependabot/dependabot-updates)

## Prerequisites

- Ensure to have admin access to the Kubernetes Cluster, installed the `kubectl` CLI and access to a GitHub repository.
- Install `flux` CLI

    ```bash
    brew install fluxcd/tap/flux
    ```

## Initilize repository

1. A folder structure of the repository may look this:

    ```text
    .
    ├── apps
    │   └── backend
    │       ├── base
    │       │   ├── deployment.yaml
    │       │   ├── kustomization.yaml
    │       │   └── service.yaml
    │       └── overlays
    │           ├── dev
    │           │   └── kustomization.yaml
    │           └── prod
    ├── clusters
        ├── dev
        │   ├── apps.yaml
        │   └── flux-system             # content will be generated from flux bootstrap process
        │       ├── gotk-components.yaml
        │       ├── gotk-sync.yaml
        │       └── kustomization.yaml
        └── prod 
    ```

1. Bootstrap git rerepository and kubernetes cluster
    1. Cerate a token on github for repository access. *For accessing the GitHub API, the boostrap command requires a GitHub personal access token (PAT) with administration permissions.*
    2. Bootstrap the repository

        ```bash
        flux bootstrap github \
        --owner=anbaephd \
        --repository=sdu-se-research-talk \
        --branch=main \
        --path=./clusters/dev \
        --personal
        ```
        
        or 
        
        ```bash
        flux bootstrap github \
        --owner=anbaephd \
        --repository=sdu-se-research-talk \
        --branch=main \
        --path=./clusters/dev
        ```

    3. Use PAT, eg.

        ```bash
        echo $GITHUB_FLUX_TOKEN
        ```

1. Do what you need to do...
1. Cleanup

    ```bash
    flux uninstall
    ```
