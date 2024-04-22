Command line used to find this crash:

afl-fuzz -m 80000 -t1000000 -i gemma/input/ -o gemma/output2/ -- Python-3.13.0a5/python @@

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 78.1 GB.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please post
to https://github.com/AFLplusplus/AFLplusplus/issues/286 once the issues
 are fixed :)

