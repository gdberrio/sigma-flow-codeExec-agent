FROM python:3.10-bullseye
#COPY install.sh .
RUN pip install pymc
#ENTRYPOINT [ "./install.sh" ]