# cmake -DSLIST=on .. or cmake -DDLIST=on or cmake -DCLIST=on ..
cmake_minimum_required (VERSION 3.22.1)


if (SLIST)
    add_definitions(-DSLIST_UP)
    project(slist)
    add_executable(slist src/v1/main.c src/v1/slist.c)
endif()

if (DLIST)
    add_definitions(-DDLIST_UP)
    project(dlist)
    add_executable(dlist src/v1/main.c src/v1/dlist.c)
endif()

if (CLIST)
    add_definitions(-DCLIST_UP)
    project(clist)
    add_executable(clist src/v1/main.c src/v1/clist.c)
endif()

if (STACK)
    add_definitions(-DSTACK_UP)
    project(stack)
    add_executable(stack src/v1/main.c src/v1/stack.c)
endif()

if (MAP)
    add_definitions(-DMAP_UP)
    project(map)
    add_executable(map src/v1/main.c src/v1/map.c)
endif()
