### imux

- 描述
一个使用Kustomize工具的示例

- 使用
1. cd imux/bases && kustomize edit fix .
2. cd imux/overlays/dev && kustomize edit fix .
3. cd imux/overlays/prod && kustomize edit fix .
4. cd imux/overlays/test && kustomize edit fix .
5. cd imux/overlays/staging && kustomize edit fix .
6. 部署：kubectl apply -k overlays/dev
7. 卸载: kubectl delete -k overlays/dev