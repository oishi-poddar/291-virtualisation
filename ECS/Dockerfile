FROM --platform=linux/amd64 python:3

WORKDIR /Users/nidhidhamnani/Documents/courses/fall2022/cse291d/project

COPY predict.py .

COPY app.py .

RUN pip3 install -U scikit-learn

RUN pip3 install Flask

EXPOSE 80

CMD ["python3", "app.py"]