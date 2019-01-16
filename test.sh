python3 setup.py build
#PYTHONPATH="$PWD/build/lib.linux-x86_64-3.7" valgrind --leak-check=full --show-leak-kinds=all python memleak.py
PYTHONPATH="$PWD/build/lib.linux-x86_64-3.7" python memleak.py
