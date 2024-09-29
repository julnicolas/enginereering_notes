# Definition of core concepts
## Chart
A `helm chart` is a set of configurations, templated
kubernetes manifests and manifests. Altogether they represent
a whole kubernetes application (or an infrastructure).

These charts can be shared similarly to an application
package (lib a .deb) to be able to deploy kubernetes applications/
infrastructure.

Bear in mind that in general the chart must generated so that it yields deployable
kubernetes manifests. 

Generated means that the template engine must be run to fill in the right values.

## Repository
It is a storage service which can be queried to store or retrieve
helm charts. It must track charts' versions.

## Release
A release is a deployed helm chart in a kubernetes cluster. Generated
kubernetes manifests are now live resources in the cluster.

Releases are versioned using the `app version field`.

## Conclusion
Helm can be sum up as:
```
Helm installs charts into Kubernetes, creating a new release for each installation.
And to find new charts, you can search Helm chart repositories.
```

