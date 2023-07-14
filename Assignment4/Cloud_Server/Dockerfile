FROM ubuntu
WORKDIR /
COPY . .
RUN apt update
RUN apt install python3 -y
RUN mkdir /database
RUN mkdir  /database/query_data
RUN mkdir /database/factor_data
RUN touch /database/query_data/query.txt
RUN touch /database/factor_data/prime_factors.txt
CMD bash ./script.sh
EXPOSE 2002     