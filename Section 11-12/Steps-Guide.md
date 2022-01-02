#### Step 1 - Basic Concepts

- go to `Docker` folder :

  -  run the following command

    ```bash
    $ docker-compose build spark-master
    $ docker-compose build pyspark
    $ docker-compose up -d
    ```
    
    this will start building the Images and setup the cluster

- got to `wsl` terminal and install `netcat`

  ```bash
  $ sudo apt update
  $ sudo apt install netcat
  $ nc -h
  ```

- put `netcat` in server mode to start communicating with :

  ```bash
  $ nc -l -p 9999
  ```

- go to  another `wsl` terminal and connect to this port :

  ```bash
  $ nc localhost 9999
  ```

- type in some words in Server/Client and you must see a chat style behavior

- install `netcat` in `pyspark` container and run the server with port number : 9999

  ```bash
  $ docker exec -it pyspark bash
  $ apt update
  $ apt install netcat
  $ nc -l -v -p 9999
  Hi
  Hello World
  ```

  

- go to `pyspark` container to get the `jupyter notebook` token

  ```bash
  $ docker logs pyspark
  ```

  - copy the provided `url` into your browser address bar . something like this :

  ```bash
  $ http://pyspark:8888/?token=0d6dbfc0f045b4a09e64ca8b2d53ffc8d75be188d1300494
       or http://127.0.0.1:8888/?token=0d6dbfc0f045b4a09e64ca8b2d53ffc8d75be188d1300494
  
  ```

  - go to **Step1** and run the notebooks.

#### Step 2 - A Practical Sample With Kafka

- please stop the `spark cluster`

  - go to console and in `Docker` folder run these commands

    ```bash
    $ docker-compose down -v
    $ docker-compose -f  docker-compose-kafka.yml up -d 
    ```

- go to `pyspark` container to get the `jupyter notebook` token

  ```bash
  $ docker logs pyspark
  ```

  - copy the provided `url` into your browser address bar . something like this :

  ```bash
  $ http://pyspark:8888/?token=0d6dbfc0f045b4a09e64ca8b2d53ffc8d75be188d1300494
       or http://127.0.0.1:8888/?token=0d6dbfc0f045b4a09e64ca8b2d53ffc8d75be188d1300494
  
  ```

  - go to **Step2** and run the notebooks.

#### Step 3 - Sample Data Pipeline

- similar to previous steps,  go to `jupyter notebook` and run the Step3 files





