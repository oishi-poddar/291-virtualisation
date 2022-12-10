FROM --platform=linux/amd64 ubuntu:latest


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python3 \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    pip install numpy scipy scikit-learn pandas numpy datetime pyarrow boto3 nltk xlrd flask gevent gunicorn && \
        rm -rf /root/.cache


ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY digits /opt/program
WORKDIR /opt/program
