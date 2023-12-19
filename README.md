This repo is a minimal setup to reproduce a potential pitfall (or even a bug) when using `package_type = "application"` packages in a host context.

The setup is:
1. `mock-gcc` defines `self.buildenv_info.define("CC", "mock-gcc")` etc. in its `package_info` method and exports some runtime libraries.
2. `package-a` uses `mock-gcc` in both the build context (for the compiler) and host context (to create a dependency on the runtime libs) to build a library.
3. `package-b` uses `package-a` as a library dependency.

The expected result is for the runtime libraries in `mock-gcc` to become a transitive dependency for `package-b` and nothing more.

However, when `mock-gcc` is used without `run=False` in `self.requires()` in `package-a`, the buildenv environment variables
get propagated into `package-b`'s buildenv as well, which is not at all expected.

To reproduce this run:
```
./test.sh
```

Expected result in `package-b`:
```
CC=
CXX=
FC=
```
Actual result:
```
CC=mock-gcc
CXX=mock-gcc
FC=mock-gcc
```
