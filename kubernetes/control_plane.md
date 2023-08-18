# Control Plane
The control plane is a set of nodes administering worker nodes
(nodes with application workload).

It is made up of the following components:
- `kube-apiserver`: server API exposing cluster resources and acting on them
    it is made to be scaled horizontally. It is the frontend to interact
    with the control plane
- `etcd`: a consitent and highly available key value store containing all
    cluster data. A proper backup plan needs to be put in place to rescue
    etcd.
- `kube-scheduler`: schedules newly-created pods for running by finding them
    a node to run on depending on factors such as available resources and
    affinity (amongst others)
- `kube-controller-manager`: a control loop that runs several controller
    processes. For operation simplicity all controllers run from a single
    process in a single binary however, they perform distinct tasks such as:
        - pod management (pod controller)
            responsible of noticing and reacting when pods go down
        - node management (node controller)
            responsible of noticing and reacting when pods go down
        - EndPointSlice management (EndPointSlice controller)
            populates endpoint-slice objects to provide a link between
            services and pods
- `cloud-controller-manager`: cloud-specific controller which interfaces
    with cloud resources so that cluster resources can be allocated/deallocated
    or more generally managed (it can provide info on availability).
    *This controller doesn't manage cluster resource, it is an interface to provide
    cloud-specific resources in a portable way.*
    The cloud-controller-manager runs the following controller processes (and more):
        - node controller: check if a cloud node is deleted from the node pool after
            it stopped responding
        - route controller: for setting network routes in the underlying cloud
            infrastructure
        -service controller: for creating, updating, deleting cloud-provider load-balancers
    *On premise clouds do not need a cloud-controller-manager as cluster nodes would
    be reachable from the control plane.*
