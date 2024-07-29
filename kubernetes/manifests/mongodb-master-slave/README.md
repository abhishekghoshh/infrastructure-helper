### start the statefullset:
- kubectl apply -f mongo-secret.yaml
- kubectl apply -f mongo-configmap.yaml
- kubectl apply -f mongo-storage-class.yaml
- kubectl apply -f mongo-headless-service.yaml
- kubectl apply -f mongo-statefullset.yaml

### stop the statefullset:
- kubectl delete -f mongo-statefullset.yaml
- kubectl delete -f mongo-secret.yaml
- kubectl delete -f mongo-configmap.yaml
- kubectl delete -f mongo-storage-class.yaml
- kubectl delete -f mongo-headless-service.yaml


https://www.mongodb.com/docs/manual/reference/method/rs.initiate/

```
kubectl exec -it mongo-0 -- mongo

rs.initiate(
    {
      _id: "rs0",
      version: 1,
      members: [
         { _id: 0, host : "mongo-0.mongo.default.svc.cluster.local:27017" },
         { _id: 1, host : "mongo-1.mongo.default.svc.cluster.local:27017" },
         { _id: 2, host : "mongo-2.mongo.default.svc.cluster.local:27017" }
      ]
   }
)
rs.status()
use persons

db.person.insert({"firstName": "Abhishek","lastName": "Ghosh","age": 25,"gender": "Male"})
db.person.insert({"firstName": "Nasim","lastName": "Molla","age": 26,"gender": "Male"})
```

```
kubectl exec -it mongo-1 -- mongo
rs.slaveOk()
rs.status()
use persons
db.person.findOne()
```

```
kubectl run -i --tty mongo --image=mongo:4.0.8 --restart=Never -- bash

mongo "mongodb://mongo-0.mongo.default.svc.cluster.local:27017,mongo-1.mongo.default.svc.cluster.local:27017,mongo-1.mongo.default.svc.cluster.local:27017/?replicaSet=rs0"
```

```
kubectl run -i --tty mongo --image=mongo:4.0.8 --restart=Never -- bash

mongo "mongodb://mongo-0.mongo.default.svc.cluster.local:27017"
```

minikube ssh

cd /tmp/hostpath-provisioner/default

## Find a way to connect to the statefull set from mongodb atlas