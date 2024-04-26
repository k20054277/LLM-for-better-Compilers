FROM debian:12

# Create User
USER root
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN useradd -ms /bin/bash debian

# Install Env.
RUN apt-get -y update
RUN apt install -y build-essential git m4 scons zlib1g zlib1g-dev \
    libprotobuf-dev protobuf-compiler libprotoc-dev libgoogle-perftools-dev \
    python3-dev libboost-all-dev pkg-config libssl-dev
RUN apt install -y libpng-dev libpng++-dev libhdf5-dev
RUN apt install -y python3-pip python3-venv

# Install pre-requirements
RUN apt-get install -y automake
RUN apt-get install -y python3-dev
WORKDIR /home/debian
USER debian
RUN mkdir env
RUN python3 -m venv /home/debian/env/python
RUN source /home/debian/env/python/bin/activate
RUN pip3 install --upgrade pip --break-system-packages
RUN pip3 install wheel --break-system-packages

# Getting Compilers
USER root
RUN rm -rf /usr/bin/llvm-config
RUN apt -y autoremove
RUN apt-get -y install gcc-11 g++-11 cpp-11 wget lsb-release gnupg software-properties-common
RUN rm /usr/bin/cpp /usr/bin/gcc /usr/bin/g++  /usr/bin/gcov  /usr/bin/c++
RUN rm /usr/bin/cc
RUN ln -s /usr/bin/cpp-11 /usr/bin/cpp
RUN ln -s /usr/bin/gcc-11 /usr/bin/gcc
RUN ln -s /usr/bin/gcc-11 /usr/bin/cc
RUN ln -s /usr/bin/g++-11 /usr/bin/g++
RUN ln -s /usr/bin/g++-11 /usr/bin/c++
RUN ln -s /usr/bin/gcov-11 /usr/bin/gcov

RUN wget https://apt.llvm.org/llvm.sh
RUN chmod +x llvm.sh
RUN ./llvm.sh 13
RUN ln -s /usr/bin/llvm-config-13 /usr/bin/llvm-config
RUN apt-get install -y lld-13 llvm-13-dev clang-13
RUN apt-get install -y lld llvm llvm-dev clang
RUN apt-get install -y build-essential python3-dev automake cmake git flex bison libglib2.0-dev libpixman-1-dev python3-setuptools cargo libgtk-3-dev
RUN apt-get install -y ninja-build cmake
RUN apt-get install -y wget git make cmake llvm gdb coreutils
RUN apt-get install -y gcc-11-plugin-dev
RUN apt -y autoremove

# Update default clang to 13
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-13 1300 --slave /usr/bin/clang++ clag++ /usr/bin/clang++-13
RUN update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-13 1300

# Getting AFL++
USER debian
RUN git clone https://github.com/AFLplusplus/AFLplusplus.git
WORKDIR /home/debian/AFLplusplus
RUN git checkout f596a297c4de6a5e1a6fb9fbb3b4e18124a24f58
RUN AFL_USE_ASAN=0 make
USER root
RUN make install 

# Installing python
RUN apt-get -y update
RUN apt-get install -yq --fix-missing build-essential emacs-nox vim-tiny git inkscape jed libsm6 libxext-dev libxrender1 lmodern netcat-openbsd python3-dev tzdata unzip nano emacs ca-certificates wget gcc-12 gcc-12-plugin-dev curl screen  nginx clang llvm lld gdb

#Extras for R
RUN apt-get install -yq gfortran libreadline-dev zlib1g-dev librust-bzip2-dev liblzma-dev libpcre2-dev libcurl4-openssl-dev

#Support packages for Python
RUN apt-get install -y libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev

#Install Python 3.12.3
USER debian
WORKDIR /home/debian
RUN curl -O https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
RUN tar -xvzf Python-3.12.3.tgz
WORKDIR /home/debian/Python-3.12.3
RUN CC=/home/debian/AFLplusplus/afl-gcc CXX=/home/debian/AFLplusplus/afl-g++ ./configure --enable-static --disable-shared
RUN make
USER root
RUN make install

# Installing python 3.13.0
USER debian
WORKDIR /home/debian
RUN curl -O https://www.python.org/ftp/python/3.13.0/Python-3.13.0a5.tgz
RUN tar -xvzf Python-3.13.0a5.tgz
WORKDIR /home/debian/Python-3.13.0a5
RUN CC=/home/debian/AFLplusplus/afl-gcc CXX=/home/debian/AFLplusplus/afl-g++ ./configure --enable-static --disable-shared
RUN make
USER root
RUN make install

USER root
RUN apt-get install -y sudo python3-dev
#Support packages for Python
RUN apt-get install -y libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Install numpy using apt-get
RUN apt-get update && apt-get install -y python3-numpy

# Install AFL dependencies and upgrade pip
RUN apt-get update \
    && apt-get install -y build-essential clang llvm \
    && pip3 install --upgrade pip

# Set up Python bindings
RUN pip3 install python-afl

# Set container folder structures and move executable files from project folder

RUN mkdir -p /home/debian/Python-3.12.3/debug
RUN mkdir -p /home/debian/Python-3.13.0a5/debug

RUN mkdir -p /home/debian/Python-3.13.0a5/output
RUN mkdir -p /home/debian/Python-3.12.3/output

WORKDIR /home/debian/Python-3.13.0a5
COPY run_cpython_3.13.py .
WORKDIR /home/debian/Python-3.12.3
COPY run_cpython_3.12.py .

WORKDIR /home/debian/
RUN mkdir -p /home/debian/gemma
RUN mkdir -p /home/debian/mistral
RUN mkdir -p /home/debian/codellama
RUN mkdir -p /home/debian/gemma_out
RUN mkdir -p /home/debian/mistral_out
RUN mkdir -p /home/debian/codellama_out
RUN mkdir -p /home/debian/compare/3.13
RUN mkdir -p /home/debian/compare/3.12

COPY mistral mistral/
COPY codellama codellama/
COPY gemma gemma/

COPY delete_empty.py .
COPY move_all.py .
COPY compare.py .


