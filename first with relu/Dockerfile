FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install torch pandas matplotlib scikit-learn

CMD ["jupyter", "notebook","--ip=0.0.0.0","--allow-root","--no-browser"]