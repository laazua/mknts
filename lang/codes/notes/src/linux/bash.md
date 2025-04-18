### Bash

- _函数_

```
#!/bin/bash

set -e

function func1 {
    echo "func1"
    ## caller
    caller 0 1
    echo "func1 end"
}


function func2 {
    echo "func2"
    # caller
    caller 0 1
    echo "func2 end"
    func1
}

function func3 {
    echo "func3"
    ## caller
    caller 0 1
    echo "func3 end"
    func2
}

func3
```
