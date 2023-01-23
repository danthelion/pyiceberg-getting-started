FROM python:3.9-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      vim \
      unzip \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

## Download spark and hadoop dependencies and install
# Optional env variables
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

# Download spark
RUN curl https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz -o spark-3.3.1-bin-hadoop3.tgz \
 && tar xvzf spark-3.3.1-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-3.3.1-bin-hadoop3.tgz

# Download postgres connector jar
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.24.jar -o postgresql-42.2.24.jar \
 && cp postgresql-42.2.24.jar /opt/spark/jars \
 && rm postgresql-42.2.24.jar

# Download iceberg spark runtime
RUN curl https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.1.0/iceberg-spark-runtime-3.3_2.12-1.1.0.jar -Lo iceberg-spark-runtime-3.3_2.12-1.1.0.jar \
 && mv iceberg-spark-runtime-3.3_2.12-1.1.0.jar /opt/spark/jars

RUN curl https://tabular-repository-public.s3.amazonaws.com/releases/io/tabular/tabular-client-runtime/0.40.0/tabular-client-runtime-0.40.0.jar -Lo tabular-client-runtime-0.40.0.jar \
 && mv tabular-client-runtime-0.40.0.jar /opt/spark/jars

# Download URL connection client required for S3FileIO
RUN curl https://repo1.maven.org/maven2/software/amazon/awssdk/url-connection-client/2.17.257/url-connection-client-2.17.257.jar -Lo url-connection-client-2.17.257.jar \
 && mv url-connection-client-2.17.257.jar /opt/spark/jars

# Add iceberg spark runtime jar to IJava classpath
ENV IJAVA_CLASSPATH=/opt/spark/jars/*

RUN mkdir -p /home/iceberg/warehouse /home/iceberg/spark-events

COPY spark-defaults.conf /opt/spark/conf
ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"

RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
