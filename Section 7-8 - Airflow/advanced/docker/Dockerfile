FROM dockerhub.ir/apache/airflow:2.2.0
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential tzdata \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install \
      jdatetime \
      apache-airflow-providers-apache-hdfs>=2.1.0 \
      hdfs 
USER airflow      
