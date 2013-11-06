from subprocess import Popen

tests = [runtest_sequences.py -s 10.111.4.110 -i 10.111.1.134   -a ui-test-acct-02 -u user00 -w mypassword5 -t keypair_operations, runtest_sequences.py -s 10.111.4.110 -i 10.111.1.134   -a ui-test-acct-01 -u user00 -w mypassword3 -t instance_operations]
processes = []
for test in tests:
processes.append(Popen('python %s' % test, shell=True))
for process in processes:
process.wait()