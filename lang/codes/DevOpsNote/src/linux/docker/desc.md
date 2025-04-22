# Docker


- [官方参考](https://docs.docker.com/reference/dockerfile/)

- **debootstrap制作基础镜像**
> 1. sudo apt install debootstrap
> 2. mkdir bullseys-base && cd bullseys-base
> 3. sudo debootstrap bullseye .
> 4. cd .. && sudo chroot bullseys-base (如果需要额外的配置,如网络配置,就需要这一步)
> 5. tar czvf bullseys-base.tar.gz bullseys-base
> 6. cat bullseys-base.tar.gz | podman import - bullseys-base:0.0.1
